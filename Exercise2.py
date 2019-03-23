# Sum the list of numbers
def sum_list(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

# input numbers in the array until hit Stop
def input_numbers():
    num_array = []
    print("Please input all the numbers : ")
    number = input("Enter a num or Stop : ")
    while number != "Stop":
        number = int(number)
        num_array.append(number)
        number = input("Enter a num or Stop : ")
    return num_array


def main():
    num_array = input_numbers()
    sum_numbers = sum_list(num_array)
    print("The sum is ", sum_numbers)


main()