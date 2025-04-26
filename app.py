from flask import Flask, jsonify
from flask_cors import CORS
from weather_scraper import fetch_weather

app = Flask(__name__)
CORS(app)  # 启用 CORS 支持，允许前端跨域请求

# 替换为你的和风天气 API Key 和城市代码
API_KEY = "7eabf2eb885649188338d9e9a8edb490"
LOCATION_ID = "101010100"

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """
    提供实时天气数据的 API
    """
    weather_data = fetch_weather(LOCATION_ID, API_KEY)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)