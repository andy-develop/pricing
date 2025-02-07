import json
from llm_utils import analyze_with_llm

def estimate_price(analysis_result):
    # Prepare prompt for LLM
    prompt = f"""根据以下信息估算艺术品的价格：
    - 艺术家: {analysis_result.get('艺术家', 'Unknown')}
    - 艺术家在百度中知名度: {analysis_result.get('百度', 'Unknown')}
    - 艺术家在小红书中知名度: {analysis_result.get('小红书', 'Unknown')}
    
    作品的特征：
    - 内容: {analysis_result.get('内容', 'Unknown')}
    - 技法: {analysis_result.get('技法', 'Unknown')}
    - 尺寸: {analysis_result.get('尺寸', '适中')}
    - 风格: {analysis_result.get('风格', 'Unknown')}

    提供一个价格估算或价格区间，并解释其背后的理由。以json格式输出结果，案例：{{'价格': '','原因': ''}}。直接输出结果：
    """

    # Get price estimate from LLM
    price_estimate = analyze_with_llm(None, prompt)

    # Parse the response (this is a simple example, you might want to improve parsing)
    try:
        price_dict = json.loads(price_estimate)
    except json.JSONDecodeError:
        pass

    if price_dict not in locals():
        price_dict = {
            '价格': '未知',
            '原因': '未知'
        }

    return price_dict



