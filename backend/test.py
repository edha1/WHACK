import pandas as pd
from sklearn.metrics import accuracy_score
from utils import clean_text, load_models, format_input
import joblib, yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)

# load test data
df_test = pd.read_pickle(config["dataset"]["test"])

# clean text
df_test["title"] = df_test["title"].apply(clean_text)
df_test["content"] = df_test["content"].apply(clean_text)

# combine title + content
df_test["text"] = format_input(df_test["title"], df_test["content"])

x_test = df_test["text"]
y_test = df_test["label"]

# Load all saved models
models, accuracies = load_models(), {}
for name, model in models.items(): 
    try:
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies[name] = accuracy
        if config["log"]: print(f"{name}: {accuracy * 100:.2f}%")
    except Exception:
        accuracies[name] = 0.0 # if there is any error in testing; set accuracy to zero
        if config["log"]: print(f"{name}: ERROR")

# write to accuracy file
filepath = config["model"]["dir"] + "/" + config["model"]["accuracies"]
with open(filepath, "w", encoding="utf-8") as f:
    f.write("accuracies = {\n")
    for k, v in accuracies.items():
        f.write(f'    "{k}": {v},\n')
    f.write("}\n")

if config["log"]: print(f"\nSaved accuracy scores to {filepath}")