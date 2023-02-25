class Game:

    def __init__(self, no_of_question=0):
        self._no_of_question = no_of_question

    def no_of_question(self, value):
        if value < 1:
            self._no_of_question = 1
            print('Вопросов в раунде не может быть меньше 1!')
            print('Раз ты хочешь поменьше, я задам в этом раунде всего 1 вопрос!')
        elif value > 10:
            self._no_of_question = 10
            print('Вопросов в раунде не может быть больше 10!')
            print('Хочешь играть подольше? Тогда я задам тебе 10 вопросов в этом раунде!')
        else:
            self._no_of_question = value
        return self._no_of_question


class BinaryGame(Game):

    def generate_questions(self, _no_of_question):
        from random import randint
        score = 0
        for i in range(_no_of_question):
            base10 = randint(1, 100)
            user_result = input("В двоичной системе число " + str(base10) + "= ")
            while True:
                try:
                    answer = bin(base10)[2:]
                    print(answer)
                    if answer == user_result:
                        score += 1
                        print("Отлично! Твой баланс в этом раунде: " + str(score))
                        break
                    else:
                        print("Ошибочка! Правильный ответ:" + str(answer))
                        break
                except:
                    user_result = input("Ops! Try again. Your answer for number " + str(base10) + ": ")
        return score


class MathGame(Game):

    def generate_questions(self, _no_of_question):
        # self._no_of_question = _no_of_question
        from random import randint
        score = 0
        number_list = [0, 0, 0, 0, 0]
        symbol_list = [' ', ' ', ' ', ' ']
        operator_dict = {1: "+", 2: "+", 3: "+", 4: "+"}
        for i in range(self._no_of_question):
            for j in range(5):
                number_list[j] = randint(1, 9)
            for k in range(4):
                if symbol_list[k - 1] == "**":
                    symbol_list[k] = operator_dict[randint(1, 3)]
                else:
                    symbol_list[k] = operator_dict[randint(1, 4)]
            question_string = str(number_list[0]) + symbol_list[0] + str(number_list[1]) + symbol_list[1] \
                              + str(number_list[2]) + symbol_list[2] + str(number_list[3]) + symbol_list[3] \
                              + str(number_list[4])
            result = eval(question_string)
            question_string.replace("**", "^")
            user_result = input("Реши пример: " + question_string + "= ")

            while True:
                try:
                    answer = int(user_result)
                    if answer == result:
                        score += 1
                        print("Отлично! Твой баланс в этом раунде: " + str(score))
                        break
                    else:
                        print("Ошибочка! Правильный ответ: " + str(result))
                        break
                except:
                    user_result = input("Ой! Ты написал что-то не то. Попробуй еще раз: " + question_string + "= ")
        return score
