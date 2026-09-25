import encryption

def output(result: str) -> None:
    with open("Output.txt", "w") as f:
        f.write(result)

def main() -> None:
    text = input("Enter Text:\n")
    result = ""

    for letter in text:
        if ord(letter) >= 65 and ord(letter) <= 90:
            result += encryption.rotors(letter)
        else:
            result += letter

    output(result)

if __name__ == "__main__":
    main()