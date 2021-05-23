import pandas as pd

def load_data(path):
    train = pd.read_csv(path + '/train.csv')
    test = pd.read_csv(path + '/test.csv')
    return train, test
    
def train_load_data():
    df_train = pd.read_csv(train_path)
    return df_train

def test_load_data():
    df = pd.read_csv(test_path)
    return df_test
