import timeit
import random

name = input('Enter your name:\n')
subject = input('Select subject (Mathematical analysis, Microeconomics, Discrete math)\n')

if subject == 'Mathematical analysis':
    from Mathematical_analysis import quests, answ
elif subject == 'Microeconomics':
    from Microeconomics import quests, answ
elif subject == 'Discrete math':
    from Discrete_Math import quests, answ

timer = timeit.default_timer()

number = 1
counter = 0

while number < 5:
    print()
    query = random.choice(quests)
    print(number, '. ', query, sep='')
    answer = input().lower()

    if answer in answ:
        if query == answ[answer]:
            print('Правильно!')
            number += 1
            counter += 1
        else:
            print('Неверно!')
            number += 1
    else:
        number += 1
        print('Ответ некорректный!')

print()
with open('input.txt', 'w') as in_file:
    in_file.write(name)
    in_file.write('\n')
    in_file.write("-" * 53)
    in_file.write('\n')

    test_time = 'Test time:'
    points = 'Points earned:'
    timer_t = str(round(timeit.default_timer() - timer)) + ' seconds'
    points_t = str(counter) + ' points'

    in_file.write("|{:^25s}|{:^25s}|".format(test_time, points))
    in_file.write('\n')
    in_file.write("|{:^25s}|{:^25s}|".format(timer_t, points_t))
    in_file.write('\n')
    in_file.write("-" * 53)
