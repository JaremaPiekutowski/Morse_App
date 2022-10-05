from code import code


def string_input() -> str:
    return str(input("Enter a string. A-Z/a-z letters and 0-9 numbers only:"))


def check_string(s: str) -> bool:
    for letter in s:
        if letter.isalpha() or letter.isnumeric() or letter == " ":
            pass
        else:
            print(f"The string contains at least one invalid character: {letter}")
            return False
    return True


def morse_encode(s: str, c: dict) -> str:
    m = ""
    for letter in s:
        if letter == ' ':
            m += '/'
        else:
            m += (c[letter] + '/')
    return m


def main() -> None:
    while True:
        data = string_input().lower()
        if check_string(data):
            break
    morse = morse_encode(s=data, c=code)
    print(f"The Morse code for the string is:\n{morse}")


main()
