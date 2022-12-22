def main():
    def factor(x):
        y , i , factor_list = x , 2, []
            
        while i * i <= x:
            if x % i == 0:
                while x % i == 0:
                    x /= i
                    factor_list.append(i)

            i += 1
            
        if x > 1:
            factor_list.append(int(x))
        
        return factor_list

    while True:

        message = str(input("This is a Factorization Calculator. Press 'Y' to use it and 'N' to exit: "))

        if message.upper() == 'N':
            print("\nThanks for using the Factorization Calculator!")
            break

        elif message.upper() == 'Y':
            
            try:
                n = int(input("\nENTER N: "))
            except ValueError:
                print("\nInvalid Input! Please try again.")
                continue
            
            print(factor(n))

        else:
            print("\nInvalid Input! Please try again.")

if __name__ == "__main__":
    main()