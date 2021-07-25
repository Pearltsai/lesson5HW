s=[]
x=int(input('學生數量'))
for j in range(x):
    y=input(('學生成績'))
    s.append(y)

m=s[0]
for i in range(1,x):
    if m<s[i]:
        m=s[i]
print(m)