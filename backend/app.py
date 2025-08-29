import os
import tempfile
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from docx import Document
import markdownify
import zipfile
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 配置
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'docx', 'doc'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def docx_to_markdown(docx_path):
    """将docx文件转换为markdown格式"""
    try:
        # 读取docx文件
        doc = Document(docx_path)
        
        markdown_content = []
        
        # 按顺序处理文档中的所有元素
        for element in doc.element.body:
            if element.tag.endswith('p'):  # 段落
                paragraph = None
                for p in doc.paragraphs:
                    if p._element == element:
                        paragraph = p
                        break
                
                if paragraph and paragraph.text.strip():
                    md_text = convert_paragraph_to_markdown(paragraph)
                    if md_text:
                        markdown_content.append(md_text)
            
            elif element.tag.endswith('tbl'):  # 表格
                table = None
                for t in doc.tables:
                    if t._element == element:
                        table = t
                        break
                
                if table:
                    table_md = convert_table_to_markdown(table)
                    if table_md:
                        markdown_content.extend(table_md)
                        markdown_content.append('')  # 表格后添加空行
        
        # 清理空行并返回
        result = []
        for line in markdown_content:
            if line.strip() or (result and result[-1].strip()):
                result.append(line)
        
        return '\n'.join(result)
        
    except Exception as e:
        raise Exception(f"转换过程中出现错误: {str(e)}")


def convert_paragraph_to_markdown(paragraph):
    """将段落转换为markdown格式"""
    if not paragraph.text.strip():
        return ''
    
    # 检查是否为标题
    style_name = paragraph.style.name.lower()
    text = paragraph.text.strip()
    
    # 更准确的标题识别
    heading_patterns = {
        'heading 1': '#',
        'heading1': '#',
        '标题 1': '#',
        'heading 2': '##',
        'heading2': '##', 
        '标题 2': '##',
        'heading 3': '###',
        'heading3': '###',
        '标题 3': '###',
        'heading 4': '####',
        'heading4': '####',
        '标题 4': '####',
        'heading 5': '#####',
        'heading5': '#####',
        '标题 5': '#####',
        'heading 6': '######',
        'heading6': '######',
        '标题 6': '######'
    }
    
    # 检查是否匹配标题样式
    for pattern, prefix in heading_patterns.items():
        if pattern in style_name:
            return f'{prefix} {text}'
    
    # 对于没有使用标题样式的文档，尝试根据格式和内容判断标题
    if is_likely_heading(paragraph):
        heading_level = detect_heading_level(paragraph)
        prefix = '#' * heading_level
        return f'{prefix} {text}'
    
    # 如果不是标题，处理文本格式
    return format_text_runs(paragraph)


def is_likely_heading(paragraph):
    """判断段落是否可能是标题"""
    text = paragraph.text.strip()
    
    # 空文本不是标题
    if not text:
        return False
    
    # 排除明显的文档元数据
    metadata_keywords = [
        '资料编码', '文档版本', '发布日期', '版权所有', 'VOS3000', 'V2.1.9.07', 'Web 接口说明书',
        '昆石网络技术有限公司', '05', '2022-10-19'
    ]
    
    if any(keyword in text for keyword in metadata_keywords):
        return False
    
    # 检查是否整个段落都是粗体
    if paragraph.runs:
        all_bold = True
        has_text = False
        for run in paragraph.runs:
            if run.text.strip():  # 忽略空白run
                has_text = True
                if not run.bold:
                    all_bold = False
                    break
        
        if not has_text:
            return False
            
        # 如果整个段落都是粗体，可能是标题
        if all_bold:
            # 进一步判断：标题通常较短且不包含句号
            if len(text) < 100 and not text.endswith('。') and not text.endswith('.'):
                # 排除一些明显不是标题的内容
                exclude_keywords = ['参数名称', '必须', '类型', '描述信息', 'retCode', 'exception']
                if not any(keyword in text for keyword in exclude_keywords):
                    return True
    
    return False


def detect_heading_level(paragraph):
    """检测标题级别"""
    text = paragraph.text.strip()
    
    # 基于文本内容和位置的简单启发式规则
    
    # 一级标题：主要章节
    if any(keyword in text for keyword in ['概述', '配置', '功能操作']):
        return 1
    
    # 检查是否是章节号 (如 "1 概述", "2 配置")
    if len(text.split()) >= 2:
        first_part = text.split()[0]
        if first_part.isdigit() and int(first_part) <= 10:  # 主要章节编号
            return 1
    
    # 二级标题：小节号 (如 "2.1", "3.2")
    if '.' in text and len(text) <= 10:
        parts = text.split('.')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return 2
    
    # 三级标题：更细的分节 (如 "2.1.1")
    if text.count('.') == 2:
        parts = text.split('.')
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            return 3
    
    # 基于关键词判断标题级别
    level2_keywords = ['目录', '商标声明', '注意']
    if any(keyword in text for keyword in level2_keywords):
        return 2
    
    # 默认二级标题
    return 2


