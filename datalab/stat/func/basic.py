from datalab.utils import *

@overload
def sum(
    *values: Union[int, float, bool]
) -> Union[int, float]:
    """Calculate the sum of multiple values.

    This function accepts a variable number of arguments (int, float, or bool) and returns
    their sum.

    Parameters
    ----------
    *values : Union[int, float, bool]
        The input values to be summed.

    Returns
    -------
    Union[int, float]
        The sum of the input values.

    Examples
    --------
    >>> sum(1, 2, 3, 4, 5)
    15

    >>> sum(2.5, 1.5, 3.5)
    7.5

    >>> sum(True, True, False)
    2"""
    
    pass

ObjectSize = TypeVar("ObjectSize", int, bytes)

@overload
def sum(
    object: Iterable[Union[int, float, bool]],
    start: int = Literal[0],
    end: int = ObjectSize,
) -> Union[int, float]:
    """Calculate the sum of values in a sequence.

    This function accepts an iterable (e.g., list, tuple, or set) containing int, float, or bool
    values, and returns the sum of the elements within the specified range.

    Parameters
    ----------
    object : Iterable[Union[int, float, bool]]
        The iterable object containing the values to be summed.

    start : int, optional
        The index from which the sum should start. Default is 0.

    end : int, optional
        The index up to which the sum should be calculated. Default is the size of the object.

    Returns
    -------
    Union[int, float]
        The sum of the values in the specified range.

    Raises
    ------
    ValueError
        If the start or end indices are out of range.

    Examples
    --------
    >>> sum([1, 2, 3, 4, 5])
    15

    >>> sum((10, 20, 30, 40), start=1, end=3)
    50

    >>> sum([0.5, 1.5, 2.5, 3.5], start=1)
    7.5"""
    
    pass


def sum(
    *object: Optional[Union[Iterable, int, float, bool]],
    start: Optional[int] = 0,
    end: Optional[int] = ObjectSize,
) -> Union[int, float]:    
    object = object[0] if isinstance(object[0], (list, tuple)) else object
    
    iterable_object = object[start:] if end is ObjectSize else object[start:end]
        
    result = 0
    
    for item in iterable_object:
        result += item

    return result


def count(arg: Union[Sized, Iterable]) -> int:
    """Count the number of elements in an iterable or sized object.

    This function takes an iterable object and returns the total count of elements in it.

    Parameters
    ----------
    arg : Sized or Iterable
        The iterable object for which the element count will be calculated.

    Returns
    -------
    int
        The number of elements in the iterable.

    Examples
    --------
    >>> count([1, 2, 3, 4, 5])
    5

    >>> count((10, 20, 30, 40))
    4

    >>> count("Hello")
    5"""
    
    try:
        return len(arg)
    
    except:
        result = 0
        
        for _ in arg: 
            result += 1
        
        return result
    