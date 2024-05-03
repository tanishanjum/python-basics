a=1234535647403
if(a&1==1):
    print("even")
else:
    print("odd")

a=int(input('enter the nor'))
b=int(input('enter the nor'))
c=int(input('enter the nor'))
if b>a:
    print("b is greater than a")
elif c>a:
    print("c is greater than a ")
elif a>b:
    print("a is greater than b ")
elif a>c:
    print("a is greater than c")
elif c>a:
    print("c is greater than a")
elif c>b:
    print("c is greater than b")
else:
    print("a b  and c are equal")
print(a)
print(b)
print(c)

x=int(input("enter the no"))
if(x%2==0 and x%3==0):
    print('divisible by 2 and 3')
else:
    print('not divisible by 2 and 3')

a=int(input('enter the number'))
if (a>0):
    print('positive')
elif (a<0):
    print('negative')
else:
    print('zero')

w=int(input("weight of watermelon"))
if(w%2!=0 or w==2):
    print("no")
else:
    x=w/2
    if(x%2==0):
        print("x1=",x, "and" "x2=",x)
    else:
        print("x1=",x-1, "and" "x2=",x+1)

n=int(input('enter the value of nor'))
value=n*(n+1)/2
print(value)

n=int(input('enter the nor'))
sum=0
for i in range (1,n+1):
    sum += i
print('sum of first',n,'natural numbers:',sum)