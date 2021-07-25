s=[]
x=int(input('學生數量'))
for i in range(x):
    y=int(input('學生成績'))
    s.append(y)
print(max(s))