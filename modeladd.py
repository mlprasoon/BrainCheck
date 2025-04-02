import requests

url = "https://github.com/mlprasoon/BrainCheck/releases/download/model/best_model.keras"
response = requests.get(url)
with open("model.h5", "wb") as f:
    f.write(response.content)
