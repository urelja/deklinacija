# deklinacija
A Python library for grammatically correct declension (Serbian: deklinacija) of personal first and last names in Serbian, with support for both Cyrillic and Latin scripts, and even creation of posessive forms, with also a few useful tools for working with the Serbian language. Check out this web demo: https://deklinacija.pythonanywhere.com/

## Installation
The source code is currently hosted on GitHub: [https://github.com/urelja/deklinacija](https://github.com/urelja/deklinacija)

The latest binary versions are hosted on the Python Package Index (PyPI): [https://pypi.org/project/deklinacija/](https://pypi.org/project/deklinacija/)
```properties
pip install deklinacija
```
## Usage
Simply `import` the package and the `Gender` and `Number` enums. It is recommended to set the alias to `dek`.

```python
import deklinacija as dek
from deklinacija import Gender, Number
```
To decline names, all you have to do is to call the appropriate function for the grammatical case you want to use, and specify the `name` and the `gender` parameter. The name parameter must be a `string`, can have either Latin or Cyrillic characters (automatically detected), and can contain uppercase or lowercase letters (the script respects the capitalisation of the name and will capitalise the added suffixes according to the last character's capitalisation, see `vokativ2` below). You can also input a full name (with a first name and a last name, multiple last names are supported too, separated with a whitespace character) and the script will change the name accordingly. 

The functions in this example return a `string`.
```python
import deklinacija as dek
from deklinacija import Gender, Number

genitiv = dek.genitiv("Velja",Gender.MALE) #Velje
vokativ = dek.vokativ("Predrag",Gender.MALE) #Predraže
vokativ2 = dek.vokativ("PREDRAG JANKOVIĆ",Gender.MALE) #PREDRAŽE JANKOVIĆU
instrumental = dek.instrumental("Uroš",Gender.MALE) #Urošem
lokativ = dek.lokativ("Lana Petrović",Gender.FEMALE) #Lani Petrović

print(f"Zdravo, {vokativ}! Dobio si zahtev za prijateljstvo od {genitiv}.") 
#Zdravo Predraže! Dobio si zahtev za prijateljstvo od Velje. // Translation: Hello Predrag! You have received a friend request from Velja.
```

You can also immediatelly decline a name through all grammatical cases by calling the `declineAll()` function.

The `declineAll()` function returns a `dictionary`, where the keys are the grammatical cases.

```python
import deklinacija as dek
from deklinacija import Gender, Number

name = dek.declineAll("Nikola",Gender.MALE) 
#{'nominativ': 'Nikola', 'genitiv': 'Nikole', 'dativ': 'Nikoli', 'akuzativ': 'Nikolu', 
#'vokativ':'Nikola', 'instrumental': 'Nikolom', 'lokativ': 'Nikoli'}

print("Dali ste poklon",name['dativ']) 
#Dali ste poklon Nikoli // Translation: You have given a gift to Nikola
```

## Posessive Forms
As of version 1.6 there is a new feature: posessive forms. Aside from the name and the gender of the person, you also have to specify the gender of the posessed object and its grammatical number. In case the gender of the posessed object is unknown, you can just pass the object itself to the `object_gender` parameter and the program will figure out which gender it is, provided that the `grammatical_number` is set correctly (default value is Number.SINGULAR).

The functions in this example return a `string`.
```python
import deklinacija as dek
from deklinacija import Gender, Number

name = dek.posessive(name = "Stefan", gender = Gender.MALE, object_gender = Gender.FEMALE, grammatical_number = Number.SINGULAR)
name2 = dek.posessive(name = "Stefan", gender = Gender.MALE, object_gender = "grupa") #passing the object "group" instead of Gender.FEMALE, default grammatical_number value is Number.SINGULAR so it's not required to specify it in this case
name3 = dek.posessive(name = "Stefan", gender = Gender.MALE, object_gender = "slušalice", grammatical_number = Number.PLURAL) #passing the object "headphones"

print(name,"grupa") #Stefanova grupa // Translation: Stefan's group
print(name2,"grupa") #Stefanova grupa
print(name3,"slušalice") #Stefanove slušalice // Translation: Stefan's headphones
```

You can also immediately transform the name through all possible posessive forms (male, female, neutral in singular and plural) by calling the `posessiveAll()` function. Only the `name` and `gender` parameters are required.

The `posessiveAll()` function returns a `dictionary` where the keys are in the "GENDER_NUMBER" format.

```python
import deklinacija as dek
from deklinacija import Gender, Number

name = dek.posessiveAll("Stefan",Gender.MALE) #{'name': 'Stefan', 'male_singular': 'Stefanov', 'male_plural': 'Stefanovi', 'female_singular': 'Stefanova', 'female_plural': 'Stefanove', 'neutral_singular': 'Stefanovo', 'neutral_plural': 'Stefanova'}

print(name['male_plural'],"prijatelji") #Stefanovi prijatelji // Translation: Stefan's friends
```
## Other tools
This library makes extensive use of a few internal utilities that one may find useful when working with the Serbian language. These include:

`toLatin(word)`, `toCyrillic(word)`: Converts input string from Latin into Cyrillic and vice versa. Works with Serbian Latin letter pairs (lj, nj, dž, etc.)

`separateLetters(word)`: Separates letters from word, while making sure that certain letter pairs in Serbian Latin (lj, nj, dž etc.) stay together. Returns a list.

`isLatin(word)`: Returns a boolean indicating whether the last character of the input string is in the Latin script. Raises an error if the character isn't in neither Latin or Cyrillic.

## Todo
All promised features have been implemented. All that is left is code cleanup. Feel free to suggest new features on the GitHub page.


## Attribution
[Vokativi](https://github.com/startitrs/vokativi) by [Startit](https://github.com/startitrs) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) / Modifications: converted into Cyrillic and filtered out names longer than 6 characters
