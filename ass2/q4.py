num=int(input())

while(num):
    print(num)
    result=[[0 for x in range(num)] for y in range(num)]
    for i in range (num):
        line = input().split()
        line=[int(index) for index in line]
        for index in line:
            result[i][index]=1
        print(*result[i],"")
    num=int(input())
print(num)
