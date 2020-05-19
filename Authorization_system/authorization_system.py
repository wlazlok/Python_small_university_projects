import hashlib as h
import exceptions

class User:
    is_logged = None  #atrybut sprawdzający czy użytkownik zalogowany

    def __init__(self, username, password): #metoda init inicjalizująca podane w zadaniu atrybuty
        self.username = username
        self.password = self._encrypt_password(username + password)
        self.is_logged = False

    def _encrypt_password(self, password):  #metoda szyfrująca hasło
        return h.sha3_256(str(password).encode('utf-8'))

    def check_password(self, passwd): #metoda sprawdza czy podano prawidłowe hasło
        if self.password == passwd:
            return True
        else:
            return False

class Authenticator:
    users = {}

    def __init__(self):
        self.users = {None: None}

    def add_user(self, username, password): #metoda, dzięki której dodajemy uzytkownika
        try:
            for i in range(len(self.users)): #iterujemy po całym słowniku
                if self.users.keys() == username:  #sprawdzamy czy podany użytkownik jest już w słowniku
                    raise exceptions.UsernameAlreadyExists('Użytkownik istnieje')
                if len(password) < 7: #sprawdzamy czy hasło nie jest za krótkie
                    raise exceptions.PasswordTooShort('Haslo za krótkie')
                else:
                    self.users[username] = username + str(password)  #wprowadzamy do słownika użytkownika

        except exceptions.AuthenticException: #jeżeli nie uda się dodać użytkownika rzucamy wyjątek
            print("Nie doodano użytkownika")

    def login(self, user):  #tworzymy metodę do logowania
        try:
            for i in range(len(self.users)): #iterujemy po słowniku
                if user.username not in self.users.keys():  #sprawdzamy czy login jest w słowniku
                    raise exceptions.IncorrectUsername('Zły login')
                if user.password == self.users.values(): #sprawdzamy czy hasło jest w słowniku i jest takie samo
                    raise exceptions.IncorrectPassword('Złe hasło')
                else:
                    user.is_logged = True  #jeżeli login i hasło się zgadzają logujemy użytkownika
                    return True
        except exceptions.AuthenticException:
            print("Nie zalogowano") #Jeżeli nie uda sie zalogować rzucamy wyjątek

    def is_logged_in(self, user):  #metoda, która sprawdza czy użytkownik jest zalogowany
        if self.login(user):
            return True
        else:
            return False

class Authorizor:
    def __init__(self, authenticator):
        self.permissions = {None: None}
        self.authenticator = authenticator

    def add_permission(self, permission): #metoda, która pozwala dodać uprawnienia
        try:
            if permission in self.permissions.keys(): #sprawdzamy czy już istnienie takie uprawnienie
                raise exceptions.PermissionError
            else:
                self.permissions[permission] = set() #jeżeli nie dodajemy je do zbioru
        except exceptions.AuthenticException:
            print("Nie udało się dodać uprawnienia") #rzucamy wyjątek, jeżeli nie uda się dodać uprawnienia

    def permit_user(self, permission, user): #metoda, która pozwala dodać uprawnienie dla użytkownika
        try:
            if user.username not in self.authenticator.users.keys(): #sprawdzamy czy istnieje taki użytkownik
                raise exceptions.IncorrectUsername('Zły login')
            elif permission not in self.permissions.keys(): #sprawdzamy czy uprawnienie jest dodane do zbioru
                raise exceptions.PermissionError('Brak takiego uprawnienia')
            else:
                self.permissions[permission].add(user.username) #dodajemy użytkownikowi uprawnienie
        except exceptions.AuthenticException:
            print("Nie udało się przypisać uprawnienia użytkownikowi") #Jeżeli nie uda sie przypisać uprawnienia rzucamy wyjątek

    def check_permission(self, permission, user): #metoda sprawdzająca czy użytkownik ma uprawnienie
        try:
            if not user.is_logged: #sprawdzamy czy użytkownik jest zalogowany
                raise exceptions.NotLoggedError('Niezalogowany')
            for values in self.permissions.values(): #interujemy po wartościach słownika
                if values == None:
                    continue
                elif user.username not in values: # sprawdzamy czy uzytkownik ma takie uprawnienie
                    raise exceptions.NotPermittedError('użytkownik nie ma podanego uprawnienia')
                elif permission not in self.permissions.keys(): #sprawdzamy czy istnieje takie uprawnienie
                    raise exceptions.PermissionError('Nie ma takiego uprawnienia')
                else:
                    print("Masz uprawnienie")
                    break;
        except exceptions.AuthenticException: #Jeżeli użytkownik nie ma uprawnienia rzucamy wyjątek
            print("Użytkownik nie ma takiego uprawnienia")

authenticator = Authenticator() #tworzymy instancję klasy authenticator
authorizor = Authorizor(authenticator) #tworzymy instancję klasy Authorizator
