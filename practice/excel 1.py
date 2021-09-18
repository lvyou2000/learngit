import xlwt
# f=open("excel 1.txt","r+")
# lines=f.readlines()
# retdata=[]
# for line in lines:
#     items=line.strip().split(',')
#     retdata.append(items[i] for i in range(1,4))
#
# f.close()


workbook=xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet('sheet1')#创建工作表
worksheet.write(0,0,'avltree')#写入数据 行 列 内容
worksheet.write(0,1,'rbtree')
worksheet.write(0,2,'bsttree')
worksheet.write(0,3,'b-tree')
f=open("excel 1.txt")
lines=f.readlines()
data=[]
for line in lines:
    item=line.strip().split(',')
    for i in range(0,4):
        data.append(item[i])
m=0
for i in range(0,25):
    for j in range(0,4):
        worksheet.write(i+1,j,data[m])
        m=m+1
workbook.save('excel 1.xls')