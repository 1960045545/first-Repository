len_max = 0                                          #1
text_list = []                                       #2
space = ''                                           #3
new_list = []                                        #4
file = open('F:\\pycharm项目\\demo.py','r')           #5
file_txt = file.readlines()                          #6
                                                     #7
file.close()                                         #8
text_row = len(file_txt)                             #9
for text in file_txt:                                #10
    text_str = len(text)                             #11
    if text_str > len_max:                           #12
        len_max = text_str                           #13
    if text[-1] == '\n':                             #14
        text_list.append(text[:-1])                  #15
    else:                                            #16
        text_list.append(text)                       #17
for new_text in text_list:                           #18
    while True:                                      #19
        if len(new_text)+len(space) == len_max:      #20
            new_list.append(new_text+space+'#')      #21
            space = ''                               #22
            break                                    #23
        else:                                        #24
            space += ' '                             #25
                                                     #26
demo_file = open('F:\\pycharm项目\\demo_new.py', 'w') #27
for i in range(1,text_row):                          #28
    demo_file.write(new_list[i-1]+str(i)+'\n')       #29
