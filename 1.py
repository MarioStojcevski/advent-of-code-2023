dictionary = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five' : '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5' : '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

def checkIfKeyInString (string):
    for key in dictionary:
        if key in string:
            return dictionary[key]
    return False

def calculate ():
    lines = open('./input/1', 'r').readlines()
    numbers = []
    for line in lines:
        firstNumber = ''
        lastNumber = ''

        firstString = ''
        lastString = ''
        for i in range(0, len(line)):
            if(firstNumber == ''):
                firstString += line[i]
                if (checkIfKeyInString(firstString)):
                    firstNumber = checkIfKeyInString(firstString)
            if(lastNumber == ''):
                lastString = line[len(line) - i - 1] + lastString
                if (checkIfKeyInString(lastString)):
                    lastNumber = checkIfKeyInString(lastString)
        numbers.append(int(firstNumber + lastNumber))
    return sum(numbers)

def __main__ ():
    result = calculate()
    print(result)

if __name__ == '__main__':
    __main__()