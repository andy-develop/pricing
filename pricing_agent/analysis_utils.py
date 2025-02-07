from pathlib import Path
import os
import json
from llm_utils import analyze_with_llm

def analyze_input(image_path, text_input):
    # Convert local image path to URL
    image_url = f"file://{os.path.abspath(image_path)}"

    # Prepare prompt for LLM
    prompt = f"""
    <用户描述>
    {text_input}
    
    <任务>
    总结和分析这幅画作和用户描述，并提供以下详细信息：
    - 艺术家姓名或风格
    - 作品内容/主题
    - 使用的技法
    - 尺寸分类（小、中、大）

    以json格式输出结果，案例：{{'艺术家': '','内容': '','技法': '','尺寸': ''}}。直接输出结果："""

    # Get analysis from LLM
    analysis = analyze_with_llm(image_url, prompt)

    # Parse the response (this is a simple example, you might want to improve parsing)
    try:
        analysis_dict = json.loads(analysis)
    except json.JSONDecodeError:
        pass

    if analysis_dict not in locals():
        analysis_dict = {
            '艺术家': '未知',
            '内容': '未知',
            '技法': '未知',
            '尺寸': '适中',
        }

    return analysis_dict

if __name__ == "__main__":
    prompt = "<用户描述>\n我想买一副画给女朋友，挂在卧室，尺寸适中，看看价格多少合适？<任务>\n总结和分析这幅画作和用户描述，并提供以下详细信息：\n- 艺术家姓名或风格\n- 作品内容/主题\n- 使用的技法\n- 尺寸分类（小、中、大）\n\n以json格式输出结果，案例：{{'艺术家': '','内容': '','技法': '','尺寸': ''}}。直接输出结果："
    analysis = analyze_with_llm(None, prompt)
    print(analysis)