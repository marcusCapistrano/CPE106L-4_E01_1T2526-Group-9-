def mean(numbers):
    """Return the average of the numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    """Return the median of the numbers."""
    if not numbers:
        return None
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    return nums[mid] if n % 2 else (nums[mid - 1] + nums[mid]) / 2

def mode(numbers):
    """Return the mode (most frequent number) of the list."""
    if not numbers:
        return None
    counts = {num: numbers.count(num) for num in set(numbers)}
    max_count = max(counts.values())
    modes = [num for num, c in counts.items() if c == max_count]
    return modes[0] if len(modes) == 1 else modes

# Test run
if __name__ == "__main__":
    data = [5, 3, 8, 3, 9, 5, 3]
    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
    