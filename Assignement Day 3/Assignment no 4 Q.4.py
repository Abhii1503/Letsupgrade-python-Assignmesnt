number = input('Please Enter a number:')
i=2
toggle = 0

while i < number:
    if number%i == 0:
        toggle = 1
        print ("Your number is NOT a prime number !");
    i =  i + 1
if toggle == 0:
    print ("Your number is prime number !");
