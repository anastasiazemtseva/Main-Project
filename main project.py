from questions import quests, answ
import timeit
import random

timer = timeit.default_timer()

counter = 1

while counter < 10:
    print()
    query = random.choice(quests)
    print(counter, '. ', query, sep='')
    answer = input().lower()

    if answer in answ:
        if query == answ[answer]:
            print('Правильно!')
            counter += 1
        else:
            print('Неверно!')
            counter += 1
    else:
        counter += 1
        print('Ответ некорректный!')

print()

print(timeit.default_timer() - timer)