def format_text_runs(paragraph):
    """处理段落中的文本格式（粗体、斜体等）"""
    if not paragraph.runs:
        return paragraph.text.strip()
    
    formatted_parts = []
    
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
            
        # 应用格式
        if run.bold and run.italic:
            text = f'***{text}***'
        elif run.bold:
            text = f'**{text}**'
        elif run.italic:
            text = f'*{text}*'
        
        formatted_parts.append(text)
    
    return ''.join(formatted_parts).strip()


def convert_table_to_markdown(table):
    """将表格转换为markdown格式"""
    if not table.rows:
        return []
    
    table_md = []
    
    for i, row in enumerate(table.rows):
        row_data = []
        for cell in row.cells:
            # 处理单元格内的文本，移除换行符
            cell_text = cell.text.strip().replace('\n', ' ').replace('\r', ' ')
            # 转义管道符号以避免表格格式冲突
            cell_text = cell_text.replace('|', '\\|')
            row_data.append(cell_text)
        
        # 生成表格行
        table_row = '| ' + ' | '.join(row_data) + ' |'
        table_md.append(table_row)
        
        # 如果是第一行（表头），添加分隔符
        if i == 0:
            separator = '|' + ' --- |' * len(row_data)
            table_md.append(separator)
    
    return table_md


