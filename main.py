from data_preprocessing import Data_Preprocessing
from data_analysis import Data_analysis

def main():

 file = Data_Preprocessing('Students data.csv')
 data = file.read_data()
 print(data.head())

 student_group1, student_group2, student_group3 = file.student_groups()

 print(student_group1)
 print(student_group2)
 print(student_group3)

 file_processed = Data_analysis(student_group1,student_group2,student_group3)
 Subject1, Subject3, Subject4, Subject5, Subject6, Subject7 = file_processed.normalising_data()

 file_processed.calculate_weighted_average(Subject1,Subject3,Subject4,Subject5,Subject6,Subject7)
if __name__ == "__main__":
 main()