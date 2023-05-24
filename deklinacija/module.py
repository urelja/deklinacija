import deklinacija.utils as utils

VOWELS = ["a", "а", "e", "е", "i", "и", "o", "о",
          "u", "у"]  # used for identifying consonants

NEP_A = ["ар","ац","ај","ађ"] # words ending with these letters aren't prone to the nepostojano a sound change, the majority of names end like this

INSTRUMENTAL_LETTERS = ["ј", "љ", "њ", "ђ", "ћ", "ч", "џ", "ш", "ж"]
PALATALIZACIJA = {"k": "č", "g": "ž", "h": "š", }


def genitiv(name, gender, latin=True):
    utils.check(name, gender, latin)

    name = list(name.strip())

    lastChar = name[-1]
    secToLastChar = name[-2]
    trdToLastChar = name[-3]

    if latin == True:

        if (secToLastChar+lastChar).lower() == "ia":
            name.pop(-1)
            if lastChar.isupper():
                name.append("JE")
                return "".join(name)
            else:
                name.append("je")
                return "".join(name)

        if lastChar in ["a", "A"]:
            if lastChar.isupper():
                name[-1] = "E"
                return "".join(name)
            else:
                name[-1] = "e"
                return "".join(name)

        if gender.lower() == "female":
            if lastChar not in ["a", "A"]:
                return "".join(name)

        if gender.lower() == "male":
            if lastChar in ["e", "E"]:
                if lastChar.isupper():
                    name[-1] = "A"
                    return "".join(name)
                else:
                    name[-1] = "a"
                    return "".join(name)

            if lastChar in ["o", "O"]:
                if lastChar.isupper():
                    name[-1] = "A"
                    return "".join(name)
                else:
                    name[-1] = "a"
                    return "".join(name)

            if lastChar in ["i", "I"]:
                if lastChar.isupper():
                    name.append("JA")
                    return "".join(name)
                else:
                    name.append("ja")
                    return "".join(name)

            if lastChar not in VOWELS and trdToLastChar not in VOWELS:
                # nepostojano a
                if len(name) >= 4:
                    if secToLastChar in ["a", "A"]:
                        # od Stefana, od Miroslava, od Miodraga...
                        
                        lastTwo = name[-2]+name[-1]

                        if utils.toCyrillic(lastTwo) not in NEP_A:
                            if lastChar.isupper():
                                name.append("A")
                            else:
                                name.append("a")
                        else:  # od Petra, od Aleksandra...
                            if name[-1].isupper():
                                name[-2] = name[-1]
                                name[-1] = "A"
                            else:
                                name[-2] = name[-1]
                                name[-1] = "a"
                    else:
                        if lastChar.isupper():
                            name.append("A")
                        else:
                            name.append("a")
                else:
                    if lastChar.isupper():
                        name.append("A")
                    else:
                        name.append("a")
            else:
                if lastChar.isupper():
                    name.append("A")
                else:
                    name.append("a")

    return "".join(name)


def dativ(name, gender, latin=True):
    utils.check(name, gender, latin)
    name = name.strip()
    name = list(genitiv(name, gender, latin))

    lastChar = name[-1]
    secToLastChar = name[-2]
    trdToLastChar = name[-3]

    if latin == True:
        if lastChar == "a":
            name[-1] = "u"
        elif lastChar == "A":
            name[-1] = "U"
        elif lastChar == "e":
            name[-1] = "i"
        elif lastChar == "E":
            name[-1] = "I"

        return "".join(name)


def akuzativ(name, gender, latin=True):
    utils.check(name, gender, latin)
    name = name.strip()
    name = list(genitiv(name, gender, latin))

    lastChar = name[-1]

    if latin == True:
        if lastChar == "e":
            name[-1] = "u"
        elif lastChar == "E":
            name[-1] = "U"

    return "".join(name)

