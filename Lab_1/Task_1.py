numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index = 0

while numbers[index] is not None:
    index += 1

sum_of_numbers = sum(numbers[:index]) + sum(numbers[index + 1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers

numbers[index] = average_of_numbers

print("Измененный список:", numbers)
