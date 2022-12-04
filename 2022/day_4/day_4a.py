def main():

    file = open("input.txt", mode="r")

    first_pairs = []
    second_pairs = []

    total_overlaps = 0

    for line in file:

        line_splitted = line.rstrip("\n").split(",")

        first_pair = "".join(line_splitted[0]).split("-")
        second_pair = "".join(line_splitted[1]).split("-")

        for i in range(int(first_pair[0]), int(first_pair[1]) + 1):
            first_pairs.append(i)
        
        for j in range (int(second_pair[0]), int(second_pair[1]) + 1):
            second_pairs.append(j)

        first_set = set(first_pairs)
        second_set = set(second_pairs)

        if len(first_set.intersection(second_set)) == len(first_set):
            total_overlaps += 1
        elif len(second_set.intersection(first_set)) == len(second_set):
            total_overlaps += 1
        else:
            pass
        
        first_pairs.clear()
        second_pairs.clear()
        
    print(total_overlaps)
    
if __name__ == "__main__":
    main()