#Q.1 print 10 integer values from user
for x in range(10):
    x=int(input("enter ten integer values"))

    print("entered value",x)
    
#Q.2 Write an infinte loop.
i=1
while i<10:
    print("Hello world")
    
print(i)

#Q.3 create a list integer by user input
l=[]
for i in range (0,5):
    num=int(input("enter the list"))
    l.append(num)
print(l)
square=[]
for num in l:
    sq=num*num
    square.append(sq)
print(square)

#Q.4 list containing value int,float,string type and seprate these value
l=[1,2.2,'abcd',12,5.9,'efgh']
for i in l :
    print("the entered value is",i,str(type(i)))
    
#Q.5 even odd number between 1 to 101
even=[]
odd=[]
for i in range (1,101) :
    if i%2==0 :
     even.append(i)
    else :
     odd.append(i)
print(even)
print(odd)

#Q.6 print structure
i=1
while i<=4 :
    print("*"*i)
    i=i+1

#Q.7 user defined dictionary
d={'rajat':217,'pagal':98,'hai':76}
for key in d.keys() :
    print(key,d[key])

#Q. 8 list operation
l=[7,9,6,5]
num= int(input("enter any value which you wantin list"))
for i in l :
 if i==num:
     print("value found")
     l.remove(i)

print(l)
     


    
