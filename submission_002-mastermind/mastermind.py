import random


def run_game():
    code = [0,0,0,0]
    for item in range(4):
        value = random.randint(1,8)
        while value in code:
            value = random.randint(1,8)
        code[item] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    turns = 12

    while True:
        user_input = input('Input 4 digit code: ')
        if len(user_input) != 4 or not user_input.isdigit() or '0' in user_input or '9' in user_input:
            print("Please enter exactly 4 digits.")
            continue
    
        correct_digits = 0
        correct_places = 0

        for t in range(4):
            if code[t] == int(user_input[t]):
                correct_places += 1

        print('Number of correct digits in correct place:     ' + str(correct_places))
        
        for t in range(4):
            if int(user_input[t]) in code:
                correct_digits += 1
        correct_digits -= correct_places        
        print('Number of correct digits not in correct place: ' + str(correct_digits))

        if correct_places == 4:
            print('Congratulations! You are a codebreaker!')
            print('The code was: '+ user_input)
            break
        turns -= 1
        print("Turns left: "+str(turns))
        if turns == 0:
            break


if __name__ == "__main__":
    run_game()
