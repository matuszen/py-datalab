from datalab.Utils.types import *
from datalab.Utils.libs import *

def convert(value: Any, new_type: type) -> Any:
    """Converts the given value to the specified type

    Parameters
    ----------
    value : any
        The value to be converted.
    type : type
        The desired type to convert the value to.

    Returns
    -------
    any
        The converted value of the specified type"""

    if type(value) == str and value.strip() == "":
        value = 0

    if new_type == bool and type(value) == str and value.lower().strip() == "false":
        return False

    try:
        return new_type(value)

    except ValueError:
        if new_type == int:
            try:
                return new_type(float(value))
            except ValueError:
                if type(value) == str and value.strip().lower() in ("true", "false"):
                    if value.lower() == "true":
                        return 1
                    elif value.lower() == "false":
                        return 0

        elif new_type == float:
            if type(value) == str and value.strip().lower() in ("true", "false"):
                if value.strip().lower() == "true":
                    return 1.0
                elif value.strip().lower() == "false":
                    return 0.0
        raise


def has_same_type(*values: type) -> bool:
    """Checks if all the values passed as arguments are of the same type

    Parameters
    ----------
    *values : type
        Variable number of values to check for the same type.

    Returns
    -------
    bool
        True if all the values have the same type, False otherwise"""

    if not values:
        return True

    buffer = values[0] if type(values[0]) == type else type(values[0])

    for element in values[1:]:
        element = element if type(element) == type else type(element)
        if element != buffer:
            return False

    return True
