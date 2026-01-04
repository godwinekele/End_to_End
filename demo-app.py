from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <head><title>Trading Bot Demo</title></head>
        <body style="font-family: Arial; padding: 50px; background: #1a1a1a; color: #fff;">
            <h1>🤖 Trading Bot CI/CD Pipeline Demo</h1>
            <p><strong>Status:</strong> <span style="color: #00ff00;">Running ✓</span></p>
            <p><strong>Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Version:</strong> 1.0.0</p>
            <hr>
            <p>This is a demo app to test your Jenkins → Docker Hub → ArgoCD → K8s pipeline</p>
            <p>Once this works, you can run your actual trading bot directly on Windows!</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)