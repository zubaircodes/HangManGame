#Name; Zubair Mohamed


import random
def main():
    
    answer_list = ["change", "apple", "grapes", "banana", "egg", "cheese", "cat", "mouse", "olive"]
    answer = chosen_answer(answer_list)
    unanswered = "*" * len(answer)
    c = 0
    while "*" in unanswered:
        print("Guess a letter in the word ")
        letter = input(unanswered + ">")
        answer_letter(answer, letter)
        unanswered, c = search_letter(unanswered, letter, answer, c)
    print("The word is " + str(answer) + ". You missed " + str(c) + " times")
        

def chosen_answer(answer_list):
    return random.choice(answer_list)

def answer_letter(answer, letter):
    picked_words = []
    for a in range(len(answer)):
        char = answer[a]
        picked_words.append(char)

def search_letter(unanswered, letter, answer ,c):
    correct = False
    for a in range(len(answer)):
        if(letter == answer[a]):
            correct = True
            unanswered = unanswered[:a] + letter + unanswered[a +1:]
    if not correct:
        print(letter + " is not in the word")
        c = c+ 1
    return unanswered, c

main()
