marks=[34,54,66,44,33]
marks.append(99)
print(marks)

marks.insert(2, 100)
print(marks)

# list comprihansion
a=5
table=[] 
for i in range(1,11):
    table.append(a*i)
print(table)

tables=[6*i for i in range(1,11)]
print(tables)