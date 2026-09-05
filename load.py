import os

from dotenv import load_dotenv

load_dotenv(override=True)

import kagglehub
import pandas as pd

COMPETITION = "playground-series-s6e9"


def load_data():
    path = kagglehub.competition_download(COMPETITION)

    train = pd.read_csv(os.path.join(path, "train.csv"))
    test = pd.read_csv(os.path.join(path, "test.csv"))
    sample = pd.read_csv(os.path.join(path, "sample_submission.csv"))

    return train, test, sample


if __name__ == "__main__":
    train, test, sample = load_data()
    print("train:", train.shape)
    print("test:", test.shape)
    print(train.head())