def calculate_value(n, m, x):
    # Step 1: Check if min(n, m) - 1 is less than x
    min_value = min(n, m)
    max_value = max(n, m)
    if n == m == 1:
        if x == 1:
            return 1
        return 0
    
    elif min_value == 1:
        if x == 1:
            if max_value % 2 == 1:
                return (max_value / 2) + 1
            return max_value / 2
        return 0
    
    elif min_value - 1 < x:
        return 0
    
    else:
        # Step 2: Compute intermediate values for the conditions
        term_n = 2 * (n - 2 * (x - 1))
        term_m = 2 * (m - 2 * (x - 1))
        
        # Step 3: Check if both terms equal 1
        if term_n/2 == 1 and term_m/2 == 1:
            return 1
        
        # Step 4: Compute the result
        result = (term_n + term_m - 4) / 2
        
        # Step 5: Check if result is between 0 and 1
        if 0 < result < 1:
            return 1
        
        return int(result)

# Example usage:
n, m = map(int, input().strip().split())
x = int(input())

print(int(calculate_value(n, m, x)))

