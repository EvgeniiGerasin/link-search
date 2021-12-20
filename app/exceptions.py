class BaseException(Exception):

    def __init__(self, message=None) -> None:
        self.message = message
        self._reason = 'REASON: '


class WrongFileTypeSaveException(BaseException):

    def __str__(self) -> str:
        return "".join((self._reason, self.message))
