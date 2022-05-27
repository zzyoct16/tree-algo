num=int(input())

while(num):
    print(num)
    for i in range(num):
        new_list=[]
        output=input().split()
        for i in range(num):
            if output[i]=="1":
                new_list.append(i)
        print(*new_list,"")
    num=int(input())
print(num)
