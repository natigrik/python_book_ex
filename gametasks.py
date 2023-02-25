from os import remove, rename


def print_instructions(instruction):
    print(instruction)


def get_user_score(username):
    try:
        with open('userScores.txt', "r") as f:
            for line in f:
                content = line.split(', ')
                if username in content:
                    return content[1]
            return '-1'
    except IOError:
        print("file not found")
        with open('userScores.txt', "w"):
            return '-1'


def update_user_score(newuser, username, score):
    user_score = username + ', ' + score + '\n'
    if newuser:
        with open('userScores.txt', "a") as f:
            f.write(user_score)
    else:
        with open('userScores.tmp', 'w') as f:
            with open('userScores.txt', 'r') as f2:
                for line in f2:
                    content = line.split(', ')
                    if content[0] == username:
                        f.write(user_score)
                    else:
                        f.write(line)
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
