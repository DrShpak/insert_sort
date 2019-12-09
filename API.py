class API:

    @staticmethod
    def read(path):
        file = open(path, 'r')
        return file

    @staticmethod
    def get_numbers(file):
        string_numbers = str(file.readline()).split()
        numbers = []
        i = 0
        for num in string_numbers:
            numbers.append(int(num))
            i += 1
        return numbers

    @staticmethod
    def write(path, numbers):
        output = open(path, "w")
        output.write(numbers)
        output.close()
