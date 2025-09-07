
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    # Reverse the string and compare
    return cleaned == cleaned[::-1]

# Ask the user for input
user_input = input("Enter a word or phrase: ")

# Check and display result
if is_palindrome(user_input):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
