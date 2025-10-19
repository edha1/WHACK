import yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)

import re, string
def clean_text(text):
    """normalise and clean text for model input"""
    text = str(text).lower()  # normalise case
    text = re.sub(r"https?://\S+|www\.\S+", "", text)  # remove URLs first to avoid splitting them
    text = re.sub(r"<.*?>+", "", text)  # strip HTML tags
    text = re.sub(r"\[.*?\]", "", text)  # remove bracketed content
    text = re.sub(r"\w*\d\w*", "", text)  # remove alphanumeric tokens containing digits
    text = re.sub("[%s]" % re.escape(string.punctuation), " ", text)  # replace punctuation with space
    text = re.sub(r"\W", " ", text)  # replace non-word characters with space (redundant but reinforces punctuation stripping)
    text = re.sub(r"\n", " ", text)  # normalise newlines
    text = re.sub(r"\s+", " ", text).strip()  # collapse multiple spaces and trim edges
    return text

import glob, os, joblib
def load_models():
    loaded = {}
    for path in glob.glob(f"{config['model']['dir']}/*{config['model']['format']}"):
        name = os.path.basename(path).replace(config['model']['format'], "")
        loaded[name] = joblib.load(path)
    return loaded

def format_input(title, content):
    return title + "\n" + content