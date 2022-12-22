def main():

    def gcd(a, b):

        x = a
        y = b

        if b > a:
            a , b = b, a

        while True:

            q = int(a / b)
            r = a - (b*q)

            if r == 0:
                return int(b)
                break
            else:
                a = (a-r)/q
                b = r

    while True:

        message = str(input("This is a GCD Calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the GCD calculator!")
            break

        elif message.upper() == 'Y':

            try:
                a = int(input("\nENTER A: "))
                b = int(input("ENTER B: "))

            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue

            k = gcd(a, b)
            print(k)

        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()