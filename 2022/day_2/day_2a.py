def read_file(file):

    your_score = 0

    for line in file:
        
        # Rock
        if line[0] == "A":
            if line[2] == "Y":
                your_score += 8
            elif line[2] == "Z":
                your_score += 3
            elif line[2] == "X":
                your_score += 4

        # Paper
        if line[0] == "B":
            if line[2] == "Y":
                your_score += 5
            elif line[2] == "Z":
                your_score += 9
            elif line[2] == "X":
                your_score += 1

        # Scissors
        if line[0] == "C":
            if line[2] == "Y":
                your_score += 2
            elif line[2] == "Z":
                your_score += 6
            elif line[2] == "X":
                your_score += 7

    print(your_score)

def main():
    file = open("input.txt", mode="r")
    read_file(file)

if __name__ == "__main__":
    main()