import matplotlib.pyplot as plt
import numpy as np
import statistics
from statistics import variance
from math import sqrt

from data_preprocessing import Data_Preprocessing
class Data_analysis:

    def __init__(self,s1,s2,s3):
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3

    def outlier_extractor(self,list):

        q1,q3 = np.percentile(list,[25,75])
        iqr = q3 - q1
        lower_boundry = q1 - 1.5*iqr
        upper_boundry = q3 + 1.5*iqr
        return lower_boundry,upper_boundry

    def compare(self,firstdict,seconddict,thirddict,fourthdict,fifthdict,sixthdict):

        total_scores = {}
        for key in fifthdict:
            if key in fourthdict:
                if key in sixthdict:
                    total_scores[key] = fifthdict[key] + fourthdict[key] + sixthdict[key]
            elif key in thirddict:
                if key in seconddict:
                    total_scores[key] = fifthdict[key] + thirddict[key] + seconddict[key]
                elif key in firstdict:
                    total_scores[key] = fifthdict[key] + thirddict[key] + firstdict[key]

        return total_scores





    def normalising_data(self):

        Subject1_list = list(zip(self.__s1.ID,self.__s1.Subject1))
        Subject1_grades = [tup[1] for tup in Subject1_list]

        Subject3_list = list(zip(self.__s2.ID,self.__s2.Subject3))
        Subject3_grades = [tup[1] for tup in Subject3_list]

        Subject4_list = list(zip(self.__s1.ID,self.__s1.Subject4))
        Subject4_list.extend(list(zip(self.__s2.ID,self.__s2.Subject4)))
        Subject4_grades = [tup[1] for tup in Subject4_list]

        Subject5_list = list(zip(self.__s3.ID, self.__s3.Subject5))
        Subject5_grades = [tup[1] for tup in Subject5_list]

        Subject6_list = list(zip(self.__s1.ID,self.__s1.Subject6))
        Subject6_list.extend(list(zip(self.__s2.ID,self.__s2.Subject6)))
        Subject6_list.extend(list(zip(self.__s3.ID,self.__s3.Subject6)))
        Subject6_grades = [tup[1] for tup in Subject6_list]

        Subject7_list = list(zip(self.__s3.ID,self.__s3.Subject7))
        Subject7_grades = [tup[1] for tup in Subject7_list]

        grades = [Subject1_grades,Subject3_grades,Subject4_grades,Subject5_grades,Subject6_grades,Subject7_grades]
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111)
        ax.boxplot(grades)
        ax.set_xticklabels(['Subject1', 'Subject3','Subject4', 'Subject5','Subject6','Subject7'])
        ax.get_yaxis().tick_left()
        ax.get_xaxis().tick_bottom()
        plt.show()


        Subject3_lower,Subject3_upper = self.outlier_extractor(Subject3_grades)

        Subject3_dict = dict(Subject3_list)
        for key in list(Subject3_dict.keys()):
            if Subject3_dict[key] <= Subject3_lower or Subject3_dict[key] >= Subject3_upper:
                del Subject3_dict[key]

        normalised_Subject3_list = [(k,v) for k,v in Subject3_dict.items()]
        normalised_Subject3_grades = [tup[1] for tup in normalised_Subject3_list]

        Subject4_lower, Subject4_upper = self.outlier_extractor(Subject4_grades)
        Subject4_dict = dict(Subject4_list)
        for key in list(Subject4_dict.keys()):
            if Subject4_dict[key] <= Subject4_lower or Subject4_dict[key] >= Subject4_upper:
                del Subject4_dict[key]

        normalised_Subject4_list = [(k,v) for k,v in Subject4_dict.items()]
        normalised_Subject4_grades = [tup[1] for tup in normalised_Subject4_list]

        grades = [Subject1_grades, normalised_Subject3_grades, normalised_Subject4_grades, Subject5_grades, Subject6_grades, Subject7_grades]
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111)
        ax.boxplot(grades)
        ax.set_xticklabels(['Subject1', 'Subject3', 'Subject4', 'Subject5', 'Subject6', 'Subject7'])
        ax.get_yaxis().tick_left()
        ax.get_xaxis().tick_bottom()
        plt.show()

        return Subject1_list,normalised_Subject3_list,normalised_Subject4_list,Subject5_list,Subject6_list,Subject7_list



    def calculate_weighted_average(self, Subject1, Subject2, Subject3, Subject4, Subject5, Subject6):

        Subject1_grades = [tup[1] for tup in Subject1]
        count_s1 = len(Subject1_grades)
        mean_s1 = statistics.mean(Subject1_grades)
        sd_s1 = sqrt(variance(Subject1_grades))

        Subject2_grades = [tup[1] for tup in Subject2]
        count_s2 = len(Subject2_grades)
        mean_s2 = statistics.mean(Subject2_grades)
        sd_s2 = sqrt(variance(Subject2_grades))

        Subject3_grades = [tup[1] for tup in Subject3]
        count_s3 = len(Subject3_grades)
        mean_s3 = statistics.mean(Subject3_grades)
        sd_s3 = sqrt(variance(Subject3_grades))

        Subject4_grades = [tup[1] for tup in Subject4]
        count_s4 = len(Subject4_grades)
        mean_s4 = statistics.mean(Subject4_grades)
        sd_s4 = sqrt(variance(Subject4_grades))

        Subject5_grades = [tup[1] for tup in Subject5]
        count_s5 = len(Subject5_grades)
        mean_s5 = statistics.mean(Subject5_grades)
        sd_s5 = sqrt(variance(Subject5_grades))

        Subject6_grades = [tup[1] for tup in Subject6]
        count_s6 = len(Subject6_grades)
        mean_s6 = statistics.mean(Subject6_grades)
        sd_s6 = sqrt(variance(Subject6_grades))

        print([count_s1,count_s2,count_s3,count_s4,count_s5,count_s6])
        print("Mean of Subject1 is {:f}, Mean of Subject3 is {:f}, Mean of Subject4 is {:f}, Mean of Subject5 is {:f}, Mean of Subject6 is {:f}, Mean of Subject7 is {:f}".format(mean_s1,mean_s2,mean_s3,mean_s4,mean_s5,mean_s6))

        print(
            "Standard deviation of Subject1 is {:f}, Standard deviation of Subject3 is {:f}, Standard deviation of Subject4 is {:f}, Standard deviation of Subject5 is {:f}, Standard deviation of Subject6 is {:f}, Standard deviation of Subject7 is {:f}".format(
                sd_s1, sd_s2, sd_s3, sd_s4, sd_s5, sd_s6))

        #The Standard Deviation for all the subjects is relatively low, so we can use the mean as an indicator of the difficulty level of the exams and hence add appropriate weights to them.

        weight_s1 = 0.6
        weight_s2 = 0.3
        weight_s3 = 0.25
        weight_s4 = 0.15
        weight_s5 = 0.23
        weight_s6 = 0.2

        Subject1_dict = dict(Subject1)
        Subject2_dict = dict(Subject2)
        Subject3_dict = dict(Subject3)
        Subject4_dict = dict(Subject4)
        Subject5_dict = dict(Subject5)
        Subject6_dict = dict(Subject6)

        for key in Subject1_dict:
            Subject1_dict[key] = Subject1_dict[key]*weight_s1
        weighted_Subject1 = [(k,v) for k,v in Subject1_dict.items()]

        for key in Subject2_dict:
            Subject2_dict[key] = Subject2_dict[key]*weight_s2
        weighted_Subject2 = [(k, v) for k, v in Subject2_dict.items()]

        for key in Subject3_dict:
            Subject3_dict[key] = Subject3_dict[key]*weight_s3
        weighted_Subject3 = [(k, v) for k, v in Subject3_dict.items()]

        for key in Subject4_dict:
            Subject4_dict[key] = Subject4_dict[key]*weight_s4
        weighted_Subject4 = [(k, v) for k, v in Subject4_dict.items()]

        for key in Subject5_dict:
            Subject5_dict[key] = Subject5_dict[key]*weight_s5
        weighted_Subject5 = [(k, v) for k, v in Subject5_dict.items()]

        for key in Subject6_dict:
            Subject6_dict[key] = Subject6_dict[key]*weight_s6
        weighted_Subject6 = [(k, v) for k, v in Subject6_dict.items()]

        total_scores = self.compare(Subject1_dict,Subject2_dict,Subject3_dict,Subject4_dict,Subject5_dict,Subject6_dict)
        student_rankings = sorted(total_scores.items(), key=lambda x:x[1], reverse=True)

        for i in student_rankings:
            print(i[0], i[1])








