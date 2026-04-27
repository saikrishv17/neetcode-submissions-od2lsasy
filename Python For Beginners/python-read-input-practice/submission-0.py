def add_two_numbers() -> int:
    line = input()
    sum = 0 
    for char in line.split(","):
        sum += int(char)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
