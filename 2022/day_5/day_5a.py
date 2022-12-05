def main():

    crates_file = open("crates.txt", mode="r")
    input_file = open("input.txt", mode="r")
    
    data = {
        1:["N", "B", "D", "T", "V", "G", "Z", "J"],
        2:["S", "R", "M", "D", "W", "P", "F"],
        3:["V", "C", "R", "S", "Z"],
        4:["R", "T", "J", "T", "Z", "P", "H", "G"],
        5:["T", "C", "J", "N", "D", "Z", "Q", "F"],
        6:["N", "V", "P", "W", "G", "S", "F", "M"],
        7:["G", "C", "V", "B", "P", "Q"],
        8:["Z", "B", "P", "N"],
        9:["W", "P", "J"]
    }

    for row in input_file:
        row_splitted = row.split()
        
        crates_to_move = int(row_splitted[1])
        from_crate = int(row_splitted[3])
        to_crate = int(row_splitted[5])
        
        for i in range (crates_to_move):
            pop = data[from_crate].pop()
            data[to_crate].append(pop)
                
    for i in data.keys():
        print(data[i][-1])

if __name__ == "__main__":
    main()