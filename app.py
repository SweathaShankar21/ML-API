from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

data = load_iris()
model = RandomForestClassifier()
model.fit(data.data, data.target)

@app.get("/")
def home():
    return {"message": "Tiny ML API is running v2", "status": "ok"}

@app.post("/predict")
def predict(features: list[float]):
    if len(features) != 4:
        return {"error": "You must provide exactly 4 numbers for features"}
    pred = model.predict([features])
    return {"prediction": int(pred[0])}
