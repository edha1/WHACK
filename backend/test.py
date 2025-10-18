import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from utils import clean_text
import glob
import os

# load test data
df_test = pd.read_csv("dataset/test.csv")

# clean text
df_test["title"] = df_test["title"].apply(clean_text)
df_test["content"] = df_test["content"].apply(clean_text)

# combine title + content
df_test["text"] = df_test["title"] + "\n" + df_test["content"]

X_test = df_test["text"]
y_test = df_test["label"]

# load all saved models
model_files = glob.glob("models/*_model.joblib")

confidences = {}

for model_path in model_files:
    model_name = model_path.replace("\\", "/").split("/")[-1].replace("_model.joblib", "")
    model = joblib.load(model_path)

    try:
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        confidences[model_name] = acc
        print(f"{model_name}: {round(acc * 100, 2):.2f}%")
    except Exception:
        confidences[model_name] = 0.0
        print(f"{model_name}: ERROR")

# === Write to models/confidences.py ===
conf_path = "models/confidences.py"
with open(conf_path, "w", encoding="utf-8") as f:
    f.write("confidences = {\n")
    for k, v in confidences.items():
        f.write(f'    "{k}": {v},\n')
    f.write("}\n")

print("\n✅ Saved confidence scores to models/confidences.py")
