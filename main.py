from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# 저장할 쿠키 파일 경로
COOKIE_FILE_PATH = "gemini_cookies.json"

@app.route('/')
def home():
    return "Gemini Cookie Server is Running!"

@app.route('/upload_cookies', methods=['POST'])
def upload_cookies():
    data = request.get_json()
    
    if not data or 'cookies' not in data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400
    
    cookies = data['cookies']
    
    # 쿠키 파일 저장
    with open(COOKIE_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(cookies, f, indent=4)
        
    return jsonify({"status": "success", "message": "Cookies saved successfully"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)