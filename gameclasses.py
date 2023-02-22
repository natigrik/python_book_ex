from gametasks import update_user_score, get_user_score


class Game:
    no_of_question = 0

    def __init__(self, no_of_question):
        self._no_of_question = no_of_question

    @property
    def no_of_question_get(self):
        return self._no_of_question

    def no_of_question_set(self, value):
        if value < 1:
            _no_of_question = 1
            print('Minimum Number of Questions = 1')
            print('Hence, number of questions will be set to 1')
        elif value > 10:
            _no_of_question = 10
            print('Maximum Number of Questions = 10')
            print('Hence, number of questions will be set to 10')
        else:
            _no_of_question = value
        print(_no_of_question)
        return _no_of_question


class BinaryGame(Game):

    def generate_questions(self):
        from random import randint
        score = 0
        for i in range(self._no_of_question):
            base10 = randint(1, 100)
            user_result = int(input("Your answer for number: " + str(base10)))
            while True:
                try:
                    answer = int(user_result, base=2)
                    if answer == base10:
                        score += 1
                        print("Good job! Your scores: " + str(score))
                        break
                    else:
                        print("Wrong answer! Correct answer is {:b}.".format(base10))
                        break
                except:
                    user_result = input("Ops! Try again. Your answer for number " + str(base10) + ": ")
        return score


class MathGame(Game):

    def generate_questions(self):
        from random import randint
        score = 0
        number_list = [0, 0, 0, 0, 0]
        symbol_list = [' ', ' ', ' ', ' ']
        operator_dict = {1: "+", 2: "-", 3: "*", 4: "**"}
        # print("создали данные")
        for i in range(self._no_of_question):
            for j in range(5):
                number_list[j] = randint(1, 9)
            # print("создали список чисел" + str(number_list))
            for k in range(4):
                if symbol_list[k - 1] == "**":
                    symbol_list[k] = operator_dict[randint(1, 3)]
                    # print("поймали дубль степени")
                else:
                    symbol_list[k] = operator_dict[randint(1, 4)]
            # print("создали список операций" + str(symbol_list))
            question_string = str(number_list[0]) + symbol_list[0] + str(number_list[1]) + symbol_list[1] \
                              + str(number_list[2]) + symbol_list[2] + str(number_list[3]) + symbol_list[3] \
                              + str(number_list[4])
            # print("создали выражение для задания" + str(question_string))
            result = eval(question_string)
            question_string.replace("**", "^")
            user_result = int(input("Your answer for ex " + question_string + " "))
            while True:
                try:
                    answer = int(user_result)
                    if answer == result:
                        score += 1
                        print("Good job! Your scores: " + str(score))
                        break
                    else:
                        print("Wrong answer! Correct answer is: " + str(result))
                        break
                except:
                    user_result = input("Ops! Try again. Your answer for ex " + question_string + ": ")
        return score
