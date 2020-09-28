list = eval(input('输入一个列表'))
list_2 = []
for i in list:
    if list.count(i) == 1:
        list_2.append(i)
print(list_2)