alphabet = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'č': 'ч', 'ć': 'ћ', 'd': 'д', 'đ': 'ђ', 'dj': 'ђ', 'e': 'е', 'f': 'ф', 'g': 'г',
    'h': 'х', 'i': 'и', 'j': 'ј', 'k': 'к', 'l': 'л', 'lj': 'љ', 'm': 'м', 'n': 'н', 'nj': 'њ', 'o': 'о',
    'p': 'п', 'r': 'р', 's': 'с', 'š': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'z': 'з', 'ž': 'ж', 'dž': 'џ', 'dz': 'џ'}

latExceptions = []

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

def check(name,gender,latin):
    if type(name) != str or type(name) != str or type(gender) != str or type(latin) != bool:
        raise TypeError("name and gender params must be a string, param latin must be a boolean")
    
    gender = gender.strip()
    name = name.strip()

    if gender.lower() not in ["male","female"]:
        raise ValueError('gender param must be either "male" or "female"')

    if len(name) < 3:
        raise ValueError("name param must be at least 3 characters long")
    
