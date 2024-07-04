def print_star_pyramid(n):
    for i in range(n):
        # Print spaces on the left to center the stars
        print(' ' * ((n - i - 1)*2), end='')
        # Print stars
        print('*' * (2 * i + 1))

# Get the number of levels from the user
n = int(input("Enter the number of levels for the pyramid: "))
print_star_pyramid(n)
