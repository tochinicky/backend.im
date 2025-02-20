# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Hello World endpoint
# @app.route('/')
# def hello_world():
#     return "Hello, World!"

# # Endpoint to receive notifications
# @app.route('/notify', methods=['POST'])
# def notify():
#     data = request.json
#     print("Received notification:", data)
#     return jsonify({"status": "success"})

# # Endpoint to handle test results
# @app.route('/test-results', methods=['POST'])
# def test_results():
#     data = request.json
#     print("Received test results:", data)
#     return jsonify({"status": "success"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Notification(BaseModel):
    message: str

class TestResult(BaseModel):
    result: str

@app.get("/")
def hello_world():
     return {"message": "Hello, World!"} 

@app.post("/notify")
def notify(data: Notification):
    print(f"Received notification: {data.model_dump()}")
    return {"status": "success", "message": data.model_dump()}

@app.post("/test-results")
def test_results(data: TestResult):
    print(f"Received test results: {data.model_dump()}")
    return {"status": "success", "message": data.model_dump()}