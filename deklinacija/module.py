import deklinacija.utils as utils

VOWELS = ["а","е","и","о","у"]  # used for identifying consonants

NEP_A = ["тар","ац","рај","рађ","рак","нак","ндар"] # the last and second to last characters in names ending in these characters switch places during declension
NEP_A_EXCEPT = [] # names which have one of the above suffixes but the last and the 2nd to last characters don't switch places during declension
INSTRUMENTAL_LETTERS = ["ј", "љ", "њ", "ђ", "ћ", "ч", "џ", "ш", "ж"]
PALATALIZACIJA = {"к": "ч", "г": "ж", "х": "ш", }


def genitiv(name, gender):
    utils.check(name, gender)
    nameList = name.split(" ")
    print(nameList)
    name = utils.separateLetters(name.strip())

    lastChar = name[-1]
    secToLastChar = name[-2]
    trdToLastChar = name[-3]
    
    lastThree = (name[-3]+name[-2]+name[-1]).lower()
    lastTwo = (name[-2]+name[-1]).lower()

    if lastChar.lower() in ["а","a"]:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                if secToLastChar.lower() in ["и","i"]:
                    name.insert(-1,"J")
                name[-1] = "E"
                return "".join(name)
            else:
                if secToLastChar.lower() in ["и","i"]:
                    name.insert(-1,"Ј")
                name[-1] = "Е"
                return "".join(name)
        else:
            if utils.isLatin(lastChar) == True:
                if secToLastChar.lower() in ["и","i"]:
                    name.insert(-1,"j")
                name[-1] = "e"
                return "".join(name)
            else:
                if secToLastChar.lower() in ["и","i"]:
                    name.insert(-1,"ј")
                name[-1] = "е"
                return "".join(name)

    if gender.lower() == "female":
        if lastChar.lower() not in ["а","a"]:
            return "".join(name)

    if gender.lower() == "male":
        if lastChar.lower() in ["е","e","о","o"]:
            if lastChar.isupper():
                if utils.isLatin(lastChar) == True:
                    if secToLastChar.lower() in ["и","i"]:
                        name.insert(-1,"J")
                    name[-1] = "A"
                    return "".join(name)
                else:
                    if secToLastChar.lower() in ["и","i"]:
                        name.insert(-1,"Ј")
                    name[-1] = "А"
                    return "".join(name)
            else:
                if utils.isLatin(lastChar) == True:
                    if secToLastChar.lower() in ["и","i"]:
                        name.insert(-1,"j")
                    name[-1] = "a"
                    return "".join(name)
                else:
                    if secToLastChar.lower() in ["и","i"]:
                        name.insert(-1,"ј")
                    name[-1] = "а"
                    return "".join(name)

        if lastChar.lower() in ["и","i"]:
            if lastChar.isupper():
                if utils.isLatin(lastChar) == True:
                    name.append("JA")
                    return "".join(name)
                else:
                    name.append("ЈА")
                    return "".join(name)
            else:
                if utils.isLatin(lastChar) == True:
                    name.append("ja")
                    return "".join(name)
                else:
                    name.append("ја")
                    return "".join(name)
        
        if len(name) < 4:
            lastFour = None
            
        else:
            lastFour = (name[-4]+name[-3]+name[-2]+name[-1]).lower()
            fthToLastChar = lastFour[-4]

        if len(name) >= 4 and (utils.toCyrillic(lastFour.lower()) in NEP_A or utils.toCyrillic(lastThree.lower()) in NEP_A or utils.toCyrillic(lastTwo.lower()) in NEP_A) and utils.toCyrillic(secToLastChar.lower()) == "а" and utils.toCyrillic(lastChar.lower()) not in VOWELS and utils.toCyrillic(trdToLastChar.lower()) not in VOWELS and utils.toCyrillic("".join(name).upper()) not in NEP_A_EXCEPT:
            if utils.toCyrillic(lastThree.lower()) != "ндар" and utils.toCyrillic(fthToLastChar.lower()) not in VOWELS:
                if lastChar.isupper():
                    if utils.isLatin(lastChar) == True:
                        name.append("A")
                    else:
                        name.append("А")
                else:
                    if utils.isLatin(lastChar) == True:
                        name.append("a")
                    else:
                        name.append("а")
            # nepostojano a
            elif name[-1].isupper():
                name[-2] = name[-1]
                if utils.isLatin(lastChar) == True:
                    name[-1] = "A"
                else:
                    name[-1] = "А"
            else:
                name[-2] = name[-1]
                if utils.isLatin(lastChar) == True:
                    name[-1] = "a"
                else:
                    name[-1] = "а"
        else:
            if lastChar.isupper():
                if utils.isLatin(lastChar) == True:
                    name.append("A")
                else:
                    name.append("А")
            else:
                if utils.isLatin(lastChar) == True:
                    name.append("a")
                else:
                    name.append("а")
    return "".join(name)


