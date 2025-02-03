import sys
def table(n):
  for i in range(1,11):
    yield f"{n} X {i} = {n*i}"
    print("sys.getsizeof(n) ",sys.getsizeof(n))
  print("size of n is - ",sys.getsizeof(n))
op=table(5)
print("Size = ",sys.getsizeof(op))
print(op)
for j in op:
  print(j)
print("=======")
# it is not print any after 1st fun, b/z of "Yield" generators.
for j in op:
  print(j)