import numpy as np
import csv

"""
sources of news headlines by day
   abc news 
"""

file_name = 'inputs/news/abcnews_data.text.csv'
#input format of file is date (YYYYMMDD), title

def get_abc_news():
    file_contents = []
    with open(file_name, newline='') as csvfile:
        csv_reader_content = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csv_reader_content:
            file_contents.append(row)
    file_contents = np.array(file_contents)
    breakpoint()

get_abc_news()
