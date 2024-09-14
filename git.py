from flask import Flask, request, jsonify, redirect
import logging
import os

app = Flask(__name__)

# 设置日志记录
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('visitor_log.txt')
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
console_handler.setLevel(logging.INFO)

logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(file_handler)
logging.getLogger().addHandler(console_handler)

def get_client_ip():
    if 'X-Forwarded-For' in request.headers:
        ip_address = request.headers['X-Forwarded-For'].split(',')[0].strip()
    else:
        ip_address = request.remote_addr
    return ip_address

@app.route('/')
def log_visitor():
    try:
        # 获取访问者的 IP 和 User-Agent
        visitor_ip = get_client_ip()
        user_agent = request.headers.get('User-Agent', 'Unknown')

        # 日志记录
        logging.info(f"IP: {visitor_ip}, User-Agent: {user_agent}")

        # 重定向到目标网站
        return redirect('https://www.tesla.cn/cybertruck', code=302)

    except Exception as e:
        logging.error(f"Error logging visitor: {e}")
        return jsonify({"status": "error", "message": "An error occurred."}), 500

if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    # 启动 Flask 应用并使用 SSL 证书
    app.run(host=host, port=port, ssl_context=('crt file path url', 'key file path url'))
