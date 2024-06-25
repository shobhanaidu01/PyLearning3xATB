# Palidrome of String


#  Palidrome of String


def is_palindrome(s):
    # Removing any spaces and converting the string to lowercase for accurate comparison
    s = s.replace(" ", "").lower()
    # Checking if the string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("naman"))  # Output: True
print(is_palindrome("nitin"))  # Output: True
print(is_palindrome("level"))  # Output: True
print(is_palindrome("shobha"))  # Output: False