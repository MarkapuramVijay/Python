###Comprehensions
print([i for i in range(1,11)])
print((i for i in range(1,11))) #tuple works as generator comprehensions, so it reflects generator object.
print(tuple(i for i in range(1,11)))
#Result
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#<generator object <genexpr> at 0x7c1fafd0c900>
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print({i:i**3 for i in range(1,6)})
#Result
#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

print({i:j for i,j in zip([1,2,3],['a','d','e'])})
#Result
#{1: 'a', 2: 'd', 3: 'e'}

#Comprehension
print(["Even" if i%2==0 else "Odd" for i in range(1,6)])
print([i for i in range(1,99) if i%2==0 if i%5==0])
print(["Even" for i in range(1,6) if i%2==0])
#Result
#['Odd', 'Even', 'Odd', 'Even', 'Odd']
#[10, 20, 30, 40, 50, 60, 70, 80, 90]
#['Even', 'Even']