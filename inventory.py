import pandas as pd
import openpyxl as op

# find the location fo the data
#data = "/mnt/c/Users/crazy/Downloads/W PHX INVENTORY.xlsx"
data1 = "W PHX INVENTORY_updated.xlsx"
#read the data
my_file = pd.read_excel(data1)
#print(my_file.head())

#activate the data
wb = op.load_workbook(data1)
sheet = wb.active

#manipulate the data
col = 4
rows = sheet.max_row

polaris = {
        "H050" : 1000120,
        "B012" : 1000394,
        "H244" : 1000288,
        "H089" : 1000322,
        "EKP02" : 1000770,
        "ETK02-2PL" : 1000736,
        "ECM01-CAN" : 1000732
        }
# todo list:

# crud operations
# tmp subbing of part
#interface for quick operations


# a cli for how man unit you did
units = 5 


for i in range(1, rows): #starting in the first row till max row
    for j in range(1, col + 1): # jump colums till max
        cell_obj = sheet.cell(row=i, column=j) # storing curr location

        if cell_obj.value in polaris:
            oh = sheet.cell(row=i,column=j+3) # after finding the name just to on hand
            sheet["E{}".format(i)] = oh.value - units # subtract units done from on hand

        print(cell_obj.value, end= " - ")
    print() # Add a newline at the end of the row
       

print(sheet["E3"].value)
#nothing

wb.save(data1)
