len_max = 0
text_list = []
space = ''
new_list = []
file = open('F:\\pycharm项目\\demo.py','r')
file_txt = file.readlines()

file.close()
text_row = len(file_txt)
for text in file_txt:
    text_str = len(text)
    if text_str > len_max:
        len_max = text_str
    if text[-1] == '\n':
        text_list.append(text[:-1])
    else:
        text_list.append(text)
for new_text in text_list:
    while True:
        if len(new_text)+len(space) == len_max:
            new_list.append(new_text+space+'#')
            space = ''
            break
        else:
            space += ' '

demo_file = open('F:\\pycharm项目\\demo_new.py', 'w')
for i in range(1,text_row):
    demo_file.write(new_list[i-1]+str(i)+'\n')
demo_file.close()