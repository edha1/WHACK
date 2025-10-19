from utils import clean_text, load_models
from models.accuracies import accuracies

import yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)

models = load_models()

def normalise(prediction, accuracy):
    return ((1 if prediction else -1) * accuracy + 1) / 2

def predict(content):
    confidence = 0
    text = f"{clean_text(content)}"
    for name, model in models.items():
        prediction = model.predict([text])[0]
        if config["log"]: print(f"{name} ({accuracies[name] * 100 :.2f}%): {"Real" if prediction else "Fake"}")
        confidence += normalise(prediction, accuracies[name])
    confidence /= len(models.items()) 
    if config["log"]: print(f"{confidence * 100 : .2f}%")
    return confidence

if __name__ == "__main__":
    content = """Blackstone says Wall Street is complacent about AI disruption
    
    CLAIM: A photo taken on Monday shows former President Donald Trump with no damage to his right ear, contrary to reports that it was injured in an attempted assassination on Saturday.

AP'S ASSESSMENT: False. The photo was taken on Sept. 17, 2022, at a rally in Youngstown, Ohio, for then-U.S. Senate candidate JD Vance. Trump appeared at the Republican National Convention Monday night with a large, white bandage on his right ear. Myriad photos show his ear bloodied after a shooter opened fire at his rally in Butler, Pennsylvania, over the weekend.

THE FACTS: Social media users are sharing the old photo as new, with some falsely presenting it as evidence that Trump was not injured by the gunfire."""
    predict(content)