def dativ(name, gender):
    utils.check(name, gender)
    name = name.strip()
    name = list(genitiv(name, gender))

    lastChar = name[-1]
    secToLastChar = name[-2]
    trdToLastChar = name[-3]

    if lastChar.lower() in ["а","a"]:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                name[-1] = "U"
            else:
                name[-1] = "У"
        else:
            if utils.isLatin(lastChar) == True:
                name[-1] = "u"
            else:
                name[-1] = "у"
    elif lastChar.lower() in ["е","e"]:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                name[-1] = "I"
            else:
                name[-1] = "И"
        else:
            if utils.isLatin(lastChar) == True:
                name[-1] = "i"
            else:
                name[-1] = "и"

    return "".join(name)


def akuzativ(name, gender):
    utils.check(name, gender)
    name = name.strip()
    name = list(genitiv(name, gender))

    lastChar = name[-1]

    if lastChar.lower() in ["е","e"]:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                name[-1] = "U"
            else:
                name[-1] = "У"
        else:
            if utils.isLatin(lastChar) == True:
                name[-1] = "u"
            else:
                name[-1] = "у"

    return "".join(name)

def vokativ(name, gender):
    utils.check(name, gender)
    name = name.strip()
    nameGenitiv = list(genitiv(name,gender))
    name = list(name)
    nameSep = utils.separateLetters(name)
    rest = "".join(name[:-1])
    

    if gender.lower() == "female" and name[-1].lower() not in ["а","a"]:
        return "".join(name)
    
    if name[-2].lower()+name[-1].lower() in ["ia","иа"]:
        return "".join(name)

    if utils.toCyrillic(name[-1].lower()) in ["к","г","х"]:

        if nameGenitiv[-1].islower():
            if utils.isLatin(nameGenitiv[-1]) == True:
                nameGenitiv[-1] = "e"
            else:
                nameGenitiv[-1] = "е"
            
            if utils.isLatin(nameGenitiv[-2]) == True:
                nameGenitiv[-2] = utils.toLatin(PALATALIZACIJA[utils.toCyrillic(nameGenitiv[-2].lower())])
            else:
                nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()]
            
            return "".join(nameGenitiv)
        else:
            if utils.isLatin(nameGenitiv[-1]) == True:
                nameGenitiv[-1] = "E"
            else:
                nameGenitiv[-1] = "Е"

            if utils.isLatin(nameGenitiv[-2]) == True:    
                nameGenitiv[-2] = utils.toLatin(PALATALIZACIJA[utils.toCyrillic(nameGenitiv[-2].lower())].upper())
            else:
                nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()].upper()
            
            return "".join(nameGenitiv)
    
    if name[-1].lower() in ["j","ј"]:
        if nameGenitiv[-1].islower():
            if utils.isLatin(nameGenitiv[-1]) == True:
                nameGenitiv[-1] = "u"
            else:
                nameGenitiv[-1] = "у"
        else:
            if utils.isLatin(nameGenitiv[-1]) == True:
                nameGenitiv[-1] = "U"
            else:
                nameGenitiv[-1] = "У"
        return "".join(nameGenitiv)
    
    if utils.toCyrillic(name[-3].lower()+name[-2].lower()+name[-1].lower()).lower() in ["ица"]:
        if name[-1].islower():
            if utils.isLatin(nameGenitiv[-1]) == True:
                name[-1] = "e"
            else:
                name[-1] = "е"
        else:
            if utils.isLatin(nameGenitiv[-1]) == True:
                name[-1] = "E"
            else:
                name[-1] = "Е"
        return "".join(name)
    
    if utils.toCyrillic(name[-1].lower()) in ["о","и","у","е"]:
        return "".join(name)
    
    if name[-1].lower() in ["a","а"]:
        if len(nameSep) <= 5:
            try:
                if name[-1].isupper():
                    if utils.isLatin(name[-1]):
                        return rest+(utils.toLatin(utils.vokativ_db[utils.toCyrillic(utils.formatName(name))])[-1].upper())
                    else:
                        return rest+(utils.vokativ_db[utils.toCyrillic(utils.formatName(name))][-1].upper())
                else:
                    if utils.isLatin(name[-1]):
                        return rest+(utils.toLatin(utils.vokativ_db[utils.toCyrillic(utils.formatName(name))])[-1])
                    else:
                        return rest+(utils.vokativ_db[utils.toCyrillic(utils.formatName(name))][-1])
            except KeyError:
                if name[-1].islower():
                    if utils.isLatin(name[-1]):
                        if name[-2].lower() in ["и","i"]:
                            name.insert(-1,"j")
                        name[-1] = "o"
                    else:
                        if name[-2].lower() in ["и","i"]:
                            name.insert(-1,"ј")
                        name[-1] = "о"
                else:
                    if utils.isLatin(name[-1]):
                        if name[-2].lower() in ["и","i"]:
                            name.insert(-1,"J")
                        name[-1] = "O"
                    else:
                        if name[-2].lower() in ["и","i"]:
                            name.insert(-1,"Ј")
                        name[-1] = "О"
                return "".join(name)
    else:
        
        if name[-1].islower():
            if utils.isLatin(name[-1]):
                nameGenitiv[-1] = "e"
            else:
                nameGenitiv[-1] = "е"
        else:
            if utils.isLatin(name[-1]):
                nameGenitiv[-1] = "E"
            else:
                nameGenitiv[-1] = "Е"
        return "".join(nameGenitiv)

    
    return "".join(name)

