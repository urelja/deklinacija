# deklinacija
A Python library for grammatically correct declension (Serbian: deklinacija) of personal first and last names in Serbian, with support for both Cyrillic and Latin scripts, and even creation of possessive forms, with also a few useful tools for working with the Serbian language.

## Web Demo
You can easily try out this library's features on this web demo: https://deklinacija.pythonanywhere.com/

## Installation
The source code is currently hosted on GitHub: [https://github.com/urelja/deklinacija](https://github.com/urelja/deklinacija)

The latest binary versions are hosted on the Python Package Index (PyPI): [https://pypi.org/project/deklinacija/](https://pypi.org/project/deklinacija)
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
dativ = dek.dativ("Petar Petrović",Gender.MALE) #Petru Petroviću
vokativ = dek.vokativ("Predrag",Gender.MALE) #Predraže
vokativ2 = dek.vokativ("STEFAN JANKOVIĆ",Gender.MALE) #STEFANE JANKOVIĆU
instrumental = dek.instrumental("Uroš",Gender.MALE) #Urošem
lokativ = dek.lokativ("Beograd",Gender.FEMALE) #Beogradu

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

## Possessive Forms
As of version 1.6 you can now create possessive forms of a name. Aside from the name and the gender of the person, you also have to specify the gender of the possessed object and its grammatical number (singular/plural). In case the gender of the possessed object is unknown, you can just pass the object itself to the `object_gender` parameter and the program will figure out which gender it is, provided that the `grammatical_number` is set correctly (default value is Number.SINGULAR).

The functions in this example return a `string`.
```python
import deklinacija as dek
from deklinacija import Gender, Number

name = dek.possessive(name = "Stefan", gender = Gender.MALE, object_gender = Gender.FEMALE, grammatical_number = Number.SINGULAR)
name2 = dek.possessive(name = "Stefan", gender = Gender.MALE, object_gender = "grupa") #passing the object "group" instead of Gender.FEMALE, default grammatical_number value is Number.SINGULAR so it's not required to specify it in this case
name3 = dek.possessive(name = "Stefan", gender = Gender.MALE, object_gender = "slušalice", grammatical_number = Number.PLURAL) #passing the object "headphones"

print(name,"grupa") #Stefanova grupa // Translation: Stefan's group
print(name2,"grupa") #Stefanova grupa
print(name3,"slušalice") #Stefanove slušalice // Translation: Stefan's headphones
```

You can also immediately transform the name through all possible possessive forms (male, female, neutral in singular and plural) by calling the `possessiveAll()` function. Only the `name` and `gender` parameters are required.

The `possessiveAll()` function returns a `dictionary` where the keys are in the "GENDER_NUMBER" format.

```python
import deklinacija as dek
from deklinacija import Gender, Number

name = dek.possessiveAll("Stefan",Gender.MALE) #{'name': 'Stefan', 'male_singular': 'Stefanov', 'male_plural': 'Stefanovi', 'female_singular': 'Stefanova', 'female_plural': 'Stefanove', 'neutral_singular': 'Stefanovo', 'neutral_plural': 'Stefanova'}

print(name['male_plural'],"prijatelji") #Stefanovi prijatelji // Translation: Stefan's friends
```

## Implementing Into Your Application
In case you are not using Python in your backend and would like to utilise this library, the correct approach would be to create an API which you could call using any programming language you wish (like JavaScript) with a HTTP request. Here's an example of a simple HTTP JSON API built with [Flask](https://flask.palletsprojects.com/en/) that returns a JSON response:
```python
#To install Flask: pip install flask

from flask import Flask
import deklinacija as dek
from deklinacija import Gender, Number

app = Flask(__name__)

@app.route('/api/<name>/<gender>') #for declension
def api(name,gender):
    if gender == "male":
         gender = Gender.MALE
    elif gender == "female":
        gender = Gender.FEMALE
    result = dek.declineAll(name,gender)
    return result #returning a dictionary in Flask returns a JSON response

@app.route('/api/possessive/<name>/<gender>') #for possessive forms
def api2(name,gender):
    if gender == "male":
         gender = Gender.MALE
    elif gender == "female":
        gender = Gender.FEMALE
    result = dek.possessiveAll(name,gender)
    return result

app.run()
```

## Other Tools
This library makes extensive use of a few internal utilities that one may find useful when working with the Serbian language. These include:

`toLatin(word)`, `toCyrillic(word)`: Converts input string from Latin into Cyrillic and vice versa. Works with Serbian Latin letter pairs (lj, nj, dž, etc.)

`separateLetters(word)`: Separates letters from word, while making sure that certain letter pairs in Serbian Latin (lj, nj, dž etc.) stay together. Returns a list.

`isLatin(word)`: Returns a boolean indicating whether the last character of the input string is in the Latin script. Raises an error if the character isn't in neither Latin or Cyrillic.

## Todo
All promised features have been implemented. Feel free to suggest new features on the GitHub page.


## Attribution
[Vokativi](https://github.com/startitrs/vokativi) by [Startit](https://github.com/startitrs) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) / Modifications: converted into Cyrillic and filtered out names longer than 6 characters
