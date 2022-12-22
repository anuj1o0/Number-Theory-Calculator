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

        g = gcd(a, b)

        if g > 1:

            a //= g
            b //= g
            c //= g
            
        if b == 1:

            return c//a

        else:

            a, b = b, a % b
            u = linear_cong(a,b,c)
            return (c - a*(u))//b

    def CRT(a, m):

        a = [int(i) for i in a]
        m = [int(i) for i in m]
        n = []
        y = []
        X = 0

        if len(a) != len(m):
            return "\nINVALID INPUT"
            
        for i in range(1, len(m)):
            for j in range(i):
                if gcd(m[i], m[j]) != 1:
                    return "\nMODULI ARE NOT CO-PRIME, PLEASE TRY AGAIN!"
                    

        for i in range(len(a)):
            if a[i] > m[i]:
                a[i] = a[i] % m[i]

        N = 1

        for i in m:
            N *= i

        for i in m:
            n.append(N//i)

        for i in range(len(m)):

            x = linear_cong(n[i], m[i], 1)

            if x < 0:
                x = x + m[i]

            y.append(x)

        for i in range(len(a)):

            X += n[i]*y[i]*a[i]

        return (X % N)

    while True:

        message = str(input("This is a Chinese Remainder Theorem calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the CRT calculator!")
            break

        elif message.upper() == 'Y':

            try:
                a = list(map(int, input("\nENTER THE RESIDUES: ").split(" ")))
                m = list(map(int, input("ENTER CO-PRIME MODULI: ").split(" ")))
                
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue

            k = CRT(a, m)
            print(k)
        
        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()