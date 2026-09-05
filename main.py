from load import load_data
import pandas as pd

train, test, sample = load_data()

#exploratory data analysis
print(train.shape, test.shape)
print(train.head())

will_buy = train[train["Will_Buy_EV"] == "Yes"]
print(will_buy.head())