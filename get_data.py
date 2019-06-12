import pandas as pd

# Change url based on dataset of choice
url = "https://assets.datacamp.com/production/" \
      "repositories/401/datasets/09378cc53faec573bcb802dce03b01318108a880/gapminder_tidy.csv"

# read url into pandas DataFrame

df = pd.read_csv(url, sep=",")

# Save dataframe locally for later use

df.to_csv('data/gapminder.csv')

