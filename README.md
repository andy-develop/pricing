以下是一个基于你项目信息生成的较为详细的 README.md 内容，突出了项目的重点部分：

```markdown
# pricing

## 项目概述
这是一个基于 Flask 框架构建的 Web 应用，主要用于分析画作信息并估算艺术品价格。通过用户上传画作图像和输入文本描述，应用可以对画作进行详细分析，处理缺失信息，搜索艺术家知名度，并最终估算出艺术品的价格。

## 主要功能

### 1. 用户输入处理
用户可以通过表单上传画作图像，并输入相关的文本描述，这些信息将作为后续分析的基础。

### 2. 画作分析
- 利用大语言模型（LLM）对上传的画作和用户描述进行深入分析，提取关键信息，包括：
  - 艺术家姓名或风格
  - 作品内容/主题
  - 使用的技法
  - 尺寸分类（小、中、大）

### 3. 缺失值处理
- 系统会检查分析结果中是否存在缺失或未知的值。
- 如果存在缺失值，会提示用户进行填充，提供预定义的选项供用户选择。

### 4. 艺术家知名度搜索
根据分析结果中的艺术家姓名，搜索该艺术家在百度和小红书等平台的知名度，为价格估算提供参考。

### 5. 价格估算
- 综合分析结果和艺术家知名度，调用 LLM 进行艺术品价格的估算。
- 给出价格估算结果及对应的价格区间，并详细解释估算背后的理由。

## 文件结构

### 主要文件和文件夹
- `pricing_agent`：项目的主要代码文件夹，包含以下重要文件和子文件夹：
  - `analysis_utils.py`：包含 `analyze_input` 函数，负责处理图像和文本输入，调用 LLM 进行分析并解析结果。
  - `llm_utils.py`：与大语言模型交互的相关函数，如创建 OpenAI 客户端和不同模型的分析函数。
  - `main.py`：Flask 应用的主文件，定义了路由和核心业务逻辑，包括文件上传处理、调用其他功能函数等。
  - `price_utils.py`：包含 `estimate_price` 函数，用于根据分析结果估算艺术品价格。
  - `requirements.txt`：列出项目所需的 Python 依赖包及其版本。
  - `templates`：存放 Flask 应用的 HTML 模板文件，用于页面渲染。
  - `uploads`：用于存储用户上传的图像文件。

## 运行项目

### 步骤
1. 克隆仓库到本地：
   ```sh
   git clone <仓库地址>
   cd pricing
   ```
2. 创建并激活虚拟环境：
   - 使用 `venv` 创建虚拟环境：
     ```sh
     python -m venv venv
     source venv/bin/activate  # 对于 Linux 和 macOS
     .\venv\Scripts\activate  # 对于 Windows
     ```
3. 安装项目所需的依赖包：
   ```sh
   pip install -r pricing/pricing_agent/requirements.txt
   ```
4. 运行 `main.py` 文件：
   ```sh
   python pricing/pricing_agent/main.py
   ```
5. 打开浏览器，访问 `http://127.0.0.1:5000` 即可使用该应用。

## 依赖包
项目使用了以下主要依赖包：
- Flask：用于构建 Web 应用。
- Pillow：用于处理图像。
- OpenAI：用于与大语言模型交互。
- requests：用于发送 HTTP 请求。
- gunicorn：用于部署 Flask 应用。
- beautifulsoup4：用于 HTML 和 XML 解析。
- python-dotenv：用于加载环境变量。
- flask-wtf：用于处理 Web 表单。
- flask-sqlalchemy：用于数据库操作。
```
