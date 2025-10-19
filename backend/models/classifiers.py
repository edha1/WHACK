# core vectoriser and pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# linear models for text
from sklearn.linear_model import LogisticRegression, SGDClassifier, PassiveAggressiveClassifier, RidgeClassifier

# naive-bayes variants
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, ComplementNB

# tree-based models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    BaggingClassifier
)

# SVM linear
from sklearn.svm import LinearSVC

import yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)

models = {
    "LR": LogisticRegression(**config["models"]["LR"]),
    "MNB": MultinomialNB(**config["models"]["MNB"]),
}
"""
    "LR": LogisticRegression(**config["models"]["LR"]),
    "SVC": LinearSVC(**config["models"]["SVC"]),
    "SGD": SGDClassifier(**config["models"]["SGD"]),
    "PA": PassiveAggressiveClassifier(**config["models"]["PA"]),
    "RC": RidgeClassifier(**config["models"]["RC"]),

    "MNB": MultinomialNB(**config["models"]["MNB"]),
    "BNB": BernoulliNB(**config["models"]["BNB"]),
    "CNB": ComplementNB(**config["models"]["CNB"]),

    "DT": DecisionTreeClassifier(**config["models"]["DT"]),
    "RFC": RandomForestClassifier(**config["models"]["RFC"]),
    "ETC": ExtraTreesClassifier(**config["models"]["ETC"]),
    "GBC": GradientBoostingClassifier(**config["models"]["GBC"]),
    "ABC": AdaBoostClassifier(**config["models"]["ABC"]),
    "BAG": BaggingClassifier(**config["models"]["BAG"]),
}
"""