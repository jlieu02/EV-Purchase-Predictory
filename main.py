from load import load_data

train, test, sample = load_data()
print(train.shape, test.shape)
print(train.head())