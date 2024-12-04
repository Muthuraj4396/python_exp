number = 56784
length = len(str(number))
for i in range(4,-1,-1):
    print("i=",i)
    divisor = 10**(i)
    digit = number//divisor
    print(digit)
    number %= divisor