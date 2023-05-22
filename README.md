# deklinacija-imena
A Python library for declension of personal names in Serbian. The  grammatical rules utlized in this library likely also apply to Croatian and Bosnian.

## Usage
Simply `import` the package. It is recommended to set the alias to `dek`.

```python
import deklinacija as dek
```
**As of right now, only first names are supported.** To decline names, all you have to do is to call the appropriate function for the grammatical case you want to use, and specify the `name` and the `gender` parameter. There is also the third `latin` parameter, which indicates whether the provided `name` parameter is written in the Cyrillic or Latin script. **Currently, only the Latin script is supported.**

The functions in this example return a `string`.
```python
import deklinacija as dek

changedName1 = dek.genitiv("Velja","male") #Velje
changedName2 = dek.dativ("Petar","male") #Petru
changedName3 = dek.akuzativ("Jana","female") #Janu
changedName4 = dek.instrumental("Uroš","male") #Urošem
changedName5 = dek.instrumental("Vuk","male") #Vukom
changedName6 = dek.lokativ("Lana","female") #Lani

print("Dobili ste zahtev za prijateljstvo od",changedName1) #Dobili ste zahtev za prijateljstvo od Velje - Translation: You have received a friend request from Velja
```

You can also immediatelly decline a name through all grammatical cases by calling the `declineAll()` function.

The `declineAll()` function returns a `dictionary`.

```python
import deklinacija as dek

Nikola = dek.declineAll("Nikola","male") #{'nominativ': 'Nikola', 'genitiv': 'Nikole', 'dativ': 'Nikoli', 'akuzativ': 'Nikolu', 'instrumental': 'Nikolom', 'lokativ': 'Nikoli'}

print("Dali ste poklon",Nikola['dativ']) #Dali ste poklon Nikoli - Translation: You have given a gift to Nikola
```

## Todo
The following features are on the roadmap:
- The vocative case
- Support for both Latin and Cyrillic scripts
- Declension of last names
