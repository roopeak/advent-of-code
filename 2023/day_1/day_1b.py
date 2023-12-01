file = open("input.txt", mode="r")

text_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

numbers = []
sum = []
number_in_text = ""
result = 0

for line in file:
    for char in line:
        if (char.isdigit()):
            numbers.append(char)
            number_in_text = ""
        else:
            number_in_text += char

            last_char = number_in_text[len(number_in_text) - 1]

            if (len(number_in_text) > 2):
                for key in text_to_number:
                    if (key in number_in_text):
                        numbers.append(text_to_number[key])
                        number_in_text = last_char

    length = len(numbers)

    if (length == 1):
        sum.append(int(str(numbers[0] + numbers[0])))
    elif (length == 2):
        sum.append(int(str(numbers[0] + numbers[1])))
    else:
        sum.append(int(str(numbers[0] + numbers[length - 1])))

    numbers.clear()

for i in sum:
    result += i

print(result)
