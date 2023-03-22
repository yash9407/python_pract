

'''
#  1st program -------

print("Hello!")
name = input("enter your name : ")
print("Welcome",name)
age = int(input("enter your age : "))
a = input("what is your favourite dish?? ")
print(a,"amazing!!!! Indeed it is delicious")
print('a perfect taste for',age,'years old person')

'''


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