@app.route('/')
def index():
    """主页"""
    return '''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Word转Markdown工具</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                max-width: 600px;
                width: 100%;
                text-align: center;
            }
            
            h1 {
                color: #333;
                margin-bottom: 30px;
                font-size: 2.5em;
                background: linear-gradient(135deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .upload-area {
                border: 3px dashed #667eea;
                border-radius: 15px;
                padding: 40px 20px;
                margin: 30px 0;
                transition: all 0.3s ease;
                cursor: pointer;
                background: #f8f9ff;
            }
            
            .upload-area:hover {
                border-color: #764ba2;
                background: #f0f3ff;
                transform: translateY(-2px);
            }
            
            .upload-area.dragover {
                border-color: #764ba2;
                background: #e8ecff;
                transform: scale(1.02);
            }
            
            .upload-icon {
                font-size: 3em;
                color: #667eea;
                margin-bottom: 15px;
            }
            
            .upload-text {
                color: #666;
                font-size: 1.1em;
                margin-bottom: 10px;
            }
            
            .file-input {
                display: none;
            }
            
            .btn {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 25px;
                font-size: 1em;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 10px;
                text-decoration: none;
                display: inline-block;
            }
            
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
            }
            
            .btn:disabled {
                opacity: 0.6;
                cursor: not-allowed;
            }
            
            .progress {
                margin: 20px 0;
                display: none;
            }
            
            .progress-bar {
                width: 100%;
                height: 8px;
                background: #f0f0f0;
                border-radius: 4px;
                overflow: hidden;
            }
            
            .progress-fill {
                height: 100%;
                background: linear-gradient(135deg, #667eea, #764ba2);
                width: 0%;
                transition: width 0.3s ease;
            }
            
            .result {
                margin-top: 20px;
                padding: 20px;
                border-radius: 10px;
                display: none;
            }
            
            .result.success {
                background: #d4edda;
                border: 1px solid #c3e6cb;
                color: #155724;
            }
            
            .result.error {
                background: #f8d7da;
                border: 1px solid #f5c6cb;
                color: #721c24;
            }
            
            @media (max-width: 600px) {
                .container {
                    margin: 10px;
                    padding: 30px 20px;
                }
                
                h1 {
                    font-size: 2em;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📝 Word转Markdown</h1>
            <p style="color: #666; margin-bottom: 30px;">轻松将Word文档转换为Markdown格式</p>
            
            <div class="upload-area" id="uploadArea">
                <div class="upload-icon">📁</div>
                <div class="upload-text">点击或拖拽Word文档到这里</div>
                <div style="color: #999; font-size: 0.9em;">支持 .docx 和 .doc 格式，最大16MB</div>
                <input type="file" id="fileInput" class="file-input" accept=".docx,.doc" />
            </div>
            
            <div class="progress" id="progress">
                <div class="progress-bar">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <div style="margin-top: 10px; color: #666;">转换中...</div>
            </div>
            
            <div class="result" id="result">
                <div id="resultMessage"></div>
                <div id="downloadLink" style="margin-top: 15px;"></div>
            </div>
        </div>

        <script>
            const uploadArea = document.getElementById('uploadArea');
            const fileInput = document.getElementById('fileInput');
            const progress = document.getElementById('progress');
            const progressFill = document.getElementById('progressFill');
            const result = document.getElementById('result');
            const resultMessage = document.getElementById('resultMessage');
            const downloadLink = document.getElementById('downloadLink');

            // 点击上传区域触发文件选择
            uploadArea.addEventListener('click', () => {
                fileInput.click();
            });

            // 拖拽功能
            uploadArea.addEventListener('dragover', (e) => {
                e.preventDefault();
                uploadArea.classList.add('dragover');
            });

            uploadArea.addEventListener('dragleave', () => {
                uploadArea.classList.remove('dragover');
            });

            uploadArea.addEventListener('drop', (e) => {
                e.preventDefault();
                uploadArea.classList.remove('dragover');
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    handleFile(files[0]);
                }
            });

            // 文件选择处理
            fileInput.addEventListener('change', (e) => {
                if (e.target.files.length > 0) {
                    handleFile(e.target.files[0]);
                }
            });

            function handleFile(file) {
                // 检查文件类型
                if (!file.name.endsWith('.docx') && !file.name.endsWith('.doc')) {
                    showResult('error', '请选择Word文档文件 (.docx 或 .doc)');
                    return;
                }

                // 检查文件大小 (16MB)
                if (file.size > 16 * 1024 * 1024) {
                    showResult('error', '文件大小超过16MB限制');
                    return;
                }

                uploadFile(file);
            }

            function uploadFile(file) {
                const formData = new FormData();
                formData.append('file', file);

                // 显示进度条
                progress.style.display = 'block';
                result.style.display = 'none';
                progressFill.style.width = '0%';

                // 模拟进度
                let progressValue = 0;
                const progressInterval = setInterval(() => {
                    progressValue += Math.random() * 20;
                    if (progressValue > 90) progressValue = 90;
                    progressFill.style.width = progressValue + '%';
                }, 100);

                fetch('/convert', {
                    method: 'POST',
                    body: formData
                })
                .then(response => {
                    clearInterval(progressInterval);
                    progressFill.style.width = '100%';
                    
                    if (response.ok) {
                        return response.blob();
                    } else {
                        return response.json().then(err => Promise.reject(err));
                    }
                })
                .then(blob => {
                    // 成功，提供下载链接
                    const url = window.URL.createObjectURL(blob);
                    const filename = file.name.replace(/\\.(docx?|doc)$/i, '.md');
                    
                    showResult('success', '转换成功！');
                    downloadLink.innerHTML = `<a href="${url}" download="${filename}" class="btn">📥 下载Markdown文件</a>`;
                    
                    setTimeout(() => {
                        progress.style.display = 'none';
                    }, 500);
                })
                .catch(error => {
                    clearInterval(progressInterval);
                    progress.style.display = 'none';
                    showResult('error', error.message || '转换失败，请重试');
                });
            }

            function showResult(type, message) {
                result.className = `result ${type}`;
                result.style.display = 'block';
                resultMessage.textContent = message;
                if (type === 'error') {
                    downloadLink.innerHTML = '';
                }
            }
        </script>
    </body>
    </html>
    '''


@app.route('/convert', methods=['POST'])
def convert_word_to_markdown():
    """转换Word文档为Markdown"""
    try:
        # 检查是否有文件上传
        if 'file' not in request.files:
            return jsonify({'error': '没有选择文件'}), 400
        
        file = request.files['file']
        
        # 检查文件名
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 检查文件类型
        if not allowed_file(file.filename):
            return jsonify({'error': '不支持的文件格式，请选择Word文档(.docx或.doc)'}), 400
        
        # 保存上传的文件
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        try:
            # 转换为Markdown
            markdown_content = docx_to_markdown(filepath)
            
            # 创建临时文件用于下载
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as temp_file:
                temp_file.write(markdown_content)
                temp_filepath = temp_file.name
            
            # 生成下载文件名
            base_name = os.path.splitext(filename)[0]
            download_filename = f"{base_name}.md"
            
            # 清理上传的文件
            os.remove(filepath)
            
            # 返回文件用于下载
            return send_file(
                temp_filepath,
                as_attachment=True,
                download_name=download_filename,
                mimetype='text/markdown'
            )
            
        except Exception as e:
            # 清理上传的文件
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': str(e)}), 500
            
    except Exception as e:
        return jsonify({'error': f'处理请求时出现错误: {str(e)}'}), 500


@app.route('/health')
def health_check():
    """健康检查接口"""
    return jsonify({'status': 'ok', 'message': 'Word转Markdown工具运行正常'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)