'''
Cleaning Thematic Analysis Results
From Extracts 

'''
import pandas as pd

class Data_Cleaner:
    path = r'E:\ARA\2022\Semester 1\BCIS303 - IT Governance\Assignment 1\BCIS303_Thematic_Analysis_V3_BrydenJoe.xlsx'
       
    def get_data(self):
        '''Get's all uncleaned data from required column'''
        df = pd.read_excel (self.path, header=7, usecols='A:E')
        return df['Theme/Factor (typically data that helps answering your question)'].tolist()

    def clean_data(self):
        '''asfdasfd'''
        list = self.get_data()
        invalid_char = "1234567890()"
        for i in list:
            for char in invalid_char:
                i = i.replace(char, ',')

        return list


       

if __name__ == '__main__':
    dc = Data_Cleaner()
    # print(dc.get_data())
    print(dc.clean_data())
