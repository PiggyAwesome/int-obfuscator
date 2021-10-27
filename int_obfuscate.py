import string


def decode(yourCode):
        yourCode = str(yourCode)
        num = 0
        temp = []
        fin = []

        numb = 0
        for number in yourCode:
            numb += 1
            temp.append(number)
            if numb == 2:
                fin.append("".join(temp))
                temp = []
                numb = 0

        yourCode = "|".join(fin)

        for character in string.printable:
            if num < 10:
                exec(f"num = \"0{num}\"")
            yourCode = yourCode.replace(f"{num}", character)
            num = int(num)
            num += 1
        return yourCode.replace("|", "")


def obfuscate(yourCode):
    if "|" in yourCode:
        raise ValueError("Invalid character: \"|\"")
        
    nump = 0
    for character in string.printable:
        if nump < 10:
            exec(f"nump = \"0{nump}\"")
        yourCode = yourCode.replace(character, str(nump))
        nump = int(nump)
        nump += 1

    return yourCode

