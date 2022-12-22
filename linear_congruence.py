def main():
    import sys
    def gcd(a, b):

        if b > a:
            a , b = b, a

        while True:

            q = int(a / b)
            r = a - (b*q)

            if r == 0:
                return int(b)

            else:
                a = (a-r)/q
                b = r

    def linear_cong(a,b,c):
            
        if gcd(a, b) > 1:

            if c % gcd(a, b) != 0:
                return "\nNO SOLUTIONS POSSIBLE!"

            g = gcd(a, b)
            a //= g
            b //= g
            c //= g

        if b == 1:
            return c//a

        else:
            a, b = b, a % b
            u = linear_cong(a,b,c)

            return (c - a*u)//b

    while True:

        message = str(input("This is a linear congruence calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the Linear congruence calculator!")
            break

        elif message.upper() == 'Y':

            try:
                a = int(input("\nENTER A: "))
                b = int(input("ENTER B: "))
                c = int(input("ENTER C: "))
                
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue
        
            k = linear_cong(a, b, c)
            print(k)
        
        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()