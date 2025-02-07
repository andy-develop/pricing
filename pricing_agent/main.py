from flask import Flask, request, render_template
import os
from PIL import Image
import requests
import json

app = Flask(__name__)


from analysis_utils import analyze_input


from artist_popularity import search_artist_popularity


from price_utils import estimate_price



def confirm_values():
    # Get the updated values from the form
    updated_values = {field: request.form.get(field) for field in request.form if field != 'analysis_result'}

    # Get the original analysis_result from the hidden input
    analysis_result = json.loads(request.form.get('analysis_result'))

    # Update the analysis_result with the new values
    def update_analysis_result(analysis_result, updated_values):
        # Update the analysis_result with the new values
        analysis_result.update(updated_values)
        return analysis_result

    analysis_result = update_analysis_result(analysis_result, updated_values)

    # Search artist popularity
    popularity = search_artist_popularity(analysis_result['artist'])

    # Estimate price
    price_estimate = estimate_price({**analysis_result, **popularity})

    return render_template('result.html',
                           analysis=analysis_result,
                           popularity=popularity,
                           estimate=price_estimate)


@app.route('/confirm_values', methods=['POST'])
def handle_confirm_values():
    return confirm_values()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        if 'image' in request.files:
            image = request.files['image']
            image_path = os.path.join('uploads', image.filename)
            image.save(image_path)

        text_input = request.form.get('text_input', '')

        # Analyze input
        analysis_result = analyze_input(image_path, text_input)

        # Check and fill missing or unknown values
        def fill_missing_values(analysis_result):
            missing_fields = []
            for key, value in analysis_result.items():
                if value is None or value == 'Unknown':
                    missing_fields.append(key)
            
            if missing_fields:
                # Define predefined options for size, content, and style
                predefined_options = {
                    '尺寸': ['大', '适中', '小'],
                    '内容': ['人物', '动物', '植物', '大自然', '图案'],
                    '风格': ['印象派', '现代派', '抽象派']
                }

                # Render the fill_values.html template with predefined options and current analysis_result
                return render_template(
                    'fill_values.html',
                    missing_fields=missing_fields,
                    analysis_result=analysis_result,
                    predefined_options=predefined_options
                )
            
            # If no missing fields, return the original analysis_result
            return analysis_result

        # Call the function to check and fill missing values
        analysis_result = fill_missing_values(analysis_result)

        # Search artist popularity
        popularity = search_artist_popularity(analysis_result['artist'])

        # Estimate price
        price_estimate = estimate_price({**analysis_result, **popularity})

        return render_template('result.html',
                               analysis=analysis_result,
                               popularity=popularity,
                               estimate=price_estimate)

    return render_template('index.html')




if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(port=5000)