def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    user_input = int(input("Input : "))
    
    if is_prime(user_input):
        print("Output : It is Prime Number")
    else:
        print("Output : It is not a Prime Number")
except ValueError:
    print("Invalid input. Please enter an integer.")
