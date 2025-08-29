#!/bin/bash

# Word转Markdown工具启动脚本

echo "🚀 启动 Word转Markdown 工具..."

# 检查是否存在虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📚 安装依赖包..."
pip install -q -r requirements.txt

# 创建上传目录
mkdir -p uploads

echo "✅ 启动完成！"
echo ""
echo "🌐 打开浏览器访问: http://localhost:8080"
echo ""
echo "使用 Ctrl+C 停止服务"
echo ""

# 启动应用
python backend/app.py