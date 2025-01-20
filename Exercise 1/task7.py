#7. Process with an arithmetic progression (AP) 3, 6, 9, ... . The maximum value of the AP is obtained from the user. Count the number of terms that appeared in the AP, the sum of the terms and the sum of the squared terms. Use functions in your solution.

#I just made one functions which runs everything.
def aprogression():
    user_input = int(input("Give a value: "))
    ap_list = []
    if user_input > 0:
        x = range(0, user_input + 1, 3)
        for n in x:
            ap_list.append(n)
    elif user_input < 0:
        x = range(0, user_input + 1, -3)
        for n in x:
            ap_list.append(n)
    print(f"Sum of terms: {sum(ap_list)}")
    print(f"Number of terms: {len(ap_list)}")
    print(f"Sum of squared terms: {sum(n ** 2 for n in ap_list) }")

aprogression()