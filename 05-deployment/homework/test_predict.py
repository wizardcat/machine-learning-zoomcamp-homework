import requests

# URL of the Gunicorn server running inside the Docker container
url = "http://localhost:9696/predict"

# Sample client data provided in Question 5 / Question 6
client = {
    "job": "management",
    "marital": "single",
    "education": "tertiary",
    "default": "no",
    "balance": 1590,
    "housing": "single",
    "loan": "no",
    "contact": "cellular",
    "day": 12,
    "month": "nov",
    "duration": 240,
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown",
}

# Send HTTP POST request with JSON payload
response = requests.post(url, json=client)
result = response.json()

print("Full API Response:", result)

# Print specific prediction probability if returned as a dict key
if "probability" in result:
    print(f"Prediction Probability: {result['probability']:.3f}")
elif "get_credit_probability" in result:
    print(f"Probability: {result['get_credit_probability']:.3f}")