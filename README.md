# deklinacija
A Python library for declension of personal names in Serbian, with support for both Cyrillic and Latin scripts.

## Installation
The source code is currently hosted on GitHub: [https://github.com/urelja/deklinacija](https://github.com/urelja/deklinacija)

The latest binary versions are hosted on the Python Package Index (PyPI): [https://pypi.org/project/deklinacija/](https://pypi.org/project/deklinacija/)
```properties
pip install deklinacija
```
## Usage
Simply `import` the package. It is recommended to set the alias to `dek`.

```python
import deklinacija as dek
```
**As of right now, only first names are supported.** To decline names, all you have to do is to call the appropriate function for the grammatical case you want to use, and specify the `name` and the `gender` parameter. The name parameter must be a `string`, can have either Latin or Cyrillic characters (automatically detected), and can contain uppercase or lowercase letters (the script respects the capitalisation of the name and will capitalise the added suffixes according to the last character's capitalisation, see `vokativ2` below).

The functions in this example return a `string`.
```python
import deklinacija as dek

genitiv = dek.genitiv("Velja","male") #Velje
dativ = dek.dativ("Петар","male") #Петру
akuzativ = dek.akuzativ("Jana","female") #Janu
vokativ = dek.vokativ("Predrag","male") #Predraže
vokativ2 = dek.vokativ("PREDRAG","male") #PREDRAŽE
instrumental = dek.instrumental("Uroš","male") #Urošem
instrumental2 = dek.instrumental("Вук","male") #Вуком
lokativ = dek.lokativ("Lana","female") #Lani

print(f"Zdravo, {vokativ}! Dobio si zahtev za prijateljstvo od {genitiv}.") 
#Zdravo Predraže! Dobio si zahtev za prijateljstvo od Velje.
#Translation: Hello Predrag! You have received a friend request from Velja.
```

You can also immediatelly decline a name through all grammatical cases by calling the `declineAll()` function.

The `declineAll()` function returns a `dictionary`, where keys are the grammatical cases.

```python
import deklinacija as dek

Nikola = dek.declineAll("Nikola","male") 
#{'nominativ': 'Nikola', 'genitiv': 'Nikole', 'dativ': 'Nikoli', 'akuzativ': 'Nikolu', 
#'vokativ':'Nikola', 'instrumental': 'Nikolom', 'lokativ': 'Nikoli'}

print("Dali ste poklon",Nikola['dativ']) 
#Dali ste poklon Nikoli
#Translation: You have given a gift to Nikola
```

## Todo
The following features are on the roadmap:
- Declension of last names
- Possessive forms


## Attribution
[Vokativi](https://github.com/startitrs/vokativi) by [Startit](https://github.com/startitrs) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) / Modifications: converted to Cyrillic and filtered out names longer than 4 characters
