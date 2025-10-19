from utils import clean_text, load_models
from models.accuracies import accuracies

import yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)

models = load_models()

def normalise(prediction, accuracy, scale):
    return ((1 if prediction else -1) * accuracy / scale + 1) / 2

def predict(title, content):
    confidence = 0
    text = f"{clean_text(title)}\n{clean_text(content)}"
    for name, model in models.items():
        prediction = model.predict([text])[0]
        if config["log"]: print(f"{name} ({accuracies[name] * 100 :.2f}%): {"Real" if prediction else "Fake"}")
        confidence += normalise(prediction, accuracies[name], max(accuracies.values()))
    confidence /= len(models.items()) 
    if config["log"]: print(f"{confidence * 100 : .2f}%")
    return confidence