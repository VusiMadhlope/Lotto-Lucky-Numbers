import pandas as pd

def load_history(csv_path):
    df = pd.read_csv(csv_path)
    return df

def save_user_numbers(user_boards, csv_path = "data/user_numbers.csv"):
    df = pd.DataFrame(user_boards)
    df.to_csv(csv_path, mode = 'a', header=False, index=False)