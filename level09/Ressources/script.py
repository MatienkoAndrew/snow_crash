import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        token = f.readlines()
        token = token[0]
        decrypted = ""
        for idx, ch in enumerate(token):
            number = ord(ch) - idx
            if number < 0:
                number += 256
            elif number >= 256:
                number -= 256
            decrypted += chr(number)
    print(decrypted)
