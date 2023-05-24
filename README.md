# deklinacija
A Python library for declension of personal names in Serbian. The  grammatical rules utlized in this library also apply to Croatian and Bosnian.

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
**As of right now, only first names are supported.** To decline names, all you have to do is to call the appropriate function for the grammatical case you want to use, and specify the `name` and the `gender` parameter. There is also the third `latin` parameter, which indicates whether the provided `name` parameter is written in the Cyrillic or Latin script. **Currently, only the Latin script is supported.**

The functions in this example return a `string`.
```python
import deklinacija as dek

genitiv = dek.genitiv("Velja","male") #Velje
dativ = dek.dativ("Petar","male") #Petru
akuzativ = dek.akuzativ("Jana","female") #Janu
vokativ = dek.vokativ("Predrag","male") #Predraže
instrumental = dek.instrumental("Uroš","male") #Urošem
instrumental2 = dek.instrumental("Vuk","male") #Vukom
lokativ = dek.lokativ("Lana","female") #Lani

print(f"Zdravo, {vokativ}! Dobio si zahtev za prijateljstvo od {genitiv}.") 
#Zdravo Predraže! Dobio si zahtev za prijateljstvo od Velje.
#Translation: Hello Predrag! You have received a friend request from Velja.
```

You can also immediatelly decline a name through all grammatical cases by calling the `declineAll()` function.

The `declineAll()` function returns a `dictionary`.

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
- Support for both Latin and Cyrillic scripts
- Declension of last names

## Attribution
[Vokativi](https://github.com/startitrs/vokativi) by [Startit](https://github.com/startitrs) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) / Modifications: converted to Cyrillic and filtered out names longer than 4 characters
