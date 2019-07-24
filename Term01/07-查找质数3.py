import math
prime = [2]
for i in range(3, 1000, 2):
    s = math.sqrt(i)  # 把i的平方根保存，减少后面的计算次数
    for j in prime:  # 只用之前保存的质数作因数
        if j > s:  # 如果j大于i的平方根
            continue  # 跳过本次循环后面的语句，执行else
        if i % j == 0:
            break  # 跳出本层循环，下一个i，不执行else
    else:
        prime.append(i)
print(prime)
