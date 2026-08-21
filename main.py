import json
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")


if not API_KEY:
    raise SystemExit(
        "未找到 DEEPSEEK_API_KEY。请复制 .env.example 为 .env，并填写你的 DeepSeek API Key。"
    )


client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def load_prompt() -> str:
    with open("prompts/storyboard_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()


def analyze_script(script: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": load_prompt()},
            {
                "role": "user",
                "content": f"请分析下面的剧本：\n\n{script}",
            },
        ],
    )

    content = response.choices[0].message.content or ""

    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError(
            "DeepSeek 返回的内容不是合法 JSON。原始返回内容：\n" + content
        ) from exc


def main() -> None:
    print("=== AI 漫剧剧本拆镜工具 v0.1 ===")
    print("请输入剧本，输入空行两次结束：")

    lines = []
    empty_lines = 0

    while True:
        line = sys.stdin.readline()
        if not line:
            break

        line = line.rstrip("\n")
        if not line.strip():
            empty_lines += 1
            if empty_lines >= 2:
                break
        else:
            empty_lines = 0
            lines.append(line)

    script = "\n".join(lines).strip()

    if not script:
        raise SystemExit("没有输入剧本，程序结束。")

    print("\n正在调用 DeepSeek 分析剧本，请稍候...\n")

    result = analyze_script(script)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
