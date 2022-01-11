# define a function
def add_two(a, b):
    return a + b


def mult_two(a, b):
    return a * b


# Main code starts with    if __name__ == "__main__":
if __name__ == "__main__":
    a = 10
    b = 20
    c = add_two(a, b)  # Calling a function
    print(f"{a} + {b} = {c}")

    for i in range(2, 10):  # for-loop i=2 ... 9 (<10)
        print(f"======{i}======")
        for j in range(2, 10):  # duplicated for-loop  j=2 ... 9, Therefore (i, j) = (2, 2) ... (9, 9)
            k = mult_two(i, j)
            print(f"{i} x {j} = {k}")
        if i == 2:  # Condition
            print("This was easy.")
        elif i == 9:
            print("This was hard.")
        else:
            print("So-so.")
