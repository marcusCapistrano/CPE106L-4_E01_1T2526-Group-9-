

def median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_count = max(frequency.values())
    modes = [key for key, count in frequency.items() if count == max_count]
    return modes[0] if modes else 0

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    test_numbers = [1, 2, 2, 3, 4]
    print("Test Numbers:", test_numbers)
    print("Median:", median(test_numbers))
    print("Mode:", mode(test_numbers))
    print("Mean:", mean(test_numbers))

if __name__ == "__main__":
    main()
