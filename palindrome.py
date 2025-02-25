def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    test_strings = ["radar", "hello", "level", "world", "madam"]
    for s in test_strings:
        print(f"{s} is a palindrome: {is_palindrome(s)}")
