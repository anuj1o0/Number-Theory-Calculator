def main():
    def factors_once(x):

        i , factor_list = 2, []

        while i * i <= x:

            if x % i == 0:
                factor_list.append(i)

                while x % i == 0:
                    x = x / i

            i += 1
        
        if x > 1:
            factor_list.append(int(x))

        return factor_list

    def euler_tot(x):
        prod_1, prod_2 = 1, x

        for i in factors_once(x):
            prod_1 *= (i-1)
            prod_2 /= i

        return f"\nTotal number of positive integers below {x} that are co-prime to {x}: {int(prod_1 * prod_2)}"

    while True:

        message = str(input("This is a Euler Totient Function Calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using Euler Totient Function Calculator!")
            break

        elif message.upper() == 'Y':

            try:
                x = int(input("\nENTER X: "))
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue

            k = euler_tot(x)
            print(k)

        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()