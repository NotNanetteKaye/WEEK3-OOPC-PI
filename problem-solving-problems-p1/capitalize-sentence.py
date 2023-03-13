original_sentence = input('Please type sentence here: ')
def capitalize_sentence(originalSentence):
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