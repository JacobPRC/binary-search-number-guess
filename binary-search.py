# def binary_search(list, item):
#     low = 0
#     high = len(list)-1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None


# my_list = [1, 3, 5, 7, 9, 11]

# print(binary_search(my_list, 3))

def guess_a_num():
    low = 0
    high = 100

    possible_answers = list(range(0, 101))

    print("Guess a number between 0 and 100")

    num = input()

    print("Okay let me try to guess it")

    while low <= high:
        mid = (low + high) // 2
        guess = possible_answers[mid]
        print(
            f"Is this your number: {guess}? If yes, type y, if it's too high, type - and if it's too low type +")
        response = input()
        if response == "y":
            return print("Woo! I got it!")
        if response == "-":
            high = mid - 1
        else:
            low = mid + 1
    return print("I don't think you put in the right number...")


guess_a_num()
