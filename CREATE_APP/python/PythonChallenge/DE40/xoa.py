with open('SONGUYEN.INP','r') as file:
    n,k = int(file.readline().strip().split())
    s = n
    temp = n
    for i in range(k):
        temp = temp * 10
        s += temp
 
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
with open('SONGUYEN.OUT','w') as file:
    file.write(str(sum))