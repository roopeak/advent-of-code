def main():

    file = open("input.txt", mode="r")
    
    text = []

    for line in file:
        for i in line:
            text.append(i)

    for i in range(len(text) - 3):
        string = text[i:i+4]

        if len(string) == len(set(string)):
            marker = i + 4
            break
    
    print(marker)
    
if __name__ == "__main__":
    main()