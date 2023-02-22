from gametasks import print_instructions, get_user_score, update_user_score
from gameclasses import Game, BinaryGame, MathGame

try:
    math_instruction = 'В этой игре вам предлагается решить простую арифметическую задачу. ' \
                       'За каждый правильный ответ вам начисляется одно очко. ' \
                       'За ошибочные ответы очки не вычитаются.'
    binary_instruction = 'В этой игре вы получаете десятичное число. ' \
                         'Ваша задача — преобразовать его в двоичную систему счисления. ' \
                         'За каждый правильный ответ вам начисляется одно очко. ' \
                         'За ошибочные ответы очки не вычитаются.'
    bg = BinaryGame(0)
    mg = MathGame(0)
    username = input("Enter your name: ")
    score = int(get_user_score(username))
    if score == -1:
        newuser = True
        score = 0
    else:
        newuser = False
    print("Welcome, " + username + "! Your score: " + str(score))

    user_choice = 0
    while user_choice != -1:
        game = int(input("Math Game (1) or Binary Game (2)? "))
        while game not in (1, 2):
            game = int(input("Incorrect choice! Math Game (1) or Binary Game (2)? "))

        num_prompt = int(input("How many questions do you want per game (1 to 10)? "))
        while True:
            try:
                num = int(num_prompt)
                print("количество вопросов - " + str(num))
                break
            except:
                num_prompt = int(input("Incorrect choice! How many questions do you want per game (1 to 10)?"))

        if game == 1:
            mg._no_of_question = num
            print_instructions(math_instruction)
            score += mg.generate_questions()
            print("Congratulate! Your score: " + str(score))
            user_choice = int(input("Press Enter to continue or enter -1 to exit "))
        elif game == 2:
            bg.no_of_question_set = num
            print_instructions(binary_instruction)
            score += bg.generate_questions()
            print("Congratulate! Your score: " + str(score))
            user_choice = int(input("Press Enter to continue or enter -1 to exit "))
        else:
            print("Oops! WTF?!")
            break
    update_user_score(newuser, username, str(score))

except:
    print("Oops! WTF?! Bye-bye!")
