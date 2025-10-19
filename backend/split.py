import pandas as pd
from sklearn.model_selection import train_test_split
import yaml
with open("config.yaml", "r") as f: config = yaml.safe_load(f)
# load full dataset
df = pd.read_pickle(config["dataset"]["raw"])

# validate required columns
required_columns = ["title", "content", "label"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns: raise ValueError(f"Missing expected columns: {missing_columns}")

# stratified split 80:20
train_df, test_df = train_test_split(
    df,
    test_size=(1-config["training"]["test_size"]),
    stratify=df["label"]
)

# shuffle datasets
train_df = train_df.sample(frac=1).reset_index(drop=True)
test_df = test_df.sample(frac=1).reset_index(drop=True)

# save outputs as pickle files
train_df.to_pickle(config["dataset"]["train"])
test_df.to_pickle(config["dataset"]["test"])

if config["log"]: print(f"Training and testing datasets saved: {config["dataset"]["train"]}, {config["dataset"]["test"]}")