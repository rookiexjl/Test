# coding:utf-8
import xlwt
Myexcel = xlwt.Workbook()
table=Myexcel.add_sheet('Students')  
data = {  
		'1':[u'张三',150,120,100],  
		'2':[u'李四',90,99,95],  
		'3':[u'王五',60,66,68]  
}
for key in data.keys():  
	table.write(int(key)-1,0,int(key))  
	for i in range(0,len(data[key])):  
		table.write(int(key)-1,i+1,data[key][i])  
Myexcel.save('Students.xls')
