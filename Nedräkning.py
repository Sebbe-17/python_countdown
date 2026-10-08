print('Detta program tar emot ett värde och räknar sedan ner med ett annat inskrivet värde')

loop1 = 'true'
while loop1 == 'true':
    operand_1 = int(input('\nAnge ett start-värde: '))
    operand_2 = int(input('\nAnge ett nedräknings-värde: '))

    fortsätt = 'true'
    while fortsätt == 'true':  # Oändlig loop startar
        operand_1 = operand_1 - operand_2
        print(operand_1)
        
        if operand_1 <= 0:
            fortsätt = 'false'

    print('Nedräkning klar ditt slutvärde var: ', operand_1)

        
    
    
    
    
    
