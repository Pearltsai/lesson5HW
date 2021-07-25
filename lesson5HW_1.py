r=0
s=[]
x=int(input('學生數量'))
for i in range(x):
    y=int(input('學生成績'))
    r=r+y
    s.append(y)
    
print('平均是',r/x)
