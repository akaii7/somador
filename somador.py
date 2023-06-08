def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True

sum = 0
new_input = None

while new_input != '':
    new_input = input('Insira um número: ')
    new_input = new_input.strip()

    if isnumber(new_input):
        sum += float(new_input)
    elif new_input != '':
        print('Insira apenas números.')

print(f'A soma final foi igual a: {sum}.')