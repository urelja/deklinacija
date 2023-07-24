import deklinacija.utils as utils
from deklinacija.utils import Gender, Number

VOWELS = ["а", "е", "и", "о", "у"]  # used for identifying consonants

# the last and second to last characters in names ending in these characters switch places during declension
NEP_A = ["тар", "ац", "рај", "рађ", "рак", "нак", "ндар", "чак"]
NEP_A_EXCEPT = []  # names which have one of the above suffixes but the last and the 2nd to last characters don't switch places during declension
J_EXCEPTION = ['МИА']
ZADNJONEPCANI = ["ј", "љ", "њ", "ђ", "ћ", "ч", "џ", "ш", "ж"]
PALATALIZACIJA = {"к": "ч", "г": "ж", "х": "ш", }
POSSESIVE_SUFFIXES = {"male_singular":"","male_plural":"и","female_singular":"а","female_plural":"е","neutral_singular":"о","neutral_plural":"а"}
MALE_EXCEPTIONS = ["тата","газда","судија","ага"]
FEMALE_EXCEPTIONS = ["пећ","чађ","кћер","ствар","љубав","радост"]

def genitiv(name, gender):
    """
    OD KOGA, OD ČEGA? FROM WHOM?

    Returns the genitive form of the provided name. If a last name is present, it must be separated with a whitespace.
    
    Context in a sentence:
    "Dobili ste zahtev za prijateljstvo od Petra."
    Translation:
    "You've received a friend request from Peter."

    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    name = name.strip()
    fullName = name.split()
    returnName = []

    for i in fullName:
        changedName = __genitiv(i, gender)
        returnName.append(changedName)

    return " ".join(returnName)

def dativ(name, gender):
    """
    KOME, ČEMU? TO WHOM?

    Returns the dative form of the provided name. If a last name is present, it must be separated with a whitespace.
    
    Context in a sentence:
    "Poslali ste zahtev za prijateljstvo Petru."
    "Diploma Petru Petroviću"
    Translation:
    "You've sent a friend request to Peter."
    "Diploma to Peter Petrović"
    
    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    utils.check(name, gender)
    name = name.strip()
    fullName = name.split()
    returnName = []

    n = 0
    for i in fullName:
        if n == 0: 
            changedName = __dativ(i, gender,False)
            n += 1
        else:
            changedName = __dativ(i, gender,True)
        returnName.append(changedName)

    return " ".join(returnName)

def akuzativ(name, gender):
    """
    (VIDIM) KOGA, ŠTA? (I SEE) WHOM?

    Returns the accusative form of the provided name. If a last name is present, it must be separated with a whitespace.
    
    Context in a sentence:
    "Kontaktirali ste Janu."
    Translation:
    "You've contacted Jana."

    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    utils.check(name, gender)
    name = name.strip()
    fullName = name.split()
    returnName = []

    for i in fullName:
        changedName = __akuzativ(i, gender)
        returnName.append(changedName)

    return " ".join(returnName)

def vokativ(name, gender):
    """
    Hej! Hey!

    Returns the vocative form of the provided name. If a last name is present, it must be separated with a whitespace. Used for greetings.
    
    Context in a sentence:
    "Zdravo Petre!"
    Translation:
    "Hello Peter!"

    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    utils.check(name, gender)
    name = name.strip()
    fullName = name.split()
    returnName = []
    n = 0
    for i in fullName:
        if n == 0: 
            changedName = __vokativ(i, gender,False)
            n += 1
        else:
            changedName = __vokativ(i, gender,True)
        returnName.append(changedName)

    return " ".join(returnName)

