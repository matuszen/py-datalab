from datalab.utils import *


class Vector:
    @overload
    def __init__(
        self,
        size: int,
        dtype: type = int,
        fill: Union[int, float, str, bool] = 0,
    ) -> None:
        """Initializes a vector with the specified size, data type, and fill value.

        Parameters
        ----------
        size : int
            Size of the vector.
        dtype : type, optional
            Data type of the vector elements. Default is int.
        fill : int or float or str or bool, optional
            Value used to fill the vector. Default is 0."""

        pass

    @overload
    def __init__(self, object: Iterable, dtype: type = int) -> None:
        """Initializes a vector from an iterable object.

        Parameters
        ----------
        object : Iterable
            Iterable object containing the data for the vector.
        dtype : type, optional
            Data type of the vector elements. Default is int."""
        pass

    def __init__(
        self,
        arg1: Optional[Union[Iterable, int]],
        dtype: Optional[type] = None,
        fill: Optional[Union[int, float, str, bool]] = 0,
    ) -> None:
        if isinstance(arg1, int):
            self.__size = arg1
            self._initialize_data_structure(size=arg1, dtype=dtype, fill=fill)

        else:
            self._initialize_data_structure(object=arg1, dtype=dtype)

        self.__supported_types = int, float, str, bool
        self.__precision = 4

    def __str__(self) -> str:
        buffer = [" " for _ in range(self.size)]

        for i, value in enumerate(self.__data):
            if self.dtype == float:
                splited_value = str(value).split(".")

                if len(splited_value) == 1:
                    if splited_value[0] == "0":
                        formatted_value = f"0."

                    else:
                        formatted_value = f"{splited_value[0]}."

                if len(splited_value) == 2:
                    if splited_value[0] == "0" and splited_value[1] == "0":
                        formatted_value = f"0."

                    elif splited_value[0] == "0" and splited_value[1] != "0":
                        if len(splited_value[1]) > self.__precision:
                            formatted_value = "{:.{}e}".format(value, self.__precision)
                        else:
                            formatted_value = f"0.{splited_value[1]}"

                    elif splited_value[0] != "0" and splited_value[1] == "0":
                        formatted_value = f"{splited_value[0]}."

                    else:
                        if len(splited_value[1]) > self.__precision:
                            formatted_value = "{:.{}e}".format(value, self.__precision)
                        else:
                            formatted_value = f"{splited_value[0]}.{splited_value[1]}"

            elif self.dtype == int:
                formatted_value = str(value)

            elif self.dtype == bool:
                formatted_value = str(value)

            else:
                formatted_value = f"'{str(value)}'"

            buffer[i] = formatted_value

        max_element_length = max(len(str(item)) for item in buffer)

        output = "\n"

        for value in buffer:
            output += f"│ {value}{' ' * (max_element_length - len(value) + 1)}│\n"

        return output

    def __add__(
        self,
        object: Union[int, float, Iterable],
    ) -> Self:
        return self.add(object)

    def addition(
        self,
        object: Union[int, float, Iterable],
    ) -> Self:
        """Performs element-wise addition of the vector with the specified object.

        Parameters
        ----------
        object : int or float or Iterable
            The object to add to the vector. It can be a scalar value (int or float), another Vector, or an iterable object with compatible length.

        Returns
        -------
        Vector
            The resulting vector after performing the addition.

        Raises
        ------
        ArithmeticError
            If the object is a Vector or iterable with a different length than the vector.
        TypeError
            If the object is neither a scalar, a Vector, nor an iterable object."""

        buffer = self.deep_copy()

        def vectors_addition(A: Iterable, B: Iterable) -> Iterable:
            return [a + b for a, b in zip(A, B)]

        if isinstance(object, (int, float)):
            buffer.replace([item + object for item in self])

        elif isinstance(object, Vector):
            if len(object) == len(buffer):
                buffer.replace(vectors_addition(buffer, object))
            else:
                raise ArithmeticError("Cannot add vectors with different sizes")

        elif isinstance(object, (list, tuple)):
            if len(object) != len(buffer):
                raise ArithmeticError("Cannot add vectors with different sizes")

            buffer.replace(vectors_addition(buffer, object))

        else:
            raise TypeError(
                "You can only add vector to another vector, list, tuple or number"
            )

        return buffer

    def __sub__(
        self,
        object: Union[int, float, Iterable],
    ) -> Self:
        return self.substraction(object)

    def substraction(
        self,
        object: Union[int, float, Iterable],
    ) -> Self:
        """Performs element-wise subtraction of the vector by the specified object.

        Parameters
        ----------
        object : int or float or Iterable
            The object to subtract from the vector. It can be a scalar value (int or float), another Vector, or an iterable object with compatible length.

        Returns
        -------
        Vector
            The resulting vector after performing the subtraction.

        Raises
        ------
        ArithmeticError
            If the object is a Vector or iterable with a different length than the vector.
        TypeError
            If the object is neither a scalar, a Vector, nor an iterable object."""

        buffer = self.deep_copy()

        def vectors_subtraction(A: Iterable, B: Iterable) -> Iterable:
            return [a - b for a, b in zip(A, B)]

        if isinstance(object, (int, float)):
            buffer.replace([item - object for item in self])

        elif isinstance(object, Vector):
            if len(object) == len(buffer):
                buffer.replace(vectors_subtraction(buffer, object))
            else:
                raise ArithmeticError("Cannot subtract vectors with different sizes")

        elif isinstance(object, (list, tuple)):
            if len(object) != len(buffer):
                raise ArithmeticError("Cannot subtract vectors with different sizes")

            buffer.replace(vectors_subtraction(buffer, object))

        else:
            raise TypeError(
                "You can only subtract a vector from another vector, list, tuple or number"
            )

        return buffer

    def __mul__(
        self,
        object: Union[int, float, str, bool, Iterable],
    ) -> Self:
        return self.multiplication(object)

    def multiplication(
        self,
        object: Union[int, float, str, bool, Iterable],
    ) -> Self:
        """Performs element-wise multiplication of the vector with the specified object.

        Parameters
        ----------
        object : int or float or str or bool or Iterable
            The object to multiply with the vector. It can be a scalar value (int, float, str, or bool), another Vector, or an iterable object with compatible length.

        Returns
        -------
        Vector
            The resulting vector after performing the multiplication.

        Raises
        ------
        ArithmeticError
            If the object is a Vector or iterable with a different length than the vector.
        TypeError
            If the object is an invalid operand for vector multiplication."""

        buffer = self.deep_copy()

        if isinstance(object, (list, tuple, Vector)):
            if len(buffer) != len(object):
                raise ArithmeticError("Cannot multiply vectors with different sizes")

            buffer.replace([a * b for a, b in zip(buffer, object)])

        elif isinstance(object, (int, float, str, bool)):
            buffer.replace([item * object for item in buffer])

        else:
            raise TypeError("Invalid operand for vector multiplication")

        return buffer

    def __pow__(self, exponent: int) -> Self:
        return self.power(exponent)

    def power(
        self,
        exponent: int,
    ) -> Self:
        """Raises each element of the vector to the power of the specified exponent.

        Parameters
        ----------
        exponent : int
            The exponent to raise each element of the vector.

        Returns
        -------
        Vector
            The resulting vector after performing the exponentiation.

        Raises
        ------
        TypeError
            If the exponent is not an integer.
        TypeError
            If the exponent is a negative value."""

        buffer = self.deep_copy()

        if not isinstance(exponent, int):
            raise TypeError(
                "Vector exponentiation is only supported for integer exponents"
            )

        if exponent < 0:
            raise TypeError(
                "Vector exponentiation is not supported for negative exponents"
            )

        if exponent == 0:
            return buffer.fill(1)

        for _ in range(exponent - 1):
            buffer *= self

        return buffer

    def __setitem__(
        self,
        index: int,
        value: Union[int, float, str, bool],
    ) -> None:
        self.set(index, value)

    def set(
        self,
        index: int,
        value: Union[int, float, str, bool],
    ) -> None:
        """Sets the element at the specified index to the given value.

        Parameters
        ----------
        index : int
            The index of the element to set.
        new_value : int or float or str or bool
            The new value to set."""

        if not isinstance(index, int):
            raise ValueError("Index value must be an int")

        if not has_same_type(value, self.dtype):
            try:
                value = convert(value, self.dtype)
            except:
                raise ValueError(
                    "".join(
                        (
                            'Value of type "',
                            str(type(value)).split("'")[1],
                            '" cannot be insert into this Vector',
                        )
                    )
                )

        if index >= self.size:
            raise IndexError(
                f"Vector has {self.size} elements, you cannot appeal to {index} element"
            )

        self.__data[index] = value

    def __getitem__(
        self,
        index: int,
    ) -> Union[int, float, str, bool]:
        return self.get(index)

    def get(
        self,
        index: int,
    ) -> Union[int, float, str, bool]:
        """Returns the element at the specified index.

        Parameters
        ----------
        index : int
            The index of the element to retrieve.

        Returns
        -------
        int or float or str or bool
            The element at the specified index."""

        if not isinstance(index, int):
            raise ValueError("Index value must be an int")

        if index >= self.size:
            raise IndexError(
                f"Vector has {self.size} elements, you cannot appeal to {index} element"
            )

        return self.__data[index]

    def _empty_element(self) -> Union[int, float, str, bool]:
        if self.dtype == float:
            return 0.0

        elif self.dtype == str:
            return ""

        elif self.dtype == bool:
            return False

        else:
            return 0

    def _initialize_data_structure(
        self,
        object: Optional[Iterable] = None,
        size: Optional[int] = None,
        dtype: Optional[type] = None,
        fill: Optional[Union[int, float, str, bool]] = None,
    ) -> None:
        if object is not None:
            self.__size = len(object)

            if dtype is None:
                self.__dtype = self._estimate_data_type(object)
            else:
                self.__dtype = dtype

            self._fill_data(object=object, fill=fill)

        elif size is not None:
            self.__size = size
            self.__dtype = dtype

            self._fill_data(fill=fill)

        else:
            raise ValueError(
                "Matrix._initilize_data_structure() has recived wrong parameters"
            )

    def _fill_data(
        self,
        object: Optional[Iterable] = None,
        fill: Optional[Union[int, float, str, bool]] = None,
    ) -> None:
        element = self._empty_element() if fill is None else fill

        self.__data = [element for _ in range(self.size)]

        if object is not None:
            self.replace(object)

    def fill(self, value: Union[int, float, str, bool]) -> Self:
        """Fills the vector with the specified value.

        Parameters
        ----------
        value : int or float or str or bool
            Value to fill the vector with"""

        for index in range(self.size):
            self.set(index, value)

        return self

    def replace(
        self,
        object: Iterable,
    ) -> Self:
        """Replaces the elements of the vector with the elements from the specified iterable object.

        Parameters
        ----------
        object : Iterable
            The iterable object containing the new elements for the vector."""

        if len(self) == len(object):
            for index, element in enumerate(object):
                self.set(index, element)

        elif len(self) > len(object):
            self.fill(self._empty_element())

            for index, element in enumerate(object):
                self.set(index, element)

        elif len(self) < len(object):
            for index, element in enumerate(object):
                if index == len(self):
                    break
                self.set(index, element)

        return self

    def _estimate_data_type(self, object: Iterable) -> type:
        type_counts = {int: 0, float: 0, str: 0, bool: 0}

        for element in object:
            if isinstance(element, float):
                type_counts[float] += 1
            elif isinstance(element, str):
                type_counts[str] += 1
            elif isinstance(element, bool):
                type_counts[bool] += 1
            elif isinstance(element, int):
                type_counts[int] += 1

        if type_counts[int] > 0 and type_counts[float] > 0:
            return float
        else:
            return max(type_counts, key=type_counts.get)

    @property
    def magnitude(self) -> float:
        """Calculates the magnitude (length) of the vector

        Object's magnitude is the displayed result of an ordering (or ranking) of the class of objects to which it belongs.
        """

        return sum(a * a for a in self) ** (1 / 2)

    @property
    def size(self) -> int:
        """Vector's size (number of elements)"""

        return self.__size

    @size.setter
    def size(self, new_size: int) -> None:
        self.change_size(new_size)

    def change_size(
        self,
        new_size: int,
    ) -> Self:
        """Changes the size of the vector to the specified value.

        Parameters
        ----------
        new_size : int
            The new size to set for the vector.

        Raises
        ------
        ValueError
            If the new size is not an integer."""

        if not isinstance(new_size, int):
            raise ValueError("Vector size must be an integer")

        buffer = self.copy()

        self.__size = new_size
        self._fill_data(buffer)

        return self

    def __len__(self) -> int:
        return self.__size

    @property
    def dtype(self) -> type:
        """Store element's current type"""

        return self.__dtype

    @dtype.setter
    def dtype(self, value: type) -> None:
        self.change_dtype(value)

    def change_dtype(self, new_dtype: type) -> Self:
        """Changes the data type of the vector.

        Parameters
        ----------
        new_dtype : type
            The new data type for the vector"""

        if not isinstance(new_dtype, type):
            raise ValueError(f"New dtype must be an type object not {type(new_dtype)}")

        if new_dtype not in self.__supported_types:
            raise ValueError(
                "".join(
                    (
                        'Type "',
                        str(type(new_dtype)).split("'")[1],
                        '" is not allowed to be an Vector dtype. ',
                    )
                ),
                f"You must choose one of this types: {self.__supported_types}",
            )

        self.__dtype = new_dtype

        for index, item in enumerate(self):
            self.set(index, convert(item, new_dtype))

        return self

    def distance_to(self, other: Self) -> float:
        """Calculates the Euclidean distance between the vector and another vector.

        Parameters
        ----------
        other : Vector
            The other vector to calculate the distance to.

        Returns
        -------
        float
            The Euclidean distance between the two vectors.

        Raises
        ------
        ValueError
            If the sizes of the two vectors are different.
        """

        if self.size != other.size:
            raise ArithmeticError(
                "Cannot calculate distance for vectors with different sizes."
            )

        return (sum((a - b) ** 2 for a, b in zip(self, other))) ** (1 / 2)

    def dot_product(self, other: Self) -> Union[int, float]:
        """Computes the dot product between the vector and another vector.

        Parameters
        ----------
        other : Vector
            The other vector to compute the dot product with.

        Returns
        -------
        int or float
            The dot product of the two vectors.

        Raises
        ------
        ValueError
            If the sizes of the two vectors are different, or if dtypes are not int or float
        """

        if self.size != other.size:
            raise ArithmeticError(
                "Cannot compute dot product for vectors with different sizes."
            )

        if self.dtype not in (int, float) or other.dtype not in (int, float):
            raise ValueError(
                "Cannot compute dot product for vectors with other dtypes than int and float"
            )

        return sum(a * b for a, b in zip(self, other))

    def cross_product(self, other: Self) -> Self:
        """Computes the cross product between the vector and another 3-dimensional vector.

        Parameters
        ----------
        other : Vector
            The other vector to compute the cross product with.

        Returns
        -------
        Vector
            The cross product vector.

        Raises
        ------
        ValueError
            If either vector is not 3-dimensional.
        """

        if self.size != 3 or other.size != 3:
            raise ArithmeticError(
                "Cross product is only defined for 3-dimensional vectors."
            )

        return Vector(
            [
                self[1] * other[2] - self[2] * other[1],
                self[2] * other[0] - self[0] * other[2],
                self[0] * other[1] - self[1] * other[0],
            ]
        )

    def normalize(self) -> Self:
        """Returns a normalized version of the vector (a unit vector in the same direction)."""

        return self.deep_copy().scale(1 / self.magnitude)

    def scale(self, factor: Union[int, float]) -> Self:
        """Scales the vector by multiplying each element by the given factor.

        Parameters
        ----------
        factor : int or float
            The factor to scale the vector by.

        Returns
        -------
        Vector
            The scaled vector.

        Raise
        -----
        ValueError
            If factor parameter is not int or float."""

        if not isinstance(factor, (int, float)):
            raise ValueError("Scale factor must be int or float")

        return self.deep_copy() * factor

    def sum(self) -> Union[int, float, str]:
        """Calculates the sum of all elements in the Vector.

        If elements has str type, method returns concatenated string of all elements.

        Returns
        -------
        int or float or str
            Sum of all elements in Vector

        Raises
        ------
        ValueError
            If dtype are not in (int, float, str, bool)"""

        if self.dtype in (int, float, bool):
            result = sum(self)

        elif self.dtype == str:
            result = ""

            for item in self:
                result = f"{result}{item}"

        else:
            raise ValueError("Vector has not supported dtype to call sum method")

        return result

    def max_value(self) -> Union[int, float, str, bool]:
        """Linear search algorithm for maximal value in the Vector.

        Returns
        -------
        int or float or str or bool
            Element with maximal value in Vector

        Raises
        ------
        ValueError
            If Vector's size is 0"""

        if self.size == 0:
            raise ValueError("Vector without size, cannot have a maximum element")

        elif self.size == 1:
            return self[0]

        elif self.size == 2:
            if self[0] > self[1]:
                return self[0]
            else:
                return self[1]

        elif self.is_empty():
            return self[0]

        else:
            current_max = self[0]

            for item in self:
                if item > current_max:
                    current_max = item

            return current_max

    def min_value(self) -> Union[int, float, str, bool]:
        """Linear search algorithm for minimal value in the Vector.

        Returns
        -------
        int or float or str or bool
            Element with minimal value in Vector

        Raises
        ------
        ValueError
            If Vector's size is 0"""

        if self.size == 0:
            raise ValueError("Vector without size, cannot have a minimum element")

        elif self.size == 1:
            return self[0]

        elif self.size == 2:
            if self[0] < self[1]:
                return self[0]
            else:
                return self[1]

        elif self.is_empty():
            return self[0]

        else:
            current_min = self[0]

            for item in self:
                if item < current_min:
                    current_min = item

            return current_min

    def is_empty(self) -> bool:
        """Checks if the Vector is empty (fullfiled with empty elements)"""

        empty_element = self._empty_element()

        for item in self:
            if item != empty_element:
                return False

        return True

    def is_full(self) -> bool:
        """Check if the Vector is full (no element is empty)"""

        empty_element = self._empty_element()

        for item in self:
            if item == empty_element:
                return False

        return True

    def count_zeros(self) -> int:
        """Counts the number of empty elements in the Vector"""

        empty_element = self._empty_element()

        return sum(1 for element in self if element == empty_element)

    def count_non_zeros(self) -> int:
        """Counts the number of non empty elements in the Vector"""

        empty_element = self._empty_element()

        return sum(1 for element in self if element != empty_element)

    def equals(self, other: Self, only_data: bool = False) -> bool:
        """Checks if the Vector is equal to another Vector.

        By default, the method compares not only the data inside the Vector, but also all variables, e.g. dtype or size. To compare data only, set the only_data parameter to True

        Parameters
        ----------
        other : Vector
            The Vector to be compared

        only_data : bool
            If you need to compare only Vector content set True, default False"""

        if self.size != other.size:
            return False

        if only_data:
            if self.dtype == other.dtype:
                if self.to_list() == other.to_list():
                    return True
                else:
                    return False

            for i in range(self.size):
                if self[i] != convert(other[i], self.dtype):
                    return False

            return True

        if self.dtype != other.dtype:
            return False

        if self.to_list() != other.to_list():
            return False

        return True

    def set_precision(self, new_precision: int) -> None:
        """Sets the precision for numerical values in the Vector.

        It is important only during printing Vector, all time elements has original precision.

        Parameters
        ----------
        new_precision : int
            The new precision value to set for numerical values.

        Raises
        ------
        ValueError
            If the provided precision is not an integer"""

        if not isinstance(new_precision, int):
            raise ValueError("Number precision must be an integer")

        self.__precision = new_precision

    def to_list(self) -> list[Union[int, float, str, bool]]:
        """Converts the vector to a Python list"""

        return self.__data

    def to_tuple(self) -> tuple[Union[int, float, str, bool]]:
        """Converts the vector to a Python tuple"""

        return tuple(self.__data)

    def copy(self) -> Self:
        """Creates a copy of the vector"""

        return copy.copy(self)

    def deep_copy(self) -> Self:
        """Creates a deep copy of the vector"""

        return copy.deepcopy(self)
