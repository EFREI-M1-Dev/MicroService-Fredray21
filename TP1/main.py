import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()
baseUrl = "https://jsonplaceholder.typicode.com/"

@app.get("/posts")
def get_posts(limit: int = 5):
    url = baseUrl + f"posts?_limit={limit}"
    response = requests.get(url)
    return response.json()

@app.get("/users")
def get_users(limit: int = 5):
    url = baseUrl + f"users?_limit={limit}"
    response = requests.get(url)
    return response.json()

@app.post("/create_post")
def create_post(body: str, title: str):
    url = baseUrl + "posts"
    data = {
        "body": body,
        "title": title
    }
    response = requests.post(url, data)
    return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
