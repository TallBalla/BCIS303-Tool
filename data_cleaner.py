'''
Cleaning Thematic Analysis Results
From Extracts 

'''
import pandas as pd
import re

class Data_Cleaner:
    path = r'C:\Users\willr\Downloads\Queensland Health System.xlsx'
       
    def get_data(self):
        '''Get's all uncleaned data from required column'''
        df = pd.read_excel (self.path, header=7, usecols='A:E')
        return df['Theme/Factor (typically data that helps answering your question)'].tolist()

    def clean_data(self):
        '''asfdasfd'''
        result = []
        for i in self.get_data():
            # print(i)
            for j in re.split('\([0-9]\)', str(i)):
                result.append(j)
        return result


# TODO remove empty nans and empty items, count list items     

if __name__ == '__main__':
    dc = Data_Cleaner()
    # print(dc.get_data())
    print(dc.clean_data())
    # dc.clean_data()
    # for i in dc.clean_data():
    #     print(i)