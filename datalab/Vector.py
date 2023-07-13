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

    def __add__(self, element: Iterable) -> Self:
        buffer = self.copy()

        def vector_addition(A: Iterable, B: Iterable) -> Iterable:
            return [a + b for a, b in zip(A, B)]

        if isinstance(element, Vector):
            if buffer.size == element.size:
                buffer.__data = vector_addition(buffer.__data, element)
            else:
                raise ArithmeticError("Cannot add vectors with different sizes")

        elif isinstance(element, (list, tuple)):
            if len(element) != buffer.size:
                raise ArithmeticError("Cannot add vectors with different sizes")

            buffer.__data = vector_addition(buffer.__data, element)

        else:
            raise ValueError("You can only add vector to another vector, list or tuple")

        return buffer

    def __sub__(self, element: Iterable) -> Self:
        buffer = self.copy()

        def vector_subtraction(A: Iterable, B: Iterable) -> Iterable:
            return [a - b for a, b in zip(A, B)]

        if isinstance(element, Vector):
            if buffer.size == element.size:
                buffer.__data = vector_subtraction(buffer.__data, element)
            else:
                raise ArithmeticError("Cannot subtract vectors with different sizes")

        elif isinstance(element, (list, tuple)):
            if len(element) != buffer.size:
                raise ArithmeticError("Cannot subtract vectors with different sizes")

            buffer.__data = vector_subtraction(buffer.__data, element)

        else:
            raise ValueError(
                "You can only subtract a vector from another vector, list or tuple"
            )

        return buffer

    def __mul__(self, element: Iterable) -> Self:
        buffer = self.copy()

        if isinstance(element, Vector):
            if buffer.size != element.size:
                raise ArithmeticError("Cannot multiply vectors with different sizes")

            buffer.__data = [a * b for a, b in zip(buffer.__data, element.__data)]

        elif isinstance(element, (list, tuple)):
            if buffer.size != len(element):
                raise ArithmeticError("Cannot multiply vectors with different sizes")

            buffer.__data = [a * b for a, b in zip(buffer.__data, element)]

        elif isinstance(element, (int, float, str, bool)):
            buffer.__data = [element * a for a in buffer.__data]

        else:
            raise ValueError("Invalid operand for vector multiplication")

        return buffer

    def __pow__(self, exponent: int) -> Self:
        buffer = self.copy()

        if not isinstance(exponent, int):
            raise ValueError(
                "Vector exponentiation is only supported for integer exponents"
            )

        if exponent < 0:
            raise ValueError(
                "Vector exponentiation is not supported for negative exponents"
            )

        if exponent == 0:
            return Vector(buffer.size, dtype=buffer.dtype, fill=1)

        for _ in range(exponent - 1):
            buffer *= self

        return buffer

    def __setitem__(self, index: int, value: Union[int, float, str, bool]) -> None:
        if not isinstance(index, int):
            raise ValueError("Index value must be an integer")

        for supported_type in self.__supported_types:
            if self.dtype == supported_type:
                self.__data[index] = supported_type(value)
                break

    def __getitem__(self, index: int) -> Union[int, float, str, bool]:
        if not isinstance(index, int):
            raise ValueError("Index value must be an integer")

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

    def _fill_data(
        self,
        object: Optional[Iterable] = None,
        fill: Optional[Union[int, float, str, bool]] = None,
    ) -> None:
        empty_element = self._empty_element() if fill is None else fill

        self.__data = [empty_element for _ in range(self.size)]

        if object is not None:
            for i, element in enumerate(object):
                try:
                    self.__data[i] = element
                except IndexError:
                    self.__data[i] = empty_element

    @property
    def magnitude(self) -> float:
        """Calculates the magnitude (length) of the vector

        Object's magnitude is the displayed result of an ordering (or ranking) of the class of objects to which it belongs.
        """

        return sum(a * a for a in self.__data) ** (1 / 2)

    @property
    def size(self) -> int:
        """Vector's size (number of elements)"""

        return self.__size

    @size.setter
    def size(self, new_size: int) -> None:
        if isinstance(new_size, int):
            self.__size = new_size
            self._adjust_size()
        else:
            raise ValueError("Vector size must be an integer")

    def _adjust_size(self) -> None:
        buffer = self.__data.copy()

        init_item = self._empty_element()

        self.__data = [init_item for _ in range(self.size)]

        for i in range(self.size):
            try:
                self.__data[i] = buffer[i]
            except:
                continue

    @property
    def dtype(self) -> type:
        """Store element's current type"""

        return self.__dtype

    @dtype.setter
    def dtype(self, new_value: type) -> None:
        if new_value in (int, float, str, bool):
            self.__dtype = new_value
        else:
            raise ValueError("`dl.Vector.dtype` property must be an type object")

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
            raise ValueError(
                "Cannot calculate distance for vectors with different sizes."
            )

        return (sum((a - b) ** 2 for a, b in zip(self.__data, other.__data))) ** (1 / 2)

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
            raise ValueError(
                "Cannot compute dot product for vectors with different sizes."
            )

        if self.dtype and other.dtype not in (int, float):
            raise ValueError(
                "Cannot compute dot product for vectors with other dtypes than int and float"
            )

        dot_product = sum(a * b for a, b in zip(self.__data, other.__data))
        return dot_product

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
            raise ValueError("Cross product is only defined for 3-dimensional vectors.")

        cross_product = Vector(
            [
                self[1] * other[2] - self[2] * other[1],
                self[2] * other[0] - self[0] * other[2],
                self[0] * other[1] - self[1] * other[0],
            ]
        )

        return cross_product

    def normalize(self) -> Self:
        """Returns a normalized version of the vector (a unit vector in the same direction).

        Returns
        -------
        Vector
            The normalized vector."""

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

        scaled_vector = self.deep_copy()
        scaled_vector.__data = [element * factor for element in scaled_vector.__data]

        return scaled_vector

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
            return sum(self.__data)

        elif self.dtype == str:
            result = ""

            for item in self.__data:
                result = f"{result}{item}"

            return result

        else:
            raise ValueError("Vector has not supported dtype to call sum method")

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
            return self.__data[0]

        elif self.size == 2:
            if self.__data[0] > self.__data[1]:
                return self.__data[0]
            else:
                return self.__data[1]

        elif self.is_empty():
            return self.__data[0]

        else:
            current_max = self.__data[0]

            for item in self.__data:
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
            return self.__data[0]

        elif self.size == 2:
            if self.__data[0] < self.__data[1]:
                return self.__data[0]
            else:
                return self.__data[1]

        elif self.is_empty():
            return self.__data[0]

        else:
            current_min = self.__data[0]

            for item in self.__data:
                if item < current_min:
                    current_min = item

            return current_min

    def is_empty(self) -> bool:
        """Checks if the Vector is empty (fullfiled with empty elements)"""

        empty_element = self._empty_element()

        for item in self.__data:
            if item != empty_element:
                return False

        return True

    def is_full(self) -> bool:
        """Check if the Vector is full (all elements are filled)"""

        empty_element = self._empty_element()

        for item in self.__data:
            if item == empty_element:
                return False

        return True

    def fill(self, value: Union[int, float, str, bool]) -> Self:
        """Fills the vector with the specified value.

        Parameters
        ----------
        value : int or float or str or bool
            Value to fill the vector with"""

        if not has_same_type(self.dtype, value):
            value = convert(value, self.dtype)

        for i in range(self.size):
            self.__data[i] = value

        return self

    def count_zeros(self) -> int:
        """Counts the number of empty elements in the Vector"""

        empty_element = self._empty_element()
        count = 0

        for element in self.__data:
            if element == empty_element:
                count += 1

        return count

    def count_non_zeros(self) -> int:
        """Counts the number of non empty elements in the Vector"""

        empty_element = self._empty_element()
        count = 0

        for element in self.__data:
            if element != empty_element:
                count += 1

        return count

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
                if self.__data == other.__data:
                    return True
                else:
                    return False

            for i in range(self.size):
                if self.__data[i] != convert(other.__data[i], self.dtype):
                    return False

            return True

        if self.dtype != other.dtype:
            return False

        if self.__data != other.__data:
            return False

        return True

    def change_dtype(self, new_dtype: type) -> Self:
        """Changes the data type of the vector.

        Parameters
        ----------
        new_dtype : type
            The new data type for the vector"""

        self.dtype = new_dtype
        self._change_data_type(new_dtype)

        return self

    def _change_data_type(self, new_dtype: type) -> None:
        if new_dtype not in self.__supported_types:
            raise ValueError(
                f"dl.Vector.dtype must take one of this value: {self.__supported_types}"
            )
        self.__data = list(map(new_dtype, self.__data))

    def set_precision(self, new_precision: int) -> None:
        """Sets the precision for numerical values in the vector.

        Parameters
        ----------
        new_precision : int
            The new precision value to set for numerical values.

        Raises
        ------
        ValueError
            If the provided precision is not an integer"""

        if isinstance(new_precision, int):
            self.__precision = new_precision
        else:
            raise ValueError("Number precision must be an integer")

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
