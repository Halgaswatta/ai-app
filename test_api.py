import requests
import json

def test_api():
    base_url = "http://localhost:8000"
    
    print("Testing API endpoint...")
    
    test_data = {
        "name": "John Doe",
        "message": "Hello from the API test!",
        "data": {
            "user_id": 123,
            "preferences": ["api", "python", "fastapi"]
        }
    }
    
    try:
        response = requests.post(f"{base_url}/process", json=test_data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Response:")
            print(json.dumps(result, indent=2))
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Make sure the API server is running on localhost:8000")
        print("Run: python main.py")

if __name__ == "__main__":
    test_api()