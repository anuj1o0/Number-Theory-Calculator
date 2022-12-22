def main():
    import functools

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

    def diophantine(n, N):

        print("\n")
        n = [int(i) for i in n]
        
        n = list(set(n))

        soln = []

        g = functools.reduce(gcd, n)

        if N % g != 0:
            print("This Diophantine Equation has no possible solutions!")
            quit()
        
        for i in range((len(n) - 1), -1, -1):

            g = n[0]
            
            for j in range(i):
                g = gcd(g, n[j])

            x = linear_cong(g, n[i], N)

            if n[i] != n[0]:

                y = (N - g*x)//n[i]
                N = x*g
                
            else:
                y = N//n[i]
            
            soln.append(y)

        return n, soln[::-1]

    while True:

        message = str(input("This is a Linear Diophantine Equation Solver. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the LDE Solver!")
            break

        elif message.upper() == 'Y':

            try:
                n = list(map(int , input("\nENTER THE INTEGER COEFFICIENTS: ").split(" ")))
                N = int(input("ENTER THE INTEGER FOR WHICH TO SOLVE THE LDE: "))

            except ValueError:
                
                print("\nInvalid Input! Please try again.")
                continue

            print(diophantine(n, N))
                
        else:
            print("\nInvalid Input! Please try again.")
        
if __name__ == "__main__":
    main()



