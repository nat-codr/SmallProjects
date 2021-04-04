def checkPrimeNumber(number):
    isPrime = False
    divider = 2
    if number == divider or number == 1:
      return True
    while number % divider != 0:
        divider = divider + 1
        print(divider)
        if number == divider:
            isPrime = True

    return isPrime

def test(number):
    print(str(checkPrimeNumber(number)) + " " + str(number))

# test(4)
# test(57)
# test(567)
# test(7)
# test(2)
# test(1)
# test(0)
# test(21317)
test(100000015333)
