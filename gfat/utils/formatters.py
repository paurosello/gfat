from utils.exceptions import MandatoryFieldException


def fill_spaces(value, field_meta):
    length = field_meta["length"]

    if field_meta.get("mandatory", False) and value is None:
        raise MandatoryFieldException

    if type(value) == int:
        value = str(value)

    if value == None:
        value = ""

    if type(value) == str:
        return (" "*(length-len(value)) + value)[-length:][:length]

    raise TypeError
