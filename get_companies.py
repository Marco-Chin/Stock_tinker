import numpy as np
import csv
import pandas

"""
sources of news headlines by day
   abc news 
"""

file_name = 'inputs/companies/fortune1000-final.csv'
#input format of file is date (YYYYMMDD), title

def get_n_companies(n=500):
    file_contents = []
    company_info = []

    i = 0
    with open(file_name, newline='') as csvfile:
        csv_reader_content = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader_content:
            breakpoint()
            file_contents.append(row)
            i+=1
            if(i>= n):
                break
    file_contents = np.array(file_contents)
    breakpoint()

get_n_companies()
