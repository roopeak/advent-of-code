file = open("input.txt", mode="r")

game_dict = { 'red': 0, 'green': 0, 'blue': 0 }

score = 2
color = 3
games = []
sum_id = 0
character = ';'
counter = 0
semicolon_counter = 0

for line in file:
    line = line.strip()
    final = line + ';'
    print(final)

    split_line = final.split()
    
    for i in range(len(split_line)):

        # If color has ','
        if (split_line[i][len(split_line[i]) - 1] == ','):
            game_dict[split_line[i][:-1]] += int(split_line[i - 1])

        # If all blocks have been selected from the bag
        elif (split_line[i][len(split_line[i]) - 1] == ';'):
            semicolon_counter += 1
            game_dict[split_line[i][:-1]] += int(split_line[i - 1])

            if (game_dict['red'] <= 12 and game_dict['green'] <= 13 and game_dict['blue'] <= 14):
                counter += 1

            for key in game_dict:
                game_dict[key] = 0

    if (counter == semicolon_counter):
        games.append(int(split_line[1][:-1]))

    counter = 0
    semicolon_counter = 0 
            
for i in games:
    sum_id += i

print(sum_id)