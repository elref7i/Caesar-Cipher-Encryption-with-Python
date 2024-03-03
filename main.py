alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caeser(d,t,s):
    end_text = ""
    if (d == "decode"):
        s *= -1
    for letter in t:
        if letter == " ":
            continue
        elif letter.isnumeric():
            continue
        else:
            position = alphabet.index(letter)   #tricks
            end_text += alphabet[position + s]

    print(f"the {d} and end text is {end_text}")
from cipher import logo
print(logo)
are_you_ok = False
while not are_you_ok:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caeser(d=direction, t=text, s=shift)
    q = input("agin??").lower()
    if q == "no":
        are_you_ok = True
        print("Good Lock pro")











