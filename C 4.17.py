def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return True
    else:
        return False


input_string = "racecar"
if is_palindrome(input_string):
    print(f"'{input_string}' adalah palindrom.")
else:
    print(f"'{input_string}' bukan palindrom.")


input_string = "formula1"
if is_palindrome(input_string):
    print(f"'{input_string}' adalah palindrom.")
else:
    print(f"'{input_string}' bukan palindrom.")


input_string = "motogp"
if is_palindrome(input_string):
    print(f"'{input_string}' adalah palindrom.")
else:
    print(f"'{input_string}' bukan palindrom.")


input_string = "lockheedmartin"
if is_palindrome(input_string):
    print(f"'{input_string}' adalah palindrom.")
else:
    print(f"'{input_string}' bukan palindrom.")


input_string = ""
if is_palindrome(input_string):
    print(f"'{input_string}' adalah palindrom.")
else:
    print(f"'{input_string}' bukan palindrom.")