from colorama import Fore, init

init(autoreset=True)
score = 0

print(Fore.GREEN + 'Привет!')
print(Fore.BLUE + 'Это вопросы,')
print(Fore.BLUE + 'Важно одно: отвечай ' + Fore.RED + 'ТОЛЬКО' + Fore.BLUE + ' Да(y) или Нет(n)')
print(Fore.BLUE + 'Сейчас проверим что ты понял ==>')

l1 = input('Вопрос 1: <== Это вопрос? >>> ')
if l1.lower() == 'y':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

print(Fore.BLUE + 'Продолжаем...')

l2 = input('Вопрос 2: The Last Of Us ... >>> ')
if l2.lower() == '1' or l2.lower() == '2':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 3: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 4: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 5: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 6: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 7: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 8: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 9: Что дальше? >>> ')
if l3.lower() == 'вопрос':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

l3 = input('Вопрос 10: Что дальше? >>> ')
if l3.lower() == 'конец':
    print(Fore.GREEN + 'Ну... Правильно!')
    score += 1
else:
    print(Fore.GREEN + 'Ну... ' + Fore.RED + ' НЕ' + Fore.GREEN + 'Правильно!')

if score > 0 and score < 3:
    print(Fore.RED + 'Плохой результат')
elif score > 4 and score < 8:
    print(Fore.YELLOW + 'Средний результат')
elif score > 9:
    print(Fore.GREEN + 'Отличный результат')

