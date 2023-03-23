# use input function to get user sentence
original_sentence = input('Please type sentence here: ')

# then i would create my function. this function would utilize one parameter, a placeholder variable for my new capitalized sentence, and a for loop.
# the for loop would reiterate through the length of the passed in parameter using the range function

# within the for loop i would have if elif else statements
# i would first capitalize the beginning of any sentence through the if statement
# if index of the string character is equal to 0 i would call the capitalize function via dot notation to capitalize that string's letter and concatenate it into my placeholder variable that would hold my new capitalized sentence

# i would then capitalize words in the middle of the sentence through the elif statement
# elif index of string - 1 is equal to a space, I would also call the capitalize() Python function and concatenate it into my placeholder variable since it is the beginning of a new word

# then i would write code for the remaining pieces of my sentence 
# else the index of the string character would be concatenated into the placeholder variable as it is since that letter was not at the beginning of the sentences but still necessary to complete the sentence

def capitalize_sentence(original_sentence):
    capitalized_sentence = ''
    for i in range(len(original_sentence)):
        if i == 0:
            capitalized_sentence += original_sentence[i].capitalize() 
        elif original_sentence[i - 1] == ' ':
            capitalized_sentence += original_sentence[i].capitalize()
        else:
            capitalized_sentence += original_sentence[i]
    print(capitalized_sentence)

starter = capitalize_sentence(original_sentence)