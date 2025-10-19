import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from utils import clean_text, load_models, format_input
import joblib, os, yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)

if config["log"]: import time

os.makedirs(config["model"]["dir"], exist_ok = True) # ensures that models directory exists

# load training data
df_train = pd.read_pickle(config["dataset"]["train"])

# clean data
df_train["title"] = df_train["title"].apply(clean_text)
df_train["content"] = df_train["content"].apply(clean_text)

# combine title + content
df_train["text"] = format_input(df_train["title"], df_train["content"])

x_train = df_train["text"] # network input
y_train = df_train["label"] # network output

# define models
from models.classifiers import models
for name, model in models.items():
    if config["log"]: start_time = time.time()
    
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=config["models"]["tfidf"]["max_features"], ngram_range=tuple(config["models"]["tfidf"]["ngram_range"]))),
        ("clf", model)
    ])
    pipeline.fit(x_train, y_train)
    
    if config["log"]: elapsed = time.time() - start_time
    
    joblib.dump(pipeline, f"models/{name}_model.joblib")
    if config["log"]: print(f"Saved {name} model to models/{name}_model.joblib | Training time: {elapsed:.2f} seconds")