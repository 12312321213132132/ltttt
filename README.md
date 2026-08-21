# AI 漫剧剧本拆镜工具

第一版目标：将一段中文短剧/漫剧剧本发送给 DeepSeek，自动整理成结构化的镜头 JSON。

## 功能

- 输入中文剧本
- 调用 DeepSeek Chat API
- 自动拆分场景与镜头
- 输出镜头号、时长、景别、机位、运镜、画面描述、生成提示词等字段
- API Key 从环境变量读取，不写入 Git

## 快速开始

### 1. 创建虚拟环境（推荐）

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

复制 `.env.example` 为 `.env`，然后填写你的 DeepSeek API Key：

```env
DEEPSEEK_API_KEY=你的API_KEY
```

不要把 `.env` 提交到 GitHub。

### 4. 运行

直接运行：

```bash
python main.py
```

程序会读取终端输入的剧本，并输出 JSON。

## DeepSeek API

默认 Base URL：`https://api.deepseek.com`

默认模型：`deepseek-chat`

## 下一步

- 增加剧本文件导入
- 增加镜头表 CSV/Excel 导出
- 增加人物/场景/道具资产提取
- 接入图片生成 API
- 接入视频生成 API
- 增加 Web UI
