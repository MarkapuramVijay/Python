import sys
def table(n):
  for i in range(1,11):
    return f"{n} X {i} = {n*i}"
  print(sys.getsizeof(n))
op=table(5)
print("Size = ",sys.getsizeof(op))
print(op)

'''it prints sries of numbers by using list, return will be within function only not in for loop.
list=[]
def table(n):
  for i in range(1,11):
    list.append(f"{n} X {i} = {n*i}")
  print(sys.getsizeof(n))
  return list'''

for j in op:
  print(j, end="  ")
# it  prints any after  this fun, b/z of used "Return"
print(end="\n")
for j in op:
  print(j, end="  ")