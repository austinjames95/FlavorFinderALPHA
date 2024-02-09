import requests
import json

API_URL2 = "https://api-inference.huggingface.co/models/nateraw/food"
headers = {"Authorization": "Bearer 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"}

def get_first_label(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        first_label = next(iter(data))
        # Check if the 'labels' key exists
        return first_label
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"

def test(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL2, headers=headers, data=data)
    return response.json()

def correctFormat(name):
    newName = name.replace("_", " ")
    return newName
    
