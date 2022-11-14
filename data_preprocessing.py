import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

class Data_Preprocessing:

    def __init__(self,filename):
        self.__file = filename

    def read_data(self):
        data = pd.read_csv(self.__file)
        data = data.drop(['class','gender','race','GPA','from1','from2','from3','from4','y'],axis=1)
        data.columns = ['ID','Subject1','Subject2','Subject3','Subject4','Subject5','Subject6','Subject7']

        # print(data.head().to_string())  # Checking all the remaining column names
        return data

    def student_groups(self):

        data = self.read_data()
        s1 = data.drop(['Subject2','Subject3','Subject5','Subject7'],axis=1)
        s1 = s1.drop(range(36,105))
        # print(s1)

        s2 = data.drop(['Subject1', 'Subject2', 'Subject5','Subject7'], axis=1)
        s2 = s2.drop(range(0, 36))
        s2 = s2.drop(range(90,105))
        # print(s2)

        s3 = data.drop(['Subject3','Subject2','Subject1','Subject4'],axis = 1)
        s3 = s3.drop(range(0,90))
        # print(s3)

        return s1,s2,s3