def instrumental(name, gender):
    utils.check(name, gender)
    name = name.strip()
    
    lastChar = name[-1]
    secToLastChar = name[-2]
    nameGenitiv = utils.separateLetters(genitiv(name, gender))
    name = list(name)

    
    if gender.lower() == "female" and lastChar.lower() not in ["a","а"]:
        return "".join(name)

    nameGenitiv.pop(-1)

    if gender.lower() == "male" and utils.toCyrillic(nameGenitiv)[-1].lower() in INSTRUMENTAL_LETTERS and nameGenitiv[-2].lower() not in ["i","и","e","е"]:
        if lastChar.isupper():
            if utils.isLatin(lastChar):
                nameGenitiv.append("EM")
            else:
                nameGenitiv.append("ЕМ")
            return "".join(nameGenitiv)
        else:
            if utils.isLatin(lastChar):
                nameGenitiv.append("em")
            else:
                nameGenitiv.append("ем")
            return "".join(nameGenitiv)

    if lastChar.isupper():
        if utils.isLatin(lastChar):
            nameGenitiv.append("OM")
        else:
            nameGenitiv.append("ОМ")
        return "".join(nameGenitiv)
    
    else:
        if utils.isLatin(lastChar):
            nameGenitiv.append("om")
        else:
            nameGenitiv.append("ом")
        return "".join(nameGenitiv)


def lokativ(name, gender):
    utils.check(name, gender)
    return dativ(name, gender)


def declineAll(name, gender):
    utils.check(name, gender)
    name = name.strip()

    allDek = {"nominativ": name, "genitiv": genitiv(name, gender), "dativ": dativ(name, gender), "akuzativ": akuzativ(
        name, gender), "vokativ": vokativ(name, gender), "instrumental": instrumental(name, gender), "lokativ": lokativ(name, gender)}

    return allDek

