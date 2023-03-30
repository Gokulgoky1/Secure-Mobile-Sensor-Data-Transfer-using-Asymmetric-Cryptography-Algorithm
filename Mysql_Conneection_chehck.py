import pickle
import re
from flask_mysqldb import MySQL
from flask import Flask
import json
def Mysql_table_query(Tablename,index):
    list1=[]
    for i in range(len(index)):
        k=re.sub("\$|\)|\.|\(|\s|-","_",index[i])
        index[i]=k
    column=index.copy()
    index.append("@")
    string=" VARBINARY(10000),".join(index)
    string = string[:-2]
    sql="CREATE TABLE "+Tablename+"("+string+")"
    list1.append(sql)
    list1.append(column)
    return list1
def Mysql_column_query(list1):
    length=len(list1)
    list2=[]
    list3=[]
    for i in range(length):
        list2.append("%s")
    string2=",".join(list2)
    string2="VALUES"+'('+string2+')'
    string = ",".join(list1)
    string='('+string+')'
    list3.append(string)
    list3.append(string2)
    return list3