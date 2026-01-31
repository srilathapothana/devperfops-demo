import requests
import time

url = "https://example.com/"

def test_response_time():
    start = time.time()
    response = requests.get(url)
    end = time.time()
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {end - start:.2f} seconds")

if __name__ == "__main__":
    for i in range(3):
        test_response_time()
