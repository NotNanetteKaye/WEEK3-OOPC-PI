# i would call user input function to obtain palindrome word
original_word = input('Type in palindrome word: ')

# then i create my palindrome finder function.  My function would require 1 parameter in order to work
# in my palindrome finder function, I would have a placeholder variable to hold my word i am trying to determine if it is a palindrome
# then i would create a for loop that reiterates through the length of my potential palindrome word from the -1 starting point and counts backwards by -1
# i do this so i can compare my potential word to the final results after the word has been reiterated through the for loop to determine if it is a palindrome word via concatenating each index of the string
# if the final result equals the potential word forwards, then the function would print a statement to confirm that the word is indeed a palindrome
# if not the else statement would then be printed to confirm that the word is not a palindrome

def palindrome_finder(potential_word):
    final_result = ''
    for i in range(len(potential_word) -1, -1, -1):
        final_result += potential_word[i]
    if final_result == potential_word:
        print(f'{potential_word} is a palindrome!')
    else:
        print(f'{potential_word} is not a palindrome.')

start = palindrome_finder(original_word)