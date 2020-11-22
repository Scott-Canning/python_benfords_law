# script to test Benford's law on data embedded within xlsx file
import random
import time
from openpyxl import load_workbook

# testing runtime
start = time.time()

# load in workbook
workbook = load_workbook(filename="benfords_tests.xlsx")
spreadsheet = workbook.active
first_column =  spreadsheet['A']
column_size = len(first_column)

array = [0 for i in range(10)]

# take values from each cell and "sort" into array, 0-9
count_data = 0;
for i in range(column_size):
    num = int(str(first_column[i].value)[:1]) # strips off leftmost integer
    array[num] += 1
    count_data += 1

# print array
index = 0
for i in array:
   print(index, ".", round(i/column_size * 100, 3), "%\n")
   index += 1


end = time.time()
delta = end - start

print("Data points:", count_data)
print("runtime", round(delta,3))



# testing benford's law on random number generator
#
#
'''
limit = 10000
array = [0 for i in range(10)]
num = 0

# create random numbers, count leftmost integer occurence
for i in range(limit):
    num = random.randrange(0, limit)
    num = int(str(num)[:1]) # strips off leftmost integer
    array[num] += 1

# print array
index = 0
for i in array:
   print(index, ".", round(i/limit * 100,3), "%\n")
   index += 1

'''
