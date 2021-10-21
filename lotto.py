from random import shuffle

numbers = []
for i in range(49):
    i += 1
    numbers.append(i)  # to change  - get int, need str

shuffle(numbers)
comp_choise = numbers[0:6]

print('Welcome in LOTTO lottery.!!!')
print("Choose 6 numbers from 1 to 49. If you hit more than 3 - You will win\n")
usr_numbers = []
result = 0

for i in range(6):
    i +=1
    while True:
        try:

            usr_num = int(input(f'{i}: Pick your number from 1 to 49: '))

            if usr_num in usr_numbers:
                print("You chose this number earlier! Try again\n")
                continue
            elif usr_num > 49 or usr_num < 1:
                print("It's not number between from 1 to 49: Try again\n")
                continue

            break
        except ValueError:
            print("It's not a correct number! Try again!\n")
            continue
    if usr_num in usr_numbers:
        result += 1
    usr_numbers.append(str(usr_num))
print(f'Twoje liczby to:    {", ".join(sorted(usr_numbers))}')
print(f'Komputer wylosował liczby:    {comp_choise}') #  after change add .join
print(f"You have {result} hitts.")
if result >= 3:
    print('You WON' + '!' * result)

