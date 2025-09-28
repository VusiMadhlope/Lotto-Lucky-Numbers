import pandas as pd
import random
import numpy as np


def dataProcessing(file_storage):
 df = pd.read_csv(file_storage)
 return df.values.tolist()




def analyzePatterns():
 pass




def generatePredictions():
 pass




def results():
 pass

if __name__ == "__main__":
 test_file = "Data/Lottery_Powerball_Winning_Numbers__Beginning_2010.csv"
 draws = dataProcessing(test_file)
 print("first 5 draws: ", draws[:5])
 print("total draws: ", len(draws))