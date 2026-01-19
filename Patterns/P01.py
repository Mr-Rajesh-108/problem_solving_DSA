# def pyramid(n):
#     for i in range(1, n+1):
#         # print spaces + stars
#         print(" " * (n - i) + "*" * (2*i - 1))

# # Example
# pyramid(2)


def pattern(n):
    # Line 1: Pyramid top
    print(" " * (n+1) + "*")

    # Line 2: Pyramid wider
    print(" " * n + "***")

    # Line 3: Special line with @
    print(" " * n + "@ @")

    # Line 4: Combined middle pattern
    print("***@ @***")

    # Line 5: Bottom with space in middle
    print(" " + "*" + " " * (2*n-1) + "*")


# Driver code
n = 3
pattern(n)
