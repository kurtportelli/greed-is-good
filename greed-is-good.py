def score(dice):
    points = 0
    if dice.count(1) >= 3:
        points += 1000
        for i in range(3):
            dice.remove(1)
    for num in range(2, 7):
        if dice.count(num) >= 3:
            points += num * 100
            for i in range(3):
                dice.remove(num)
    for die in dice:
        if die == 1:
            points += 100
        if die == 5:
            points += 50
    return points
