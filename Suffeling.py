def shuffle_index(n, p):
    """ 
    Simulate the shuffling process and find the index of the city after (p-1) shuffles.
    n: the index of the city to track
    p: the number of shuffling rounds based on 2^p cities
    """
    num_of_shuffles = p - 1
    size = 2**p

    for _ in range(num_of_shuffles):
        new_index = 0
        if n % 2 == 0:
            new_index = n // 2
        else:
            new_index = size // 2 + (n - 1) // 2
        n = new_index

    return n

# Input handling
p = int(input("Enter P: "))
n = int(input("Enter N: "))

# Perform the shuffling and get the result
result_index = shuffle_index(n, p)

# Output the city they will visit
print(f"City they will visit: {result_index}")
