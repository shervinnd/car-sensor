def complexx():
    while True:
        try:
            number_one = complex(input("Enter first complex number: "))
            number_two = complex(input("Enter second complex number: "))
            break
        except:
            print("Invalid input. Please enter a valid complex number.")
        return

    print("First complex number:",(number_one))
    print("Second complex number:",(number_two))

complexx()
