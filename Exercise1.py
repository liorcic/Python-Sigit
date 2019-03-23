user_password = "1234"
user_balance = 25378


def check_code():
    code = input("Please enter your code : ")
    if code == user_password:
        return True
    return False


def print_menu():
    print("Hi, please select your action")
    print("A. Show balance")
    print("B. Take money")
    print("C. Change password")
    print("D. Exit")
    return input()


# Function that receive a num and return if it is possible to give that mnum with only 20's and 50's
def check_validity_sum(num):
    if num % 50 == 0 or num % 20 == 0:
        return True
    while num % 50 != 0 and num != 0:
        num = num - 20
    if num != 0:
        return True
    return False


def show_money_options():
    print("How much money would you like ?")
    print("A. 20")
    print("B. 50")
    print("C. Other")
    user_input = input()
    if user_input == "A" or user_input == "a":
        return 20
    elif user_input == "B" or user_input == "b":
        return 50
    elif user_input == "C" or user_input == "c":
        request_money = int(input("How much would you like ?"))
        if check_validity_sum(request_money):
            return request_money
        else:
            print("You need to enter a sum divisable by 20 or 50")
    else:
        print("Wrong input")
        return 0


def show_balance():
    print("The balance of your account is : ", user_balance, " USD")


# Starting machine
while True:
    if check_code():
        user_input = print_menu()
        if user_input == "A" or user_input == "a":
            show_balance()
            print()
        elif user_input == "B" or user_input == "b":
            user_request = show_money_options()
            user_balance -= user_request
            show_balance()
        elif user_input == "C" or user_input == "c":
            user_password = input("Please enter new password : ")
        elif user_input == "D" or user_input == "d":
            break
        else:
            print("Error in choice")
    else:
        print("Code error")