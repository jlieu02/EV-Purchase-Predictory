from dotenv import load_dotenv
load_dotenv()

import os
import kagglehub
import pandas as pd

path = kagglehub.competition_download('playground-series-s6e9')
print("Path:", path)
print("Files:", os.listdir(path))

train = pd.read_csv(os.path.join(path, "train.csv"))
print(train.shape)
print(train.head())