words = ''
with open('C:\\Users\\user\\Desktop\\Walden.txt','r') as f:
    all_list = f.readlines()
    for pargam in all_list:
        words = pargam+words
words_list = words.split()
words_type = []
for i in words_list:
    if i not in words_type:
        words_type.append(i)
words_dict = {}
for x in words_type:
    words_dict[x]= words_list.count(x)
new_dict = sorted(words_dict.items(),key=lambda x:x[1],reverse= True)
for word in new_dict:
    print('{0}  {1}'.format(word[0],word[1]))