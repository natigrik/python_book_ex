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
    bg = BinaryGame()
    mg = MathGame()
    username = input("Введи свое имя: ")
    score = int(get_user_score(username))
    if score == -1:
        newuser = True
        score = 0
    else:
        newuser = False
    print("Привет, " + username + "! Твой баланс очков: " + str(score))

    user_choice = 0
    while user_choice != -1:
        game = int(input("Математическая игра (1) или Двоичная игра (2)? "))
        while game not in (1, 2):
            game = int(input("Кажется, ты выбрал что-то не то. Математическая игра (1) или Двоичная игра (2)? "))

        num_prompt = int(input("Сколько вопросов ты хочешь получить в этом раунде (1 to 10)? "))
        while True:
            try:
                num = int(num_prompt)
                break
            except:
                num_prompt = int(input("Что-то не так. Сколько вопросов ты хочешь получить в этом раунде (1 to 10)? "))

        if game == 1:
            _no_of_question = mg.no_of_question(num)
            print_instructions(math_instruction)
            score += mg.generate_questions(_no_of_question)
            print("Поздравляю! Теперь твой баланс очков: " + str(score))
            user_choice = int(input("Что дальше? Сыграем еще раз (1) или попрощаемся (-1)? "))
        elif game == 2:
            _no_of_question = bg.no_of_question(num)
            print_instructions(binary_instruction)
            score += bg.generate_questions(_no_of_question)
            print("Поздравляю! Теперь твой баланс очков: " + str(score))
            user_choice = int(input("Что дальше? Сыграем еще раз (1) или попрощаемся (-1)? "))
        else:
            print("При выборе игры произошла ошибка, попробуй запустить заново.")
            break
    update_user_score(newuser, username, str(score))

except:
    print("Произошла какая-то неведомая фигня. Запусти приложение заново.")
