from starlette import status


class BaseError(Exception):
    def __init__(self, status_code: int, detail: str):
        self.code = status_code
        self.detail = detail


class WrongQueryError(BaseError):
    def __init__(self):
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        detail = "Bot can answer only questions related to traveling or marketing"
        super(WrongQueryError, self).__init__(status_code=status_code, detail=detail)
