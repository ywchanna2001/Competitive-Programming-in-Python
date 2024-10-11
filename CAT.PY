def print_pattern(n):
    # Top part (pyramids)
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1) + ' ' * (2*n-2*i) + '*' * (2*i-1))
    
    # Middle part (hourglass with stars)
    for i in range(n, 0, -1):
        print('*' * (2*i-1) + ' ' * (2*n-2*i) + '*' * (2*i-1))
    
    # Bottom part (mirrored hourglass with stars)
    for i in range(2, n+1):
        print(' ' * (n-i) + '*' * (2*i-1) + ' ' * (2*n-2*i) + '*' * (2*i-1))

# Call the function
n = 5
print_pattern(n)
