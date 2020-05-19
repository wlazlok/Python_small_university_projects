class Pupil:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if len(name) >= 3:
            self.__name = name
        else:
            print("Zbyt krótkie imie!")
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        if len(surname) >= 3:
            self.__surname = surname
        else:
            print("Zbyt krótkie nazwisko")


    def complete_marks(self, subject, mark):
        if 1 <= mark <= 6:
            self.marks[subject] = mark
        else:
            print("Ocena poza zakresem")

    def print_marks(self):
        print(self.marks)

    def mean(self):
        sums = 0
        for key in self.marks:
            sums += self.marks[key]
        length = len(self.marks)
        return sums/length

    def getMark(self):
        return self.marks

    def __str__(self):
        return "Imie: {} Nazwisko: {} Srednia ocen: {}".format(self.name, self.surname, self.mean())

class Student(Pupil):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.weights = {}

    def complete_weights(self):
        tmp = Pupil.getMark(self)
        for key in tmp:
            print("Podaj wage dla przedmiotu: " + key)
            weight = input()
            if 0 < float(weight) <=1:
                self.weights[key] = weight
                print("DODANO")
            else:
                print("Zła waga, ustawiono domyślna wage 0,5")
                self.weights[key] = 0.5

    def mean(self):
        total = 0.0
        weight = 0.0
        tmp = Pupil.getMark(self)
        for key, value in tmp.items():
            for key_1, value_1 in self.weights.items():
                if key == key_1:
                    total += float(value) * float(value_1)
                    weight += float(value_1)

        return str(round(float(total/weight), 2))

    def __str__(self):
        return super().__str__()


pu = Pupil("Karol", "Wlazlo")
stu = Student("Karol", "Test")

pu.complete_marks("Polski", 2)
pu.complete_marks("Matematyka", 5)
pu.complete_marks("WF", 2)

stu.complete_marks("Polski", 2)
stu.complete_marks("Matematyka", 5)
stu.complete_marks("WF", 2)

stu.complete_weights()

print(pu)
print(stu)
