import random
a = []
for i in range(100):
    a.append(random.randint(1, 100))  # 生成一个随机数字的列表
a.sort()  # 对列表进行排序
print(a)
i = 0
while i < len(a):
    if a.count(a[i]) > 1:  # 删除重复项
        a.remove(a[i])  # 也可以用a.pop(i)
    else:
        i += 1  # 相当于i = i + 1
print(a)
