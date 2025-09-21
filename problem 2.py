def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        lines = [line.rstrip("\n") for line in lines]

        while True:
            print(f"\nThe file has {len(lines)} lines.")
            choice = int(input("Enter a line number (0 to quit): "))

            if choice == 0:
                print("Exiting program. Goodbye!")
                break
            elif 1 <= choice <= len(lines):
                print(f"Line {choice}: {lines[choice - 1]}")
            else:
                print("Invalid line number. Try again.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
