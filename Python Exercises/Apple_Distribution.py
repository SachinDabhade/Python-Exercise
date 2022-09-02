# *************************** Apple distribution ***************************

if __name__ == '__main__':
    while True:
        try:
            # Getting user input
            no_apple = int(input("\nEnter the number of apples: "))
            minimum = int(input("Enter the minimum number in range: "))
            maximum = int(input("Enter the maximum number in range: "))
        # Exception handeling
        except ValueError:
            print("Enter Integers only...!")
            exit()
        else:
            # Checking the range is valid or not
            if minimum >= maximum:
                print("This is not a range...!")
            for item in range(minimum, maximum + 1):
                if no_apple % item == 0: # If apple is divisible by item and remainder is 0 then it will print result
                    print(f"{item} is divisor of {no_apple}")
                else:
                    print(f"{item} is not divisor of {no_apple}")
        continue
