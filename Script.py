import pandas as pd
import random
import numpy as np


def dataProcessing(file_storage):
    df = pd.read_csv(file_storage)
    df.dropna(inplace=True)  # remove empty rows
    return df


def analyzePatterns(df):
    """
    Analyze number frequency across all historical draws.
    Returns a sorted list of (number, frequency) pairs.
    """
    # Flatten all numeric columns
    all_numbers = df.select_dtypes(include=[np.number]).values.flatten()

    # Remove NaN and convert to integers
    all_numbers = [int(n) for n in all_numbers if not pd.isna(n)]

    # Count occurrences
    unique, counts = np.unique(all_numbers, return_counts=True)
    frequency = dict(zip(unique, counts))

    # Sort from most to least frequent
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq


def generatePredictions(frequency, n_boards=1, numbers_per_board=5):
    top_numbers = [num for num, _ in frequency[:5]]
    # ensure we don't sample more numbers than are available
    if numbers_per_board > len(top_numbers):
        numbers_per_board = len(top_numbers)
    predictions = [
        sorted(random.sample(top_numbers, numbers_per_board))
        for _ in range(n_boards)
    ]
    return predictions


def results(predictions, df):
    last_draw = df.iloc[-1].dropna().tolist()
    outcomes = []
    for board in predictions:
        matches = [num for num in board if num in last_draw]
        outcomes.append({
            "board": board,
            "matches": matches,
            "count": len(matches)
        })
    return {"last draw": last_draw, "result": outcomes}


if __name__ == "__main__":
    test_file = "Data/Lottery_Powerball_Winning_Numbers__Beginning_2010.csv"
    draws = dataProcessing(test_file)
    print("first 5 draws: ", draws[:5])
    print("total draws: ", len(draws))