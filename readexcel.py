import xlrd
import xlwt
from xlwt import Workbook as WriteWorkBook
from googletrans import Translator
translator=Translator()
location =("E:\\notes\\Python\\document translation tool\\transtext2.xls")
testworkbook =xlrd.open_workbook(location,on_demand=True)
totalsheetcount= len(testworkbook.sheet_names())
print(totalsheetcount)
sheetinfo=[]
for index in range (totalsheetcount):
    testsheet=testworkbook.sheet_by_index(index)
    sheetinfo.append([index,testsheet.nrows,testsheet.ncols])
print(sheetinfo)
sheetdata=[]
sheettrans=[]
for index in sheetinfo:
    tempsheet=testworkbook.sheet_by_index(index[0])
    for rowindex in range (index[1]):
        for colindex in range (index[2]):
            tempdata=tempsheet.cell_value(rowindex,colindex)
            if tempdata =="":
                continue
            sheetdata.append([index[0],colindex,rowindex,tempdata])
            temptrans=translator.translate(str(tempdata),dest='en',src='ja')
            temptrans=temptrans.text
            sheettrans.append([index[0],colindex,rowindex,temptrans])
print(sheetdata)
print(sheettrans)
writeworkbook=WriteWorkBook()
for sheetindex in range(totalsheetcount):
    tempsheet=writeworkbook.add_sheet("sheet "+str(sheetindex))
    for textindex in sheettrans:
        if sheetindex == textindex[0]:
            tempsheet.write(textindex[2],textindex[1],textindex[3])
writeworkbook.save('E:\\notes\\Python\\document translation tool\\transtext3.xls')
        