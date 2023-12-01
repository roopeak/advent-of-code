file = open("input.txt", mode="r")

sum = []
combined_number = []
result = 0

for line in file:
    for char in line:
        if (char.isdigit()):
            combined_number.append(char)

    length = len(combined_number)

    if (len(combined_number) > 1):
       sum.append(int(str(combined_number[0] + combined_number[length-1])))
    elif (len(combined_number) == 1):
        sum.append(int(str(combined_number[0] + combined_number[0])))
        
    combined_number.clear()

for i in sum:
    result += i

print(result)