from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

seed = 42

models = {
    "LR": LogisticRegression(max_iter=1000, random_state=seed),
    "DT": DecisionTreeClassifier(random_state=seed),
    "GBC": GradientBoostingClassifier(n_estimators=200, random_state=seed),
    "RFC": RandomForestClassifier(n_estimators=200, random_state=seed),
    "SVC": LinearSVC(max_iter=1000, random_state=seed),
    "MNB": MultinomialNB()
}