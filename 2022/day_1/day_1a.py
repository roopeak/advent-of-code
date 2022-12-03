def read_file(file):

    calories = []

    current_calories = 0
    highest_calories = 0

    for line in file:

        calories.append(line.rstrip("\n"))

        if line == "":
            current_calories = sum(calories)
            calories.clear()

        if current_calories > highest_calories:
            highest_calories = current_calories




    print(highest_calories)
    
def main():
    file = open("input.txt", mode="r")
    read_file(file)
if __name__ == "__main__":
    main()