def vokativ(name, gender, latin=True):
    utils.check(name, gender, latin)
    name = name.strip()
    nameGenitiv = list(genitiv(name,gender,latin))
    name = list(name)
    nameSep = utils.separateLetters(name)

    if gender.lower() == "female" and name[-1].lower() != "a":
        return "".join(name)
    if name[-1].lower() in ["k","g","h"]:
        if nameGenitiv[-1].islower():
            nameGenitiv[-1] = "e"
            if nameGenitiv[-2].lower() in PALATALIZACIJA:
                if nameGenitiv[-2].islower():
                    nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()]
                else:
                    nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()].upper()
            return "".join(nameGenitiv)
        else:
            nameGenitiv[-1] = "E"
            if nameGenitiv[-2].lower() in PALATALIZACIJA:
                if nameGenitiv[-2].islower():
                    nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()]
                else:
                    nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()].upper()
            return "".join(nameGenitiv)
    
    if name[-1].lower() == "e":
        return "".join(name)
    
    if name[-1].lower() == "j":
        if nameGenitiv[-1].islower():
            nameGenitiv[-1] = "u"
        else:
            nameGenitiv[-1] = "U"
        return "".join(nameGenitiv)
    
    if name[-3].lower()+name[-2].lower()+name[-1].lower() == "ica":
        if name[-1].islower():
            name[-1] = "e"
        else:
            name[-1] = "E"
        return "".join(name)
    
    if name[-1].lower() == "o":
        return "".join(name)
    
    if name[-1].lower() == "i":
        return "".join(name)
    
    if name[-1].lower() == "u":
        return "".join(name)
    
    if name[-1].lower() in ["a","а"]:
        if len(nameSep) <= 5:
            try:
                if utils.isLatin(name[-1]):
                    return utils.toLatin(utils.vokativ_db[utils.toCyrillic(name)])
                else:
                    return utils.vokativ_db[utils.toCyrillic(name)]
            except KeyError:
                if name[-1].islower():
                    name[-1] = "o"
                else:
                    name[-1] = "O"
                return "".join(name)

    else:
        if name[-1].islower():
            nameGenitiv[-1] = "e"
        else:
            nameGenitiv[-1] = "E"
        return "".join(nameGenitiv)

    
    return "".join(name)

def instrumental(name, gender, latin=True):
    utils.check(name, gender, latin)
    name = name.strip()
    
    lastChar = name[-1]
    secToLastChar = name[-2]
    nameGenitiv = utils.separateLetters(genitiv(name, gender, latin))
    name = list(name)

    if latin == True:
        if gender.lower() == "female":
            if lastChar not in VOWELS:
                return "".join(name)

        nameGenitiv.pop(-1)

        if gender.lower() == "male" and utils.toCyrillic(nameGenitiv)[-1] in INSTRUMENTAL_LETTERS:
            if nameGenitiv[-2].lower() in ["i","e"]:
                if lastChar.isupper():
                    nameGenitiv.append("OM")
                    return "".join(nameGenitiv)
                else:
                    nameGenitiv.append("om")
                    return "".join(nameGenitiv)

            if lastChar.isupper():
                nameGenitiv.append("EM")
                return "".join(nameGenitiv)
            else:
                nameGenitiv.append("em")
                return "".join(nameGenitiv)

        if lastChar.isupper():
            nameGenitiv.append("OM")
        else:
            nameGenitiv.append("om")

    return "".join(nameGenitiv)


def lokativ(name, gender, latin=True):
    utils.check(name, gender, latin)
    return dativ(name, gender, latin)


def declineAll(name, gender, latin=True):
    utils.check(name, gender, latin)
    name = name.strip()

    allDek = {"nominativ": name, "genitiv": genitiv(name, gender, latin), "dativ": dativ(name, gender, latin), "akuzativ": akuzativ(
        name, gender, latin), "vokativ": vokativ(name, gender, latin), "instrumental": instrumental(name, gender, latin), "lokativ": lokativ(name, gender, latin)}

    return allDek

