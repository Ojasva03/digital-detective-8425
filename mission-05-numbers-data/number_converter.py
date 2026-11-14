"""Convert a non-negative decimal integer to binary and hexadecimal."""

def main():
    try:
        number = int(input("Enter a non-negative decimal integer: "), 10)
        if number < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative whole number.")
        return 1
    except EOFError:
        print("No input received.")
        return 1
    print("Binary:", bin(number))
    print("Hexadecimal:", hex(number))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
