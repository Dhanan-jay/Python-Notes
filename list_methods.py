# list are mutable :- matlab kabhi bhi change kar sakhte hai .

# methods of list .

a = [1,8,5,9,3,12]
print(a)

a.append(4)         # we can add any value in list but last mai hii.
print("append",a)

# a.insert(2,"Dhanan")# we can add any value in list bich mai bhi.
a.insert(2,100)
print("insert",a)

a.sort()    # sort() se order wise set ho jata hai. 
print("sort",a)

b = [2,9,4,6,7,3]

c = ["apple" , "mango" , "banana" , "guava"]

b.pop(2)       # pop() se hum kisi bhi index ke value ko delete kar sakhte hai.
print("pop",b)

b.clear()       # clear() se pure list ko clear kar sakhte hai.
print("clear",b)

c.reverse()     # reverse() se pure list ko reverse kar sakhte hai.
print("reverse",c)


print(c.count("mango"))
# count() se hum pata kar sakhte hai ki vo value ush list mai kitne baar hai.

print(c.index("mango"))
# index() se hum pata kar sakhte hai ki vo value ki index kya hai list mai.
