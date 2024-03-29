#How to use: python -m pytest
import deklinacija as dek
import ast
import os

namesMale = ["Predrag","Minja","Relja","Uroš","Petrović","Petar","Mačak","Božidar","Đurađ","Djuradj","Miki","Dario","Čuperak","Đorđe","Djordje","Pablo","Juraj","Aleksandar","Opanak","Vlah","Subotički","Niški","Srpski","Dario Subotički","Minja Niški","Miki Srpski"]
namesFemale = ["Jana","Milica","Mia","Ines","Tea","Ina","Petrović","Daria","Anžujska","Subotički","Petka","Lana Petrović","Sandra Anžujska","Milica Tabova","Milica Releva"]

module_path = os.path.abspath(__file__)
module_directory = os.path.dirname(module_path)
file_path_male = os.path.join(module_directory, 'names_male.txt')
file_path_female = os.path.join(module_directory, 'names_female.txt')
file_path_male_p = os.path.join(module_directory, 'names_male_possessive.txt')
file_path_female_p = os.path.join(module_directory, 'names_female_possessive.txt')

with open(file_path_male, "r", encoding="utf-8") as fileM:
    read_content_male = fileM.readlines()

with open(file_path_female, "r", encoding="utf-8") as fileF:
    read_content_female = fileF.readlines()

with open(file_path_male_p, "r", encoding="utf-8") as fileMP:
    read_content_male_p = fileMP.readlines()

with open(file_path_female_p, "r", encoding="utf-8") as fileFP:
    read_content_female_p = fileFP.readlines()

def testMaleNames():
    n = 0
    for i in read_content_male:
        nameDict = ast.literal_eval(read_content_male[n].strip())
        name = nameDict['nominativ']
        compare = dek.declineAll(name,dek.Gender.MALE)
        assert compare == nameDict
        n += 1

def testFemaleNames():
    n = 0
    for i in read_content_female:
        nameDict = ast.literal_eval(read_content_female[n].strip())
        name = nameDict['nominativ']
        compare = dek.declineAll(name,dek.Gender.FEMALE)
        assert compare == nameDict
        n += 1

def testPossessiveMaleNames():
    n = 0
    for i in read_content_male_p:
        nameDict = ast.literal_eval(read_content_male_p[n].strip())
        name = nameDict['name']
        compare = dek.possessiveAll(name,dek.Gender.MALE)
        assert compare == nameDict
        n += 1

def testPossessiveFemaleNames():
    n = 0
    for i in read_content_female_p:
        nameDict = ast.literal_eval(read_content_female_p[n].strip())
        name = nameDict['name']
        compare = dek.possessiveAll(name,dek.Gender.FEMALE)
        assert compare == nameDict
        n += 1