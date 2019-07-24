import math  # 导入数学模块
prime = [2]  # 先记入2
for i in range(3, 1000, 2):  # 从3开始，只判断奇数
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        prime.append(i)
print(prime)