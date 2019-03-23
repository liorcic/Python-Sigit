# Function that receive an id and returns if its legal
def find_bikoret(number_id):
    sum_id = 0
    kafoul = True
    bikoret_digit = number_id % 10
    number_id = int(number_id / 10)
    while number_id != 0:
        digit = number_id % 10
        number_id = int(number_id / 10)
        if kafoul:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
            kafoul = False
        else:
            kafoul = True
        sum_id += digit
    bikoret = 10 - (sum_id % 10)
    if bikoret == bikoret_digit:
        return True
    return False


num_id = int(input("Please enter id : "))
validity = find_bikoret(num_id)
if validity:
    print("This is a legal id ;) The check number is ", num_id%10)
else:
    print("This is not a legal id :(")