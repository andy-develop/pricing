from pathlib import Path
import os
from openai import OpenAI
import base64

def get_openai_client():
    return OpenAI()


def get_kimi_client():
    return OpenAI(
        api_key="sk-z88fu1d9T4M8RuiiCeVteOnqrRSN9SmhF1w1Mmw0RLudPwp0",
        base_url="https://api.moonshot.cn/v1",
    )


def analyze_with_llm(image_url, text_input, model="kimi"):
    if model == "openai":
        client = get_openai_client()
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": text_input},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                            }
                        },
                    ],
                }
            ],
        )
        return completion.choices[0].message.content
    elif model == "kimi":
        client = get_kimi_client()
        if not image_url:
            messages = [
                {
                    "role": "system",
                    "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。",
                },
                {"role": "user", "content": text_input},
            ]
            completion = client.chat.completions.create(
                model="moonshot-v1-32k",
                messages=messages,
                temperature=0.3,
            )
            return completion.choices[0].message.content
        else:
            # Upload file if it's a local path
            if image_url:
                with open(image_url, 'rb') as f:
                    img_base = base64.b64encode(f.read()).decode('utf-8')

                response = client.chat.completions.create(
                    model="moonshot-v1-8k-vision-preview",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{img_base}"
                                    }
                                },
                                {
                                    "type": "text",
                                    "text": text_input
                                }
                            ]
                        }
                    ]
                )
                return response.choices[0].message.content
            else:
                raise ValueError("Kimi model currently only supports local files")
    else:
        raise ValueError(f"Unsupported model: {model}")


if __name__ == "__main__":
    client = get_kimi_client()