import requests

url = "https://github.com/mlprasoon/BrainCheck/releases/download/model/best_model.keras"
response = requests.get(url)
with open("best_model.keras", "wb") as f:
    f.write(response.content)
