with open('table.txt', 'w') as wf:
    for i in range(1, 11):
        wf.write(f'10 * {i}  = {10 * i}\n')


with open('family.txt', 'w') as wf:
    numOfPeople = int(input('How many people are in your family? '))
    for nums in range(1, numOfPeople):
        familyMember = input(f'who is {nums} member of your famiy? ')
        nameOfFamilyMember = input(f'What is your {familyMember}s name? ')
        wf.write(f'{familyMember} - {nameOfFamilyMember}\n')
    name = input('What is your name? ')    
    wf.write(f'Me - {name}')

with open('names.txt', 'w') as wn:
    names = ['Timur', 'Shukhrat', 'Sanjar']
    for name in names:
        newName = ''
        for i, char in enumerate(name):
            if i % 2 == 0: newName += char.upper()
            else: newName += char
        wn.write(f'{newName}\n')

with open('digits.txt', 'w') as wd:
    nums = [123, 1000, 654, 12, 10093]
    for num in nums:
        digitList = []
        otvet = 0
        while num > 0:
            digit = num % 10
            otvet = otvet + digit
            digitList.append(digit)
            num = num // 10
        digitList.reverse()
        str = ''
        for i, digit in enumerate(digitList):
            if i != len(digitList) - 1: str = str + f'{digit} + '
            else: str = str + f'{digit} = {otvet}'
        wd.write(f'{str}\n')
