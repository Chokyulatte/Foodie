sentence="Zeven Zottegemse zotten zullen zes zomerse zondagen zwemmen zonder zwembroek."
myList=sentence.split()
print(myList)
length=len(myList)
print(length)

def reverse(s):
    return s[::-1]

print(reverse('help'))

l1=[[1,2],[2,5],[3,6]]
print(l1 [1])
l1 [1]

print("1".isdigit())
print(False)

def do(n):
    global counter
    #counter = 0
    for i in (1,2,'bla'):
        counter += n
    return counter

counter = 1
print(do(2))

def foo1(x=1):
    return x*2;
foo = (1,2,3,4)

print(foo1())

a=[(),[],'hello world'.split()]
print(len(a))

l = [1,2,3,4,5,6,7]
print(l[:-6])

count = 0
for i in range(len(l)):
    count=0
    for item in l[:-i]:
        #print('bla')
        count+=1
    #print(count)

l = [8,12,3]
x=l.sort()
y=l[:]
l.extend([1])
print(x)
print(y==l)
print(y)
print(l)

x=2
r=1
print((x,r))

s='ja'
print(s)
