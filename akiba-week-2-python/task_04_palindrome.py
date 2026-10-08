string = input("Input your string: ")

lower_string = string.lower()
reverse_string = lower_string[::-1]

if lower_string == reverse_string:
    print("It is palindrome")
else:
    print("Not Palindrome")
