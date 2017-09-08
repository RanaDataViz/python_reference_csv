import csv
import re

with open("search_file.csv") as source, open("list.csv") as module_names, open("Final_File.csv","w",newline="") as result:
    reader=csv.reader(source)
    module=csv.reader(module_names)
    writer=csv.writer(result)
    for s in module_names:
        print(s)
        k=s[1]
        l=s[2]
        print(k)
        print(l)