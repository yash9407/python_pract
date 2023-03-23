

'''
#  1st program -------

print("Hello!")
name = input("enter your name : ")
print("Welcome",name)
age = int(input("enter your age : "))
a = input("what is your favourite dish?? ")
print(a,"amazing!!!! Indeed it is delicious")
print('a perfect taste for',age,'years old person')



#MINI_PROJECT bASIC CALCULATOR

a = int(input("enter a number : "))
b = int(input("enter another number : "))
ask = input("what operation do you want?? ")
if ask=='sum':
    print(a+b)
elif a>b and ask=='sub':
    print(a-b)
elif b>a and ask=='sub':
    print(b-a)
elif (ask=='mul'):
    print(a*b)
elif (ask=='div'):
    print(a/b)
else: 
    print(a%b)
'''


#RANGE

# The last number i.e. suppose 
#  number = range(5)
# here the numbers that will be printed would be 0,1,2,3,4 and '5' WILL NOT BE DISPLAYED


# LOOPS
 
# WHILE loop
 # question 1

'''i = 1
while i<=10:
    print(i)
    print(i*i)
    i = i+1
'''
# question 2

'''i = 10
while i<=300:
    print(i)
    i = i+10
'''
# question 3


'''i = 105
while i >=7:
    print(i)
    i = i - 7
'''

# question 4

'''num = 2
sum = 0
while num <=20:
    sum = sum + num
    num = num+2
    print(sum)
'''

# question 5

'''
num = int(input("enter a number : "))
a = 0
while a<10:
    a = a + 1
    print(num*a)

'''

# question 6

a = int(input("enter a number : "))
b = int(input("enter another number : "))

# if a<b:
#     while a<b:
#         if a%2 ==0:
#             print(a)
#         a = a+1
# else:
#     while(a>b):
#         if b%2==0:
#             print(b)
#         b = b+1

start = min(a,b)
end = max(a,b)

while(start <= end):
    if start%2==0:
        print(start)
    start+=1