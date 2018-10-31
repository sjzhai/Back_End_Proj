"""
1.
"""

import random, string

class Default:
    def __init__(self):
        #储存生成的随机用户名
        self.name_li = []
        #储存用户名
        # self.name_de = []

    def default_name(self):
        """
        输入型: None
        输出型: str
        生成随机用户名，例：RX8372
        """
        name = ""
        let_part = ""
        num_part = ""
        list_len = len(self.name_li)
        # 生成大写字母
        for i in range(2):
            let = random.choice(string.ascii_uppercase)
            name += let
            let_part += str(ord(let))
        # 生成数字
        for i in range(4):
            num = random.choice(string.digits)
            name += num
            num_part += num
        # 连接字母十进制部分和数字部分
        concat = int(let_part + num_part)
        if list_len > 1:
            self.qsort(self.name_li, 0, list_len-1)
        if not self.repetition(self.name_li, concat, 0, list_len-1):
            self.name_li.append(concat)
        else:
            print("---repetition---")
            self.default_name()
        return name

    def qsort(self, li, left, right):
        """
        输入型: list, int, int
        输出型: list
        排序列表供查找
        """
        def partition(li, left, right):
            """
            输入型: list, int, int
            输出型: int
            以基值为标准，比较并交换值
            """
            i = left
            j = right
            base = li[j]
            while(i < j):
                while(i < j and li[i] <= base):
                    i += 1
                li[j] = li[i]
                while(i < j and li[j] >= base):
                    j -= 1
                li[i] = li[j]
            li[j] = base
            return j

        i = left
        j = right
        stack = []
        stack.append(i)
        stack.append(j)
        while stack:
            j = stack.pop()
            i = stack.pop()
            bar = partition(li, i, j)
            if bar-1 > i:
                stack.append(i)
                stack.append(bar-1)
            if bar+1 < j:
                stack.append(bar+1)
                stack.append(j)
        return li

    def repetition(self, li, num, start, end):
        """
        输入型: list, int, int, int
        输出型: boolean
        查找名字是否在列表中重复出现
        """
        if start <= end:
            bar = (end + start) // 2
            if num < li[bar]:
                return self.repetition(li, num, start, bar-1)
            elif num > li[bar]:
                return self.repetition(li, num, bar+1, end)
            elif num == li[bar]:
                return True
        return False

if __name__ == '__main__':
    De = Default()
    for i in range(10000):
        name_gen = De.default_name()
        print(name_gen)
