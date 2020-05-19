import string
import numbers
class Person:

    name = ""
    surname = ""
    age = 0
#konstruktor klasy Person
    def __init__(self):
        self._name
        self._surname
        self._age
#właściwość sprawdzająca warunek z zadania oraz jeśli spełniony wprowadzająca imię
    @property
    def _name(self):
        name = input("Podaj imie")
        if (name, string.ascii_letters) and len(name) >= 3:
            self.__class__.name=name
        else:
            print("Podałeś zbyt krótkie imię !")
#właściwość sprawdzająca warunek z zadania oraz jeśli spełniony wprowadzająca nazwisko
    @property
    def _surname(self):
        surname = input("Podaj nazwisko")
        if (surname, string.ascii_letters) and len(surname) >= 3:
            self.__class__.surname = surname
        else:
            print("Podałeś zbyt krótkie nazwisko !")
#właściwość sprawdzająca warunek z zadania oraz jeśli spełniony wprowadzająca wiek
    @property
    def _age(self):
        age = int(input("Podaj wiek"))

        if (age, numbers.Integral) and 0 <= age <= 130:
            self.__class__.age = age
        else:
            print("Nie żyjesz !")
            self.__class__.age = 0
#funkcja wypisująca informacje o obiekcie klasy Person
    def __str__(self):
        return f"Imię:{self.__class__.name}\nNazwisko: {self.__class__.surname}\nWiek: {self.__class__.age}\n"




class Student(Person):
#atrybuty klasy Student, która dziedziczy po klasie Person
    field_of_study = ""

    student_book = {
    "Matematyka" : 0 ,
    "Informatyka" : 0,
    "Programowanie obiektowe" : 0
    }
#funkcja pozwalająca na wprowadzenie nazwy kierunku studiów za pomocą parametru
    def put_field_of_study(self,value):
         self._field_of_study = value
#funkcja pozwalająca wprowadzić do słownika oceny do wcześniej wprowadzonych przedmiotów
    def PutStudentGrades(self):

        for keys in self.student_book.keys():

            value=input("Podaj ocene do przedmiotu " + keys)
            self.student_book[keys] = value

#funkcja pozwalająca wypisać przedmioty oraz wprowadzone oceny
    def printStudentGrades(self):

        for keys,values in self.student_book.items():
            print(keys+" "+values)

#funkcja wypisująca informacje o obiekcie klasy Student
    def __str__(self):
        chain = ""
        for keys, values in self.student_book.items():
            chain = chain + keys +" "+values+"\n"

        return super().__str__() +f"kierunek studiów: {self._field_of_study}\n{chain}"

class Employee(Person):
#atrybuty klasy Employee, która dziedziczy po klasie Person
    job_title = ""
    skills = []
#funkcja pozwalajaca na wpisanie nazwy zawodu za pomocą parametru
    def set_job_title(self, title):
        self.job_title = title
#funkcja pozwalająca na wpisanie umiejętności do listy
    def set_skills(self):
        print("Podaj 3 umiejętności")
        for i in range(3):
            self.skills.append(input())
#funkcja pozwalająca na wypisanie nazwy zawodu
    def print_job_title(self):
        print("Nazwa zawodu "+self.job_title)
#funkcja pozwalająca wypisać umiejętności (całą listę)
    def print_skills(self):
        print("Lista umiejętności:")
        for i in range(3):
           print(self.skills[i], end=" ")
#funkcja wypisująca informacje o obiekcie klasy Employee
    def __str__(self):
        chain=' '.join(self.skills)

        return super().__str__()+f"nazwa zawodu : {self.job_title}\nLista umiejętności "+ chain+"\n"