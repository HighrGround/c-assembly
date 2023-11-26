hours = int(input("enter your hours"))
rate = int(input("enter you rate of pay"))
pay = hours * rate 
print(f"your pay is {pay}")


number = 10 
if (number == 5):
    print("the number is equal to 5")
else:
    print("the number is equal to 5")


print(x ==5) #equal to
print(x != 5) #not equal to
print(x > 5) #greater than
print(x < 5) #less than
print(x >= 5) #greater than or equal to
print(x <= 5) #less than ort equal to


year = 2000
if(year <1901):
    print("the non living generation")
elif(year >= 1901 and year < 1924):
    print("the greatest generation")
elif(year >= 1925 and year < 1945):
    print("the silent generation")
elif(year >= 1946 and year < 1964):
    print("the baby boomer generation")
elif(year >= 1965 and year < 1979):
    print("generation x")
elif(year >= 1980 and year < 1994):
    print("milleanials")
elif(year >= 1995 and year < 2012):
    print("generation z")
else:
    print("gen alpha")

day = 3
match(day):
    case 0:
        print("sunday")
    case 1:
        print("monday")
    case 1:
        print("tuesday")
    case 1:
        print("wednesday")
    case 1: 
        print("thursday")
    case 1:
        print("friday")
    case 1:
        print("saturday")
    case _:
        print("unknown day")



number1 = int(input("enter your number"))
number2 = 5
divid = number1 % number2
if(divid == 0):
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")