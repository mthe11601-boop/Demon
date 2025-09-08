def is_palindrome(text):
    return text == text[::-1]

# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))   # Output: False
print(is_palindrome("madam"))   # Output: True
