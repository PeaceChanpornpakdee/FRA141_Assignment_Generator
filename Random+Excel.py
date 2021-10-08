from itertools import combinations
import random
import pandas as pd
import openpyxl

def Combi(have, pick):
    haveList = list(range(1,have+1))
    returnList = list(combinations(haveList,pick))
    return returnList

def Shuffle80(inputList):
    random.shuffle(inputList)
    return inputList[:80]

def ExcelStart(path):
    df = pd.DataFrame()
    df.to_excel(path, sheet_name='Start', index=False, header=False)

def ExcelAppend(path, sheetName, dataList):
    book = openpyxl.load_workbook(path)
    writer = pd.ExcelWriter(path, engine='openpyxl')
    writer.book = book
    df = pd.DataFrame(dataList,index=None, columns=None)
    df.to_excel(writer, sheet_name=sheetName, index=False, header=False)
    writer.save()


FRA141_Path = '/Users/Peace/Desktop/Student_Assignments.xlsx'

'''Used ONCE when start new File'''
# ExcelStart(FRA141_Path)

'''Adding new Sheet'''
AssignmentList = Combi(10,3)
AssignmentList = Shuffle80(AssignmentList)
ExcelAppend(FRA141_Path, "List II", AssignmentList)
