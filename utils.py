import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)


def clean_data(df):
    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    return df