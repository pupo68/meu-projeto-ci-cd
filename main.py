def calculate_sum(a: int, b: int) -> int:
    """Calculates the sum of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    return a + b

if __name__ == "__main__":
    print(f"Result of 5 + 3: {calculate_sum(5, 3)}")
