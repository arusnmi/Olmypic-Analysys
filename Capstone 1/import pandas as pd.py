import pandas as pd

df = pd.read_parquet("hf://datasets/foodvisor-nyu/labeled-food-ingredients/data/train-00000-of-00001.parquet")


df.to_csv('Excel.csv')