class AuthenticException(Exception):
    def __init__(self):
        self.username = None
        self.user = None


class PasswordTooShort(AuthenticException):
    pass


class UsernameAlreadyExists(AuthenticException):
    pass


class IncorrectUsername(AuthenticException):
    pass


class IncorrectPassword(AuthenticException):
    pass


class NotLoggedError(AuthenticException):
    pass


class NotPermittedError(AuthenticException):
    pass


class PermissionError(AuthenticException):
    pass