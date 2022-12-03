def main():

    file = open("input.txt", mode="r")

    letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    items = []

    for line in file:
        middle = int(len(line) / 2)

        first_rucksack, second_rucksack = line[:middle], line[middle:]
        
        strings = list(set(first_rucksack) & set(second_rucksack))
        
        for i in strings:
            items.append(i)

    total_priority = 0

    for i in items:
        if i in letters:
            priority = letters.index(i)
            total_priority += priority
    
    print(total_priority)

if __name__ == "__main__":
    main()