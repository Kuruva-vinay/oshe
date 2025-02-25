def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5]
    print(f"Sum of squares of {sample_numbers} is {sum_of_squares(sample_numbers)}")
