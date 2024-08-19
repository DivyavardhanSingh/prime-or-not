def is_prime(number):
    # Assume the number is prime
    flag = True
    
    # Edge cases: 0, 1, and negative numbers are not prime
    if number <= 1:
        flag = False
    else:
        # Check divisibility from 2 to sqrt(number)
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                # If divisible, it's not a prime number
                flag = False
                break
    
    # Check the flag to determine if the number is prime
    if flag:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Test the function
is_prime(29)  # Example test case, replace with any number
