class game:
    def game_start(num,work):
        list = []  # 设立空列表，获取人数
        for i in range(1,num+1):
            list.append(i) #人数统计
        while len(list)>2: #判断是否要继续循环
            for x in range(work-1):
                remove = list.pop(0)
                list.append(remove) #删除并添加至末尾
                if x == work-2:
                    list.pop(0) #删除步长的元素
            if work ==1:
                list = []
        print(list)

game.game_start(28,2)