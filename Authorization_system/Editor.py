import authorization_system as auth
import sys

class Editor:

    user = None

    def __init__(self):
        self.username = None
        self.options = {"a": self.login, "b": self.test, "c": self.change, "d": self.quit}

    def login(self): #metoda do wprowadzenia nazwy uzytkownika i hasła oraz logowania
        username = input("username: ")
        password = input("password: ")
        Editor.user = auth.User(username, password)
        auth.authenticator.add_user(username, password)
        auth.authenticator.login(Editor.user)


    def is_permitted(self): #metoda sprawdzająca czy użytkownik jest zalogowany i ma podane uprawnienie
        auth.authorizor.check_permission("Read", Editor.user)

    def test(self): #Metoda służąca do testowania programu
        print("TESTOWANIE PROGRAMU\nTworzenie użytkownika\nDodawanie użytkownika do słownika\nLogowanie użytkownika")
        test_user = auth.User("test_user", "123456789")
        auth.authenticator.add_user("test_user", "123456789")
        auth.authenticator.login(test_user)
        print("Czy zalogowany: " + str(auth.authenticator.is_logged_in(test_user)))

    def change(self): #metoda ustawiająca przykładowe uprawnienia i nadaje użytkownikowi jedno z nich
        auth.authorizor.add_permission("Read")
        auth.authorizor.add_permission("Write")
        auth.authorizor.add_permission("Modify")
        auth.authorizor.permit_user("Read", Editor.user)
        self.is_permitted()

    def quit(self): #metoda służąca do wyjścia z programu
        sys.exit(0)

    def run(self): #służy do pobrania klucza od użytkownika i odczytania wartości ze słownika
        print("a. Login \nb. Test\nc. Change\nd. Exit")
        k = input("wybierz opcje: ")
        while k != 'd':
            for i in self.options.keys():
                if k == i:
                    self.options[k]()
            k = input("wybierz opcje: ")



editor = Editor()
editor.run()
