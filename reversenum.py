#reverseNumbers
a=[]
b=[1,3,6,8,2,5]
for i in range(len(b)):
  a.append(b.pop())

print(a)
#Result
#[5, 2, 8, 6, 3, 1]