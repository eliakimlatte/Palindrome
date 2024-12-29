def is_palindrome(word):
    # Check if the word is equal to its reverse
    return word == word[::-1]

while True:
    # Get user input
    word = input("Write a word (or type 'exit' to quit): ")

    # Exit the loop if the user types 'exit'
    if word.lower() == 'exit':
        print("Exiting the program.")
        break

    # Check if the word is a palindrome and print the result
    if is_palindrome(word):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


