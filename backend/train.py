import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib
from utils import clean_text
import os

#create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

#load training data
df_train = pd.read_csv("dataset/train.csv")

#clean text
df_train["title"] = df_train["title"].apply(clean_text)
df_train["content"] = df_train["content"].apply(clean_text)

#combine title + content
df_train["text"] = df_train["title"] + "\n" + df_train["content"]

X_train = df_train["text"]
y_train = df_train["label"]

#define models
from models.models import models

for name, model in models.items():
    pipeline = Pipeline([("tfidf", TfidfVectorizer(max_features=20000, ngram_range=(1,2))),
                         ("clf", model)])
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, f"models/{name}_model.joblib")
    print(f"Saved {name} model to models/{name}_model.joblib")
