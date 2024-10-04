# Read input
A, V = map(int, input().split())

# Initialize variables to store the maximum T value
min_T = float('+inf')  # Start with negative infinity for maximizing T

# Iterate over all possible values of C (here from 0 to max(A, V))
for C in range(max(A, V) + 1):
    # Calculate T for current C6 12
    T = (A ^ C) + (V ^ C)
    # Update max_T if we find a larger T
    min_T = min(min_T, T)

# Output the result
print(min_T)
