# Little - 小工具集合

一个包含多个实用小工具的项目，目前包含Word转Markdown工具。

## 功能特性

### 📝 Word转Markdown工具
- 支持 `.docx` 和 `.doc` 格式
- 保留文档结构（标题、段落、表格）
- 保留文本格式（粗体、斜体）
- 简洁美观的Web界面
- 支持拖拽上传
- 最大支持16MB文件

## 快速开始

### 环境要求
- Python 3.7+
- pip

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

**方法一：使用启动脚本（推荐）**
```bash
./start.sh
```

**方法二：手动启动**
```bash
# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动应用
python backend/app.py
```

然后在浏览器中访问 `http://localhost:8080`

## 项目结构

```
Little/
├── backend/
│   └── app.py              # Flask后端应用
├── frontend/               # 前端文件（预留）
├── static/                 # 静态资源
├── templates/              # 模板文件（预留）
├── uploads/                # 文件上传目录（自动创建）
├── requirements.txt        # Python依赖
├── config.py              # 配置文件
└── README.md              # 项目说明
```

## 使用说明

1. 启动应用后，打开浏览器访问 `http://localhost:8080`
2. 点击上传区域或拖拽Word文档到页面
3. 等待转换完成
4. 点击下载按钮获取Markdown文件

### 支持的功能
- ✅ 文档标题层级（H1-H6）
- ✅ 段落文本
- ✅ 粗体和斜体格式
- ✅ 表格转换
- ✅ 文件大小限制（16MB）
- ✅ 拖拽上传
- ✅ 实时进度显示

## 故障排除

### 端口被占用
如果遇到端口5000被占用的错误，可能是macOS的AirPlay接收器服务占用了端口。应用已配置使用8080端口避免此问题。

### 依赖安装失败
如果遇到"externally-managed-environment"错误，请确保使用虚拟环境：
```bash
python3 -m venv venv
source venv/bin/activate
```

### 转换失败
- 确保上传的是有效的Word文档（.docx或.doc格式）
- 检查文件大小是否超过16MB限制
- 尝试使用较新版本的Word保存文档

## 技术栈

- **后端**: Flask, python-docx, markdownify
- **前端**: HTML5, CSS3, JavaScript (Vanilla)
- **文件处理**: python-docx, werkzeug

## 开发计划

- [ ] 添加更多文档格式支持
- [ ] 增加批量转换功能
- [ ] 添加转换预览功能
- [ ] 集成更多小工具

## 许可证

MIT License