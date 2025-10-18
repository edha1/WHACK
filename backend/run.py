import joblib
import os
from utils import clean_text
from models.confidences import confidences


#output label mapping
def output_label(n):
    return "Fake News" if n == 0 else "Real News"

# Load all models
from models.models import models
model_names = models.keys()
models = {}
for name in model_names:
    model_path = os.path.join("models", f"{name}_model.joblib")
    if not os.path.exists(model_path):
        print(f"Warning: {model_path} not found. Skipping...")
    else:
        models[name] = joblib.load(model_path)

if not models:
    raise RuntimeError("No models loaded. Train models first with train.py")

def predict(title, content):
    x = 0
    text = f"{clean_text(title)}\n{clean_text(content)}"
    for name, model in models.items():
        pred = model.predict([text])[0]
        print(f"{name}: {output_label(pred)} | {confidences[name]}")
        x += (1 if pred else -1) * (confidences[name] / max(list(confidences.values())))
    x /= len(models.items()) 
    x = (x + 1) / 2
    print("Final", x)

if __name__ == "__main__":
    title_input = """Blackstone says Wall Street is complacent about AI disruption"""
    content_input = """CLAIM: A photo taken on Monday shows former President Donald Trump with no damage to his right ear, contrary to reports that it was injured in an attempted assassination on Saturday.

AP’S ASSESSMENT: False. The photo was taken on Sept. 17, 2022, at a rally in Youngstown, Ohio, for then-U.S. Senate candidate JD Vance. Trump appeared at the Republican National Convention Monday night with a large, white bandage on his right ear. Myriad photos show his ear bloodied after a shooter opened fire at his rally in Butler, Pennsylvania, over the weekend.

THE FACTS: Social media users are sharing the old photo as new, with some falsely presenting it as evidence that Trump was not injured by the gunfire.

“The top part of his ear grew back,” reads one X post from Monday night that had received approximately 40,000 likes and 13,200 shares as of Tuesday. “(Yes. This is from today)”

Another X post from Monday night states: “This image of Trump was taken today. There is absolutely nothing wrong with his ear, and it has zero damage, FROM A BULLET. Everything about Trump is a con or a grift.” It received approximately 26,000 likes and 8,600 shares.

But the photo was taken nearly two years ago.

It is from a Sept. 17, 2022, rally in Youngstown, Ohio, for Vance during his Senate campaign. The image appeared in multiple articles published around that time. Trump chose Vance, now a U.S. senator, as his running mate on Monday.

The version spreading online is cropped to show only Trump and is zoomed in to show the former president’s ear more clearly. In the original, Vance can be seen speaking at a podium while Trump stands behind him.

Trump appeared at the Republican National Convention in Milwaukee on Monday night with a large, white bandage on his right ear. Numerous photos from the aftermath of the shooting show the same ear bloodied.

Thomas Matthew Crooks, a 20-year-old nursing-home employee from suburban Pittsburgh, fired multiple shots at Trump with an AR-style rifle from a nearby roof at a rally for the Republican nominee on Saturday. He was killed by Secret Service personnel, officials said.

The attempted assassination left Trump and two other men wounded. Corey Comperatore, a 50-year-old fire chief, was killed while protecting his family. The FBI said it was investigating the attack as a potential act of domestic terrorism, but has not identified a clear ideological motive, The Associated Press has reported."""
    predict(title_input, content_input)