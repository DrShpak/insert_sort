from API import *


def insert_sort(numbers):
    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = temp
    return numbers


def run(path):
    numbers = API.get_numbers(API.read(path))
    listToStr = ' '.join([str(elem) for elem in insert_sort(numbers)])
    API.write("insert_sort/output.txt", listToStr)


run("insert_sort/input.txt")
