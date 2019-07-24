# 使用列表列出1000以内的所有质数。
prime = []
for i in range(2, 1000):
    for j in range(2, i):  # j从2遍历到i-1
        if i % j == 0:  # i能被j整除说明i是合数
            break  # 跳出本层循环，下一个i
    else:  # 所有j都不能整除i，i是质数
        prime.append(i)  # 加到质数列表
print(prime)