def instrumental(name, gender):
    """
    S KIM? ČIM? WITH WHOM? WITH WHAT?

    Returns the instrumental form of the provided name. If a last name is present, it must be separated with a whitespace.
    
    Context in a sentence:
    "Veljko je trenutno u igri sa Milošem."
    Translation:
    "Veljko is currently in-game with Miloš."

    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    utils.check(name, gender)
    name = name.strip()
    fullName = name.split()
    returnName = []

    for i in fullName:
        changedName = __instrumental(i, gender)
        returnName.append(changedName)

    return " ".join(returnName)

def lokativ(name, gender):
    """
    O KOME? O ČEMU? NA KOJOJ LOKACIJI? ABOUT WHO? ABOUT WHAT? IN WHAT LOCATION?

    Returns the locative form of the provided name. If a last name is present, it must be separated with a whitespace.
    
    Context in a sentence:
    "Marko je trenutno u Beogradu."
    Translation:
    "Marko is currently in Belgrade."

    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    utils.check(name, gender)
    name = name.strip()
    fullName = name.split()
    returnName = []
    n = 0
    for i in fullName:
        if n == 0: 
            changedName = __dativ(i, gender,False)
            n += 1
        else:
            changedName = __dativ(i, gender,True)
        returnName.append(changedName)

    return " ".join(returnName)

def possesive(name,gender,object_gender,grammatical_number=Number.SINGULAR):
    """
    ČIJI? WHOSE?

    Returns the possesive form of the provided name. Depends on the object_gender and grammatical_number parameters to add the appropriate suffix to the name.
    
    Parameters:
    name: The name of the person that posseses something
    gender: The gender of the person that posesses something, param value must be either Gender.MALE or Gender.FEMALE
    object_gender: Can either be the gender of the object that the person posesses (value must be Gender.MALE, Gender.FEMALE or Gender.NEUTRAL) or the object itself, in which case the gender will be automatically detected provided that the grammatical_number param is correct
    grammatical_number: The grammatical number of the object that the person posesses. Param value must be either Number.SINGULAR or Number.PLURAL. Default: singular
    """
    utils.checkPosessive(name,gender,object_gender,grammatical_number,)


    if type(object_gender) == str:
        object_gender = utils.toCyrillic(object_gender.strip().lower())
        if object_gender[-1] == "е":
            if grammatical_number == Number.SINGULAR:
                object_gender = Gender.NEUTRAL
            else:
                object_gender = Gender.FEMALE
        elif object_gender[-1] == "а":
            if object_gender in MALE_EXCEPTIONS:
                object_gender = Gender.MALE
            else:
                object_gender = Gender.FEMALE
        elif object_gender[-1] == "и" and grammatical_number == Number.PLURAL:
            test = object_gender[:-1]
            if test in FEMALE_EXCEPTIONS:
                object_gender = Gender.FEMALE
            else:
                object_gender = Gender.MALE
        else:
            if object_gender in FEMALE_EXCEPTIONS:
                object_gender = Gender.FEMALE
            else:
                object_gender = Gender.MALE
    
    name = name.strip()

    gender_text = object_gender.value
    number_text = grammatical_number.value

    lastChar = name[-1]
    if lastChar.isupper():
        if utils.isLatin(lastChar) == True:
            suffix = utils.toLatin(POSSESIVE_SUFFIXES[gender_text+"_"+number_text]).upper()
        else:
            suffix = POSSESIVE_SUFFIXES[gender_text+"_"+number_text].upper()
    else:
        if utils.isLatin(lastChar) == True:
            suffix = utils.toLatin(POSSESIVE_SUFFIXES[gender_text+"_"+number_text])
        else:
            suffix = POSSESIVE_SUFFIXES[gender_text+"_"+number_text]
    return __possesive(name,gender)+suffix

def posessiveAll(name,gender):
    """
    Creates all possible posessive forms (male, female and neutral in plural and singular) of the provided name and returns a dictionary where the keys are in the "GENDER_NUMBER" format.

    Parameters:
    name: The name that should be transformed
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    utils.check(name, gender)
    name = name.strip()
    
    return {"name":name,"male_singular":possesive(name,gender,Gender.MALE,Number.SINGULAR),"male_plural":possesive(name,gender,Gender.MALE,Number.PLURAL),"female_singular":possesive(name,gender,Gender.FEMALE,Number.SINGULAR),"female_plural":possesive(name,gender,Gender.FEMALE,Number.PLURAL),"neutral_singular":possesive(name,gender,Gender.NEUTRAL,Number.SINGULAR),"neutral_plural":possesive(name,gender,Gender.NEUTRAL,Number.PLURAL)}

def __possesive(name,gender):
    utils.check(name, gender)
    name = utils.separateLetters(__genitiv(name.strip(),gender))
    lastChar = name[-1]
    secToLastChar = name[-2]
    lastThree = "".join(name[-3:])
    lastTwo = "".join(name[-2:])

    if gender == Gender.FEMALE and utils.toCyrillic(name[-1].lower()) not in ['е','e']:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                if utils.toCyrillic(lastChar.lower()) in ['и','i']:
                    name[-1] = "IJIN"
                    return "".join(name)

                name.append("IN")
                return "".join(name)
            else:
                if utils.toCyrillic(lastChar.lower()) in ['и','i']:
                    name[-1] = "ИЈИН"
                    return "".join(name)
                
                name.append("ИН")
                return "".join(name)
        else:
            if utils.isLatin(lastChar) == True:
                if utils.toCyrillic(lastChar.lower()) in ['и','i']:
                    name[-1] = "ijin"
                    return "".join(name)
                if lastThree.lower() == 'ice':
                    name[-2] = "č"

                name.append("in")
                return "".join(name)
            else:
                if utils.toCyrillic(lastChar.lower()) in ['и','i']:
                    name[-1] = "ијин"
                    return "".join(name)

                name.append("ин")
                return "".join(name)
            
    if name[-1].lower() in ['е','e']:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                if utils.toCyrillic(lastChar.lower()) in ['и','i'] or utils.toCyrillic(name[-2].lower()) in ['и','i']:
                    if utils.toCyrillic(name[-2].lower()) in ['и','i']:
                        name.pop()
                    name.append("JIN")
                    return "".join(name)
                elif utils.toCyrillic(lastThree.lower()) == 'ице':
                    name[-2] = "Č"

                name[-1] = "IN"
                return "".join(name)
            else:
                if utils.toCyrillic(lastChar.lower()) in ['и','i'] or utils.toCyrillic(name[-2].lower()) in ['и','i']:
                    if utils.toCyrillic(name[-2].lower()) in ['и','i']:
                        name.pop()
                    name.append("ЈИН")
                    return "".join(name)
                elif utils.toCyrillic(lastThree.lower()) == 'ице':
                    name[-2] = "Ч"
                
                name[-1] = "ИН"
                return "".join(name)
        else:
            if utils.isLatin(lastChar) == True:
                if utils.toCyrillic(lastChar.lower()) in ['и','i'] or utils.toCyrillic(name[-2].lower()) in ['и','i']:
                    if utils.toCyrillic(name[-2].lower()) in ['и','i']:
                        name.pop()
                    name.append("jin")
                    return "".join(name)
                if utils.toCyrillic(lastThree.lower()) == 'ице':
                    name[-2] = "č"

                name[-1] = "in"
                return "".join(name)
            else:
                if utils.toCyrillic(lastChar.lower()) in ['и','i'] or utils.toCyrillic(name[-2].lower()) in ['и','i']:
                    if utils.toCyrillic(name[-2].lower()) in ['и','i']:
                        name.pop()
                    name.append("јин")
                    return "".join(name)
                elif utils.toCyrillic(lastThree.lower()) == 'ице':
                    name[-2] = "ч"

                name[-1] = "ин"
                return "".join(name)
    
    if name[-1].lower() in ['а','a','г','g']:
        if lastChar.isupper():
            if utils.isLatin(lastChar) == True:
                if utils.toCyrillic(secToLastChar.lower()) in ZADNJONEPCANI:
                    name[-1] = "EV"
                    return "".join(name)
                if utils.toCyrillic(lastTwo.lower()) == "ог":
                    name = name[:-1]

                name[-1] = "OV"
                return "".join(name)
            else:
                if utils.toCyrillic(secToLastChar.lower()) in ZADNJONEPCANI:
                    name[-1] = "ЕВ"
                    return "".join(name)
                
                name[-1] = "ОВ"
                return "".join(name)
        else:
            if utils.isLatin(lastChar) == True:
                if utils.toCyrillic(secToLastChar.lower()) in ZADNJONEPCANI:
                    name[-1] = "ev"
                    return "".join(name)
                if utils.toCyrillic(lastTwo.lower()) == "ог":
                    name = name[:-1]
                
                name[-1] = "ov"
                return "".join(name)
            else:
                if utils.toCyrillic(secToLastChar.lower()) in ZADNJONEPCANI:
                    name[-1] = "ев"
                    return "".join(name)
                if utils.toCyrillic(lastTwo.lower()) == "ог":
                    name = name[:-1]
                
                name[-1] = "ов"
                return "".join(name)
    
def __genitiv(name, gender):
    #utils.check(name, gender)
    name = utils.separateLetters(name.strip())

    lastChar = name[-1]
    secToLastChar = name[-2]
    trdToLastChar = name[-3]

    lastThree = "".join(name[-3:]).lower()
    lastTwo = "".join(name[-2:]).lower()

    if gender == Gender.FEMALE:
        if lastChar.lower() not in ["а", "a"]:
            return "".join(name)

    if lastChar.lower() in ["а", "a"]:
        if utils.toCyrillic("".join(name).upper()) in J_EXCEPTION:
            return utils.addSuffix(name,gender,"e",False,False)
        return utils.addSuffix(name,gender,"e",False,True)

    if lastChar.lower() in ["е", "e", "о", "o"]:
        return utils.addSuffix(name,gender,"a",False,True)

    if utils.toCyrillic(lastThree.lower()) in ["ски", "чки", "шки"] and len(name) > 3:
        return utils.addSuffix(name,gender,"og",False,False)

    if lastChar.lower() in ["и", "i"]:
        return utils.addSuffix(name,gender,"ja",True,False)

    if len(name) < 4:
        lastFour = None

    else:
        lastFour = "".join(name[-4:]).lower()
        fthToLastChar = name[-4]

    if len(name) >= 4 and (utils.toCyrillic(lastFour.lower()) in NEP_A or utils.toCyrillic(lastThree.lower()) in NEP_A or utils.toCyrillic(lastTwo.lower()) in NEP_A) and utils.toCyrillic(secToLastChar.lower()) == "а" and utils.toCyrillic(lastChar.lower()) not in VOWELS and utils.toCyrillic(trdToLastChar.lower()) not in VOWELS and utils.toCyrillic("".join(name).upper()) not in NEP_A_EXCEPT:
        if utils.toCyrillic(lastFour.lower()) != "ндар" and utils.toCyrillic(fthToLastChar.lower()) not in VOWELS:
            return utils.addSuffix(name,gender,"a",True,False)
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
        return utils.addSuffix(name,gender,"a",True,False)
    return "".join(name)

def __dativ(name, gender, last_name):
    utils.check(name, gender)
    ogName = utils.separateLetters(name)
    name = utils.separateLetters(genitiv(name, gender).strip())

    lastThree = "".join(ogName[-3:])
    lastTwo = "".join(ogName[-2:])
    lastChar = name[-1]

    if last_name == True and (utils.toCyrillic(lastThree.lower()) in ["ева","ова"] or utils.toCyrillic(lastTwo.lower()) == "ка") and len(ogName) > 3 and gender == Gender.FEMALE:
        return utils.addSuffix(ogName,gender,"oj",False,False)

    if utils.toCyrillic(lastThree.lower()) in ["ски", "чки", "шки"] and len(ogName) > 3 and gender == Gender.MALE:
        return utils.addSuffix(ogName,gender,"om",False,False)

    if lastChar.lower() in ["а", "a"]:
        return utils.addSuffix(name,gender,"u",False,False)
    
    elif lastChar.lower() in ["е", "e"]:
        return utils.addSuffix(name,gender,"i",False,True)

    return "".join(name)

def __akuzativ(name, gender):
    utils.check(name, gender)
    ogName = list(name)
    name = utils.separateLetters(genitiv(name, gender).strip())
    lastThree = "".join(name[-3:]).lower()

    lastChar = name[-1]

    if lastChar.lower() in ["е", "e"]:
        return utils.addSuffix(name,gender,"u",False,False)

    return "".join(name)

def __vokativ(name, gender, last_name):
    utils.check(name, gender)
    nameGenitiv = utils.separateLetters(genitiv(name, gender))
    name = utils.separateLetters(name.strip())
    rest = "".join(name[:-1])

    if (gender == Gender.FEMALE and name[-1].lower() not in ["а", "a"]) or "".join(name[-2:]) in ["ia", "иа"] or utils.toCyrillic(name[-1].lower()) in ["о", "и", "у", "е"]:
        return "".join(name)

    if (utils.toCyrillic(name[-1].lower()) in ["к", "ц"] and (utils.toCyrillic("".join(name[-3:]).lower()) in NEP_A or utils.toCyrillic("".join(name[-2:]).lower()) in NEP_A or last_name == True)) or utils.toCyrillic(name[-1].lower()) in ZADNJONEPCANI:
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
        return utils.addSuffix(nameGenitiv,gender,"u",False,False)

    if utils.toCyrillic(name[-1].lower()) != "а":
        if nameGenitiv[-1].islower():
            if utils.isLatin(nameGenitiv[-1]) == True:
                nameGenitiv[-1] = "e"
            else:
                nameGenitiv[-1] = "е"
            
            if utils.toCyrillic(name[-1].lower()) in ["к", "г", "х"]:
                if utils.isLatin(nameGenitiv[-2]) == True:
                    nameGenitiv[-2] = utils.toLatin(
                        PALATALIZACIJA[utils.toCyrillic(nameGenitiv[-2].lower())])
                else:
                    nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()]

            return "".join(nameGenitiv)
        else:
            if utils.isLatin(nameGenitiv[-1]) == True:
                nameGenitiv[-1] = "E"
            else:
                nameGenitiv[-1] = "Е"
            
            if utils.toCyrillic(name[-1].lower()) in ["к", "г", "х"]:
                if utils.isLatin(nameGenitiv[-2]) == True:
                    nameGenitiv[-2] = utils.toLatin(
                        PALATALIZACIJA[utils.toCyrillic(nameGenitiv[-2].lower())].upper())
                else:
                    nameGenitiv[-2] = PALATALIZACIJA[nameGenitiv[-2].lower()].upper()

            return "".join(nameGenitiv)

    if utils.toCyrillic(name[-3].lower()+name[-2].lower()+name[-1].lower()).lower() in ["ица"] and len(name) > 5:
        return utils.addSuffix(nameGenitiv,gender,"e",False,False)

    if name[-1].lower() in ["a", "а"]:
        if len(name) <= 6:
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
                if len(name) == 6:
                    return "".join(name)
                return utils.addSuffix(name,gender,"o",False,False)
    return "".join(name)

def __instrumental(name, gender):
    utils.check(name, gender)
    nameGenitiv = utils.separateLetters(genitiv(name, gender))
    name = utils.separateLetters(name.strip())

    lastChar = name[-1]
    lastThree = "".join(name[-3:]).lower()

    if gender == Gender.FEMALE and lastChar.lower() not in ["a", "а"]:
        return "".join(name)

    if utils.toCyrillic(lastThree.lower()) in ["ски", "чки", "шки"] and len(name) > 3 and gender == Gender.MALE:
        nameGenitiv.pop(-1)
        return utils.addSuffix(nameGenitiv,gender,"im",False,False)

    if gender == Gender.MALE and utils.toCyrillic(nameGenitiv)[-2].lower() in ZADNJONEPCANI and lastChar.lower() not in ['а','a']:
        return utils.addSuffix(nameGenitiv,gender,"em",False,False)
    else:
        return utils.addSuffix(nameGenitiv,gender,"om",False,True)

def __lokativ(name, gender):
    utils.check(name, gender)
    return dativ(name, gender)

def declineAll(name, gender):
    """
    Declines a name through all 7 grammatical cases and returns a dictionary where each case is a key.

    Parameters:
    name: The name that should be declined
    gender: The gender of the person, param value must be either Gender.MALE or Gender.FEMALE
    """
    #utils.check(name, gender)
    name = name.strip()

    allDek = {"nominativ": name, "genitiv": genitiv(name, gender), "dativ": dativ(name, gender), "akuzativ": akuzativ(
        name, gender), "vokativ": vokativ(name, gender), "instrumental": instrumental(name, gender), "lokativ": lokativ(name, gender)}

    return allDek
