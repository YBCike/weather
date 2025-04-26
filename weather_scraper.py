import requests

def fetch_weather(location_id, api_key):
    """
    爬取和风天气的实时天气数据
    :param location_id: 城市代码（如北京：101010100）
    :param api_key: 和风天气的 API Key
    :return: 天气数据字典
    """
    url = f"https://nb4ewr2pw5.re.qweatherapi.com/v7/weather/now?location=101010100&key=7eabf2eb885649188338d9e9a8edb490"
    try:
        response = requests.get(url)
        
        # 检查 HTTP 响应状态码
        if response.status_code != 200:
            print(f"Failed to fetch weather data. HTTP Status: {response.status_code}")
            return {"error": f"HTTP Status: {response.status_code}"}
        
        # 解析 JSON 响应
        data = response.json()
        
        # 检查 API 返回的错误码
        if data.get("code") != "200":
            print(f"API returned error code: {data.get('code')}")
            return {"error": f"API Error Code: {data.get('code')}"}
        
        # 返回天气数据
        return {
            "city": location_id,
            "temperature": data["now"]["temp"],
            "condition": data["now"]["text"],
            "humidity": data["now"]["humidity"],
            "wind": data["now"]["windScale"],
            "update_time": data["updateTime"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching weather data: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    # 替换为你的 API Key 和城市代码
    API_KEY = "7eabf2eb885649188338d9e9a8edb490"  # 替换为有效的 API Key
    LOCATION_ID = "101010100"  # 北京的城市代码
    
    # 调试爬取天气数据
    weather_data = fetch_weather(LOCATION_ID, API_KEY)
    print(weather_data)