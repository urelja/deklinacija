import csv
import os

alphabet = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'č': 'ч', 'ć': 'ћ', 'd': 'д', 'đ': 'ђ', 'dj': 'ђ', 'e': 'е', 'f': 'ф', 'g': 'г',
    'h': 'х', 'i': 'и', 'j': 'ј', 'k': 'к', 'l': 'л', 'lj': 'љ', 'm': 'м', 'n': 'н', 'nj': 'њ', 'o': 'о',
    'p': 'п', 'r': 'р', 's': 'с', 'š': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'z': 'з', 'ž': 'ж', 'dž': 'џ', 'dz': 'џ'}

alphabet_latin = {
    'а': 'a', 'б': 'b', 'ц': 'c', 'ч': 'č', 'ћ': 'ć', 'д': 'd', 'ђ': 'đ', 'е': 'e', 'ф': 'f', 'г': 'g',
    'х': 'h', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'ш': 'š', 'т': 't', 'у': 'u', 'в': 'v', 'з': 'z', 'ж': 'ž', 'џ': 'dž'}

ZVUCNI = ["б", "д", "г", "ђ", "ж", "з", "џ"]

latExceptions = []


def isLatin(word):
    if word[-1].lower() in alphabet:
        return True
    elif word[-1].lower() in alphabet_latin:
        return False
    else:
        raise ValueError("word contains illegal characters")


def toCyrillic(word):

    wordArray = []
    word = list(word)
    wordText = "".join(word)

    if wordText.lower() not in latExceptions:
        n = 0
        while n <= (len(word)-1):

            if n == len(word)-1:
                wordArray.append(word[n])
                break

            if word[n] in ["d", "D", "l", "L", "n", "N"] and word[n+1] in ["j", "J"]:
                wordArray.append(word[n]+word[n+1])
                word.pop(n+1)
                n += 1
            elif word[n] in ["d", "D"] and word[n+1] in ["ž", "Ž", "z", "Z"]:
                wordArray.append(word[n]+word[n+1])
                word.pop(n+1)
                n += 1
            else:
                wordArray.append(word[n])
                n += 1
    else:
        n = 0
        for i in word:
            if i[0].isupper() == True:
                word[n] = alphabet[i.lower()].capitalize()
            else:
                word[n] = alphabet[i]
            n += 1

        return "".join(word)

    n = 0

    for i in wordArray:
        if i.lower() in alphabet:
            if i[0].isupper() == True:
                wordArray[n] = alphabet[i.lower()].capitalize()
            else:
                wordArray[n] = alphabet[i.lower()]
            n += 1
        else:
            wordArray[n] = i
            n += 1

    word = "".join(wordArray)

    return word


def toLatin(word):
    word = list(word)

    n = 0
    for i in word:
        if i.lower() in alphabet_latin:
            if i[0].isupper() and i.lower() in ['љ', 'њ', 'џ']:
                letter = alphabet_latin[i.lower()][0].upper(
                ) + alphabet_latin[i.lower()][1]
                word[n] = letter
            elif i[0].isupper():
                word[n] = alphabet_latin[i.lower()].upper()
            else:
                word[n] = alphabet_latin[i]

        else:
            word[n] = i
        n += 1

    return "".join(word)


def check(name, gender):
    if type(name) != str or type(gender) != str:
        raise TypeError(
            "name and gender params must be a string")

    name = name.strip()

    if gender.lower() not in ["male", "female"]:
        raise ValueError('gender param must be either "male" or "female"')

    if len(name) < 3:
        raise ValueError("name param must be at least 3 characters long")


def checkPosessive(name,gender,grammatical_number):
    if type(name) != str or type(gender) != str or type(grammatical_number) != str:
        raise TypeError(
            "all params must be strings")
    
    if gender.lower() not in ["male", "female"]:
        raise ValueError('gender param must be either "male" or "female"')
    
    if grammatical_number.lower() not in ["singular", "plural"]:
        raise ValueError('grammatical_number param must be either "singular" or "plural"')

    if len(name) < 3:
        raise ValueError("name param must be at least 3 characters long")
    
def separateLetters(word):
    word = list(word)
    wordText = "".join(word)
    wordArray = []

    n = 0
    while n <= (len(word)-1):

        if n == len(word)-1:
            wordArray.append(word[n])
            break

        if word[n] in ["d", "D", "l", "L", "n", "N"] and word[n+1] in ["j", "J"]:
            wordArray.append(word[n]+word[n+1])
            word.pop(n+1)
            n += 1
        elif word[n] in ["d", "D"] and word[n+1] in ["ž", "Ž", "z", "Z"]:
            wordArray.append(word[n]+word[n+1])
            word.pop(n+1)
            n += 1
        else:
            wordArray.append(word[n])
            n += 1

    return wordArray


def isZvucni(letter):
    if toCyrillic(letter.lower()) in ZVUCNI:
        return True
    else:
        return False

#Excel formula for filtering names shorter or equal to 5 characters and ending in cyrillic "а"
#(assumes that names start from the second row): 
# =FILTER(A2:B1970;(LEN(A2:A1970)<=5)*(RIGHT(A2:A1970)="а"))
#For converting the csv to cyrillic:
# with open('deklinacija/vokativ_database.csv',"r+",encoding="utf-8") as f:

#     reader = dict(csv.reader(f, delimiter=","))
#     converted = {}
#     text = ""

#     for (k,v) in reader.items():
#         kConverted = toCyrillic(k)
#         vConverted = toCyrillic(v)
#         text = text + kConverted + "," + vConverted + "\n"

#     f.truncate(0)
#     f.write(text)


def formatName(word):
    if type(word) == list:
        word = "".join(word).lower()
    word = list(word)
    word[0] = word[0].upper()
    return "".join(word)


module_path = os.path.abspath(__file__)

module_directory = os.path.dirname(module_path)

csv_file_path = os.path.join(module_directory, 'vokativ_database.csv')

with open(csv_file_path, "r", encoding="utf-8") as file:
    vokativ_db = dict(csv.reader(file, delimiter=";"))
