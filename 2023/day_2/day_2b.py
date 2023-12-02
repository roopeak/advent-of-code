import math

file = open("input.txt", mode="r")

game_dict = { 'red': 0, 'green': 0, 'blue': 0 }
list_of_cubes = []
sum_id = 0
character = ';'

for line in file:
    line = line.strip()
    final = line + ';'

    split_line = final.split()
    
    for i in range(len(split_line)):

        # If color has ','
        if (split_line[i][len(split_line[i]) - 1] == ','):
            cube = int(split_line[i - 1])

            if (cube > game_dict[split_line[i][:-1]]):
                game_dict[split_line[i][:-1]] = cube

        # If all blocks have been selected from the bag
        elif (split_line[i][len(split_line[i]) - 1] == ';'):
            cube = int(split_line[i - 1])

            if (cube > game_dict[split_line[i][:-1]]):
                game_dict[split_line[i][:-1]] = cube

    # Add all the values to a list of cubes
    for key in game_dict:
        list_of_cubes.append(game_dict[key])

    # Multiply list values
    sum_id += math.prod(list_of_cubes)

    # Empty list and dict
    list_of_cubes = []
    game_dict = { 'red': 0, 'green': 0, 'blue': 0 }


# Print result
print(sum_id)