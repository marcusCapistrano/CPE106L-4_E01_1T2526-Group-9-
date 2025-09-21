    def main():
    # Prompt for filename
    filename = input("Enter the filename: ")

    try:
        # Read all lines into a list
        with open(filename, "r") as file:
            lines = file.readlines()

        # Remove trailing newlines
        lines = [line.rstrip("\n") for line in lines]

        # Start at the first line
        current_index = 0 if lines else -1  

        while True:
            print(f"\nThe file has {len(lines)} lines.")

            if current_index != -1:  # File not empty
                print(f"Currently at line {current_index + 1}: {lines[current_index]}")

            choice = input("Enter line number, 'next', 'prev', or 0 to quit: ").strip().lower()

            # Quit
            if choice == "0" or choice == "quit":
                print("Exiting program.")
                break

            # Navigation
            elif choice == "next":
                if current_index < len(lines) - 1:
                    current_index += 1
                else:
                    print("You are at the last line already.")
            
            elif choice == "prev":
                if current_index > 0:
                    current_index -= 1
                else:
                    print("You are at the first line already.")

            # Jump to line number
            elif choice.isdigit():
                line_num = int(choice)
                if 1 <= line_num <= len(lines):
                    current_index = line_num - 1
                else:
                    print("Invalid line number.")
            
            else:
                print("Invalid input. Please enter a line number, 'next', 'prev', or 0 to quit.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
