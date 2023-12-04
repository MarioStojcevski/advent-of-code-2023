config = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def calculate():
    games = open('./input', 'r').readlines()
    result = 0
    for i in range(0, len(games)):
        game = games[i]
        data = game.split(': ')
        sets = data[1].split('; ')

        isPossible = True
        for set in sets:
            balls = set.strip().split(', ')
            for ball in balls:
                ballsNumber = ball.split(' ')[0]
                ballsColor = ball.split(' ')[1]
                print(f'{ballsColor}-{ballsNumber}')
                isPossible = int(ballsNumber) <= config[ballsColor]

        if isPossible:
            result += i + 1
                
    return result

def __main__ ():
    result = calculate()
    print(result)

if __name__ == '__main__':
    __main__()