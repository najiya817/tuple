tuplee=(1,2,3,4,5)
print(tuplee[0])
print(tuplee[1])
print(tuplee[2])
print(tuplee[3])
print(tuplee[4])
print(len(tuplee))
print(tuplee[0])
print(tuplee[0:1])
print(tuplee[0:2])
print(tuplee[0:3])
print(tuplee[0:4])
print(tuplee[0:5])

tuplee=(0,1,2,3,4,5,6,7,8,9)
len=len(tuplee)
print(len)
print(tuplee[:len])
print(tuplee[3:6])
print(tuplee[6:9])
print(tuplee.count(5))
print(tuplee.index(1))



fruits=("apple","banana","cherry")
a,b,c=fruits
print(a)
print(b)
print(c)

fruits=("apple","banana","cherry","guava","mango","pineapple")
a,b,*c=fruits
print(a)
print(b)
print(c)

ttuple=(1,2,3,4)
ttuple=list(ttuple)
ttuple.append(5)
ttuple=tuple(ttuple)
print(ttuple)