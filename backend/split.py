import pandas as pd
from sklearn.model_selection import train_test_split

seed = 42 #deterministic testing
df = pd.read_csv("dataset/data.csv")

required_columns = ["title", "content", "label"]
missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing expected columns: {missing_cols}")

#stratified split 80:20
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=seed,
    stratify=df["label"]
)

#shuffle datasets
train_df = train_df.sample(frac=1, random_state=seed).reset_index(drop=True)
test_df = test_df.sample(frac=1, random_state=seed).reset_index(drop=True)

#save outputs
train_df.to_csv("dataset/train.csv", index=False)
test_df.to_csv("dataset/test.csv", index=False)

print("Training and testing datasets saved: train.csv, test.csv")