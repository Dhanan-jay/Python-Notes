# list are mutable :- matlab kabhi bhi change kar sakhte hai .

# a = [0,1,2,3,4,5,6,7,8,9,10]

a = [x for x in range(10)]      
# hame ish  syntax se uper jaisa manually likhna nahi pada

print(a)

a = [x for x in range(50) if x % 2 == 0] # we apply if condition also

print(a)       # only even no. can print

# another example :- 

b = [3 ** i for i in range(10)]     # 3 ka power nikalta hai 

print(b)
