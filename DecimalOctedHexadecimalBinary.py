def print_formatted(number):
    # your code goes here

    width = len(bin(n)) - 2

    for i in range(1, n + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexadecimal.rjust(width),
            binary.rjust(width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
  #enter the value it give decimal octed hexadecimal binary
  
