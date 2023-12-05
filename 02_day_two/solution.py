config = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def calculate(isDayTwo):
    games = open('input.txt', 'r').readlines()
    result = 0
    sumOfPowers = 0
    for i in range(0, len(games)):
        game = games[i]
        sets = game.split(': ')[1].split('; ')
        isPossible = False

        fewestBallsInGame = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for set in sets:
            balls = set.strip().split(', ')
            for ball in balls:
                ballsNumber = ball.split(' ')[0]
                ballsColor = ball.split(' ')[1]

                if fewestBallsInGame[ballsColor] < int(ballsNumber):
                    fewestBallsInGame[ballsColor] = int(ballsNumber)

                if config[ballsColor] >= int(ballsNumber):
                    isPossible = True
                else:
                    isPossible = False
                    if not isDayTwo: break
            
            if not isPossible and not isDayTwo:
                break
        sumOfPowers += fewestBallsInGame['red'] * fewestBallsInGame['green'] * fewestBallsInGame['blue']
        if isPossible:
            result += i + 1
                
    return result, sumOfPowers

def __main__ ():
    isDayTwo = False
    result, sumOfPowers = calculate(isDayTwo)
    print(f'Sum of game indexes which are possible {result}')
    print(f'Sum of powers of the fewest balls in each color {sumOfPowers}')

if __name__ == '__main__':
    __main__()