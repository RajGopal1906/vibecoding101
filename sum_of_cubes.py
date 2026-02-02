def find_sum_of_cubes(n):
    """
    Check if a number can be expressed as the sum of two cubes.
    Returns a list of tuples (a, b) such that a^3 + b^3 = n and a <= b.
    """
    solutions = []
    limit = int((n / 2) ** (1/3)) + 1
    
    for a in range(1, limit + 1):
        remainder = n - a**3
        if remainder < 0: 
            break
            
        # Check if remainder is a perfect cube
        b = int(round(remainder ** (1/3)))
        if b**3 == remainder:
            solutions.append((a, b))
            
    return solutions

if __name__ == "__main__":
    try:
        user_input = input("Enter a number to check: ")
        num = int(user_input)
        
        results = find_sum_of_cubes(num)
        
        if results:
            print(f"Yes, {num} can be expressed as the sum of two cubes:")
            for a, b in results:
                print(f"{num} = {a}^3 + {b}^3")
        else:
            print(f"No, {num} cannot be expressed as the sum of two cubes.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
