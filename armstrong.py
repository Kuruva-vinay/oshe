def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == number

if __name__ == "__main__":
    test_numbers = [153, 370, 371, 407, 9474, 9475]
    for num in test_numbers:
        if is_armstrong(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
