def main():

    file = open("input.txt", mode="r")

    letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    items = []

    rucksacks = []

    for line in file:

        rucksacks.append(line.rstrip("\n"))

        if len(rucksacks) == 3:
            strings = list(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))

            for i in strings:
                items.append(i)
            
            rucksacks.clear()
    
    print(items)

    total_priority = 0

    for i in items:
        if i in letters:
            priority = letters.index(i)
            total_priority += priority
    
    print(total_priority)

if __name__ == "__main__":
    main()