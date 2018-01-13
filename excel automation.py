# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:56:43 2018

@author: Shivam
"""

import openpyxl
import os

os.chdir('')

wb=openpyxl.load_workbook('test.xlsx')

sheet=wb.get_sheet_by_name('test1')


data=[]
for i in range(1,5):
    value=(sheet.cell(row=i,column=3).value)
    data.append(value)

print(data)

text_file=open(os.path.join('C:\\Users\\Shivam\\Documents',"file.txt"), 'a')   
text_file.write(str(data))
text_file.close()

  
