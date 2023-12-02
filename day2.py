total = 0
maxes = {'red': 12, 'green': 13, 'blue': 14}
part_2 = True
with open('day2.txt', 'r') as file:
    while True:
        mins = {'red': 0, 'green': 0, 'blue': 0}
        not_possible = False
        line = file.readline().replace('\n', '')
        if not line:
            break
        game_id, content = line.split(':')
        game_id = game_id.replace("Game ", "")
        games = content.split(';')
        for game in games:
            rounds = game.split(',')

            for r in rounds:
                _, number, color = r.split(' ')
                if part_2:
                    mins[color] = max(mins[color], int(number))
                else:
                    if maxes[color] < int(number):
                        not_possible = True
                        break
            if not_possible:
                break
        if part_2:
            total += mins['red']*mins['blue']*mins['green']
        else:
            if not not_possible:
                total += int(game_id)
                not_possible = False
                
print(total) 
                