import random
'''
str = 'abcdef'
list1 =["ab","cd","ef"]

for i in range(5):
    #1到10產生五個亂數
    print(random.randint(1,10),end = ",")
    #0,2,4,6,8
    print(random.randrange(0,12,2),end = ",")
#0到1之間的浮點亂數
print(random.random())
#範圍內浮點數亂數
print(random.uniform(3,10))
#字串，隨機取得一字元。串列，隨機取得一個元素。
print(random.choice("abcdefg"), end = ",")
print(random.choice([1,2,3,4,5,6,7]))
#可指定取得的數量字元
print(random.sample("abcdefg",3))
print(random.sample([1,2,3,4,5,6,7,8],3))
'''
list1 = [1,2,3,4]
for i in range(2):
    print(random.choice(list1),end = ' ')
