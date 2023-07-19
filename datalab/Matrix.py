from datalab.utils import *


class Matrix:
    @overload
    def __init__(
        self,
        rows: int,
        columns: int,
        dtype: type = int,
        fill: Union[int, float, str, bool] = 0,
    ) -> None:
        """Initializes a new matrix with the specified number of rows and columns.

        Parameters
        ----------
        rows : int
            The number of rows in the matrix.
        columns : int
            The number of columns in the matrix.
        dtype : type, optional
            The data type of the matrix elements (default: int).
        fill : Union[int, float, str, bool], optional
            The value used to fill the matrix elements (default: 0)"""

        pass

    @overload
    def __init__(
        self,
        shape: tuple[int, int],
        dtype: type = int,
        fill: Union[int, float, str, bool] = 0,
    ) -> None:
        """Initializes a new matrix with the specified shape.

        Parameters
        ----------
        shape : tuple[int, int]
            The shape of the matrix, specified as a tuple (rows, columns).
        dtype : type, optional
            The data type of the matrix elements (default: int).
        fill : Union[int, float, str, bool], optional
            The value used to fill the matrix elements (default: 0)"""

        pass

    @overload
    def __init__(
        self,
        object: Iterable,
        dtype: type = int,
    ) -> None:
        """Initializes a new matrix from an iterable object.

        Parameters
        ----------
        object : Iterable
            An iterable object containing the matrix elements
        dtype : type, optional
            The data type of the matrix elements (default: int)"""

        pass

    def __init__(
        self,
        arg1: Optional[Union[Iterable, tuple[int, int]]] = None,
        arg2: Optional[Union[int, type]] = None,
        dtype: Optional[type] = None,
        fill: Optional[Union[int, float, str, bool]] = 0,
    ) -> None:
        if (
            isinstance(arg1, tuple)
            and len(arg1) == 2
            and all(isinstance(item, int) for item in arg1)
        ):
            self._initialize_data_structure(shape=arg1, dtype=dtype, fill=fill)

        elif (
            isinstance(arg1, int)
            and isinstance(arg2, int)
        ):
            self._initialize_data_structure(shape=(arg1, arg2), dtype=dtype, fill=fill)

        elif (
            isinstance(arg1, (list, tuple))
            and all(isinstance(sublist, (list, tuple)) for sublist in arg1)
        ):
            self._initialize_data_structure(object=arg1, dtype=dtype)

        else:
            raise TypeError("Wrong parameters in Matrix initialization")

        self.__precision = 4
        self.__supported_types = int, float, str, bool
    
    def _initialize_data_structure(
        self,
        object: Optional[Iterable] = None,
        shape: Optional[tuple[int, int]] = None,
        dtype: Optional[type] = None,
        fill: Optional[Union[int, float, str, bool]] = None,
    ) -> None:
        
        if object is not None:
            self.__rows, self.__columns = (
                len(object), max([len(row) for row in object])
            )
            
            if dtype is None:
                self.__dtype = self._estimate_data_type(object)
            else:
                self.__dtype = dtype
            
            self._fill_data(object=object)

        elif shape is not None:
            self.__rows, self.__columns = shape
            
            if dtype is None:
                self.__dtype = int
            else:
                self.__dtype = dtype
            
            self._fill_data(fill=fill)

        else:
            raise ValueError(
                "Wrong paramters to initialize matrix structure"
            )

    def _estimate_data_type(self, object: Iterable) -> type:
        type_counts = {int: 0, float: 0, str: 0, bool: 0}

        for row in object:
            for element in row:
                if isinstance(element, int):
                    type_counts[int] += 1
                elif isinstance(element, float):
                    type_counts[float] += 1
                elif isinstance(element, str):
                    type_counts[str] += 1
                elif isinstance(element, bool):
                    type_counts[bool] += 1

        if type_counts[int] > 0 and type_counts[float] > 0:
            return float
        else:
            return max(type_counts, key=type_counts.get)

    def __str__(self) -> str:
        if self.rows == 0 or self.columns == 0:
            return f"\n│ {' ' * self.columns}│\n"
        
        buffer = [[" " for _ in range(self.columns)] for _ in range(self.rows)]

        for i, row in enumerate(self.__data):
            for j, value in enumerate(row):
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
                                formatted_value = "{:.{}e}".format(
                                    value, self.__precision
                                )
                            else:
                                formatted_value = f"0.{splited_value[1]}"

                        elif splited_value[0] != "0" and splited_value[1] == "0":
                            formatted_value = f"{splited_value[0]}."

                        else:
                            if len(splited_value[1]) > self.__precision:
                                formatted_value = "{:.{}e}".format(
                                    value, self.__precision
                                )
                            else:
                                formatted_value = (
                                    f"{splited_value[0]}.{splited_value[1]}"
                                )

                elif self.dtype == int:
                    formatted_value = str(value)

                elif self.dtype == bool:
                    formatted_value = str(value)

                else:
                    formatted_value = f"'{str(value)}'"

                buffer[i][j] = formatted_value

        max_element_lengths = tuple(
            max(len(str(row[i])) for row in buffer) for i in range(len(buffer[0]))
        )

        output = "\n"

        for row in buffer:
            output += "│ "

            for value, max_length in zip(row, max_element_lengths):
                output += f"{value}{' ' * (max_length - len(value) + 1)}"

            output += "│\n"

        return output
    
    def __add__(
        self,
        object: Union[int, float, Iterable],
    ) -> Self:
        return self.addition(object)

    def addition(
        self,
        object: Union[int, float, Iterable],
    ) -> Self:
        """Performs addition with another matrix or scalar value.

        Parameters
        ----------
        object : int or float or Iterable or Matrix
            The object to add to the matrix. It can be another Matrix, a scalar value (int or float),
            a list or tuple representing a matrix, or a scalar value.

        Returns
        -------
        Matrix
            A new Matrix object containing the result of the addition.

        Raises
        ------
        TypeError
            If the provided object is not of a valid type for addition with the matrix.
        ArithmeticError
            If attempting to add matrices with different shapes.

        Notes
        -----
        This method allows performing addition with another matrix or scalar value. 
        If the provided object is a Matrix, the method performs element-wise addition. 
        If it is a scalar value, the method adds the value to each element of the matrix. 
        If the object is a list or tuple, it should represent a matrix, and element-wise addition is performed.
        """
        
        def matrix_addition(A: Iterable, B: Iterable) -> Iterable:
            return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(A, B)]

        buffer = self.deep_copy()

        if isinstance(object, Matrix):
            if buffer.shape != object.shape:
                raise ArithmeticError("Cannot add matrices with different shapes")
                
            buffer.replace(matrix_addition(buffer, object))

        elif isinstance(object, (list, tuple)):
            if len(object) != buffer.rows or any(
                len(row) != buffer.columns for row in object
            ):
                raise ArithmeticError("Cannot add matrices with different shapes")

            buffer.replace(matrix_addition(buffer, object))
        
        elif isinstance(object, (int, float)):
            buffer.replace([[item + object for item in row] for row in buffer])

        else:
            raise TypeError(
                "You can only add matrix to another matrix, list, tuple or number"
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
        """Performs subtraction with another matrix or scalar value.

        Parameters
        ----------
        object : int or float or Iterable
            The object to subtract from the matrix. It can be another Matrix, a scalar value (int or float),
            a list or tuple representing a matrix, or a scalar value.

        Returns
        -------
        Matrix
            A new Matrix object containing the result of the subtraction.

        Raises
        ------
        TypeError
            If the provided object is not of a valid type for subtraction with the matrix.
        ArithmeticError
            If attempting to subtract matrices with different shapes.

        Notes
        -----
        This method allows performing subtraction with another matrix or scalar value. 
        If the provided object is a Matrix, the method performs element-wise subtraction. 
        If it is a scalar value, the method subtracts the value from each element of the matrix. 
        If the object is a list or tuple, it should represent a matrix, and element-wise subtraction is performed.
        """
    
        def matrix_subtraction(A: Iterable, B: Iterable) -> Iterable:
            return [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(A, B)]

        buffer = self.deep_copy()

        if isinstance(object, Matrix):
            if buffer.shape != object.shape:
                raise ArithmeticError("Cannot subtract matrices with different shapes")
                
            buffer.replace(matrix_subtraction(buffer, object))

        elif isinstance(object, (list, tuple)):
            if len(object) != buffer.rows or any(
                len(row) != buffer.columns for row in object
            ):
                raise ArithmeticError("Cannot subtract matrices with different shapes")

            buffer.replace(matrix_subtraction(buffer, object))
        
        elif isinstance(object, (int, float)):
            buffer.replace([[item - object for item in row] for row in buffer])

        else:
            raise TypeError(
                "You can only subtract a matrix from another matrix, list, tuple, or number"
            )

        return buffer
    
    def __mul__(
        self,
        object: Union[int, float, str, bool, Iterable],
    ) -> Self:
        return self.multiplication(object)

    def multiplication(
        self,
        object: Union[int, float, str, bool, Iterable]
    ) -> Self:
        """Performs multiplication with another matrix, scalar value, or element-wise product.

        Parameters
        ----------
        object : int or float or str or bool or Iterable
            The object to multiply with the matrix. It can be another Matrix, a scalar value (int, float, str, or bool),
            a list or tuple representing a matrix, or a scalar value.

        Returns
        -------
        Matrix
            A new Matrix object containing the result of the multiplication.

        Raises
        ------
        TypeError
            If the provided object is not of a valid type for multiplication with the matrix.
        ArithmeticError
            If attempting to multiply matrices with incompatible dimensions.

        Notes
        -----
        This method allows performing multiplication with another matrix, scalar value, or element-wise product. 
        If the provided object is a Matrix, the method performs matrix multiplication. 
        If it is a scalar value, the method multiplies the value with each element of the matrix. 
        If the object is a list or tuple, it should represent a matrix, and element-wise multiplication is performed.
        """
        
        buffer = self.deep_copy()

        if isinstance(object, Matrix):
            if buffer.columns != object.rows:
                raise ArithmeticError(
                    "Cannot multiply matrices with incompatible dimensions"
                )
                
            buffer.replace([
                [
                    sum(a * b for a, b in zip(row1, col2))
                    for col2 in zip(*object)
                ]
                for row1 in buffer
            ])

        elif isinstance(object, (list, tuple)):
            if buffer.columns != len(object):
                raise ArithmeticError(
                    "Cannot multiply matrices with incompatible dimensions"
                )

            buffer.replace([
                [sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*object)]
                for row1 in buffer
            ])

        elif isinstance(object, (int, float, str, bool)):
            buffer.replace([[object * a for a in row] for row in buffer])

        else:
            raise TypeError("Invalid operand for matrix multiplication")

        return buffer
    
    def __pow__(
        self,
        exponent: int,
    ) -> Self:
        return self.power(exponent)

    def power(
        self,
        exponent: int,
    ) -> Self:
        """Raises the matrix to the power of an integer exponent.

        Parameters
        ----------
        exponent : int
            The non-negative integer exponent to raise the matrix to.

        Returns
        -------
        Matrix
            A new Matrix object containing the result of the matrix exponentiation.

        Raises
        ------
        TypeError
            If the provided exponent is not an integer.
        ValueError
            If the exponent is negative or the matrix is not square for exponent 0.

        Notes
        -----
        This method raises the matrix to the power of a non-negative integer exponent. 
        If the exponent is 0, the method returns the identity matrix with the same number of rows and columns as the original matrix. 
        If the exponent is greater than 0, the method repeatedly multiplies the matrix with itself (exponent - 1) times. 
        If the exponent is not an integer or is negative, an error is raised.
        """
        
        buffer = self.deep_copy()

        if not isinstance(exponent, int):
            raise TypeError(
                "Matrix exponentiation is only supported for integer exponents"
            )

        if exponent < 0:
            raise ValueError(
                "Matrix exponentiation is not supported for negative exponents"
            )

        if exponent == 0:
            if self.rows != self.columns:
                raise ValueError(
                    "Identity matrix must have same rows and columns number"
                )

            return Matrix(
                [
                    [1 if i == j else 0 for j in range(self.rows)]
                    for i in range(self.rows)
                ],
                dtype=self.dtype,
            )

        for _ in range(exponent - 1):
            buffer *= self

        return buffer

    def __setitem__(
        self,
        position: Union[int, tuple[int, int]],
        value: Union[int, float, str, bool],
    ) -> None:
        self.set(position, value)

    @overload
    def set(
        self,
        row: int,
        column: int,
        new_value: Union[int, float, str, bool],
    ) -> None:
        """Sets the element at the specified row and column index to the given value.

        Parameters
        ----------
        row : int
            The row index of the element to set.
        column : int
            The column index of the element to set.
        new_value : int or float or str or bool
            The new value to set."""
        pass

    @overload
    def set(
        self,
        position: tuple[int, int],
        new_value: Union[int, float, str, bool],
    ) -> None:
        """Sets the element at the specified position (row, column) to the given value.

        Parameters
        ----------
        position : tuple
            The position (row, column) of the element to set.
        new_value : int or float or str or bool
            The new value to set."""
        pass

    def set(
        self,
        arg1: Union[int, tuple[int, int]],
        arg2: Union[int, float, str, bool],
        arg3: Optional[Union[int, float, str, bool]] = None,
    ) -> None:
        if (
            arg3 is not None
            and isinstance(arg1, int)
            and isinstance(arg2, int)
            and not isinstance(arg1, bool)
            and not isinstance(arg2, bool)
        ):
            row, column, value = arg1, arg2, arg3

        elif (
            isinstance(arg1, tuple)
            and all(isinstance(element, int) for element in arg1)
            and len(arg1) == 2
        ):
            (row, column), value = arg1, arg2

        else:
            raise TypeError(
                "The index you are referring to must be of the form: object[int][int], or object[int, int]"
            )

        if not has_same_type(value, self.dtype):
            try:
                value = convert(value, self.dtype)
            except:
                raise ValueError(
                    "".join(
                        (
                            'Value of type "',
                            str(type(value)).split("'")[1],
                            '" cannot be insert into this Matrix',
                        )
                    )
                )

        if row >= self.rows:
            raise IndexError(
                f"Matrix has {self.rows} rows, you cannot appeal to {row} row"
            )

        if column >= self.columns:
            raise IndexError(
                f"Matrix has {self.columns} rows, you cannot appeal to {column} column"
            )

        self.__data[row][column] = value

    def __getitem__(
        self,
        position: Union[int, tuple],
    ) -> Union[int, float, str, bool, list]:
        return self.get(position)

    @overload
    def get(
        self,
        row: int,
        column: int,
    ) -> Union[int, float, str, bool]:
        """Returns the element at the specified row and column index.

        Parameters
        ----------
        row : int
            The row index of the element to retrieve.
        column : int
            The column index of the element to retrieve.

        Returns
        -------
        int or float or str or bool
            The element at the specified row and column index."""
        pass

    @overload
    def get(
        self,
        position: tuple[int, int],
    ) -> Union[int, float, str, bool]:
        """Returns the element at the specified position (row, column) as a tuple.

        Parameters
        ----------
        position : tuple
            The position (row, column) of the element to retrieve.

        Returns
        -------
        int or float or str or bool
            The element at the specified position (row, column)."""
        pass

    def get(
        self,
        arg1: Union[int, tuple[int, int]],
        arg2: Optional[int] = None,
    ) -> Union[int, float, str, bool]:
        if isinstance(arg1, int):
            row, column = arg1, arg2

        elif (
            isinstance(arg1, tuple)
            and all(isinstance(element, int) for element in arg1)
            and len(arg1) == 2
            and arg2 is None
        ):
            row, column = arg1

        else:
            raise ValueError(
                "The index you are referring to must be of the form: object[int][int], or object[int, int]"
            )
            
        if column is None:
            return self.__data[row]

        else:
            return self.__data[row][column]
        
    def replace(
        self,
        object: Iterable,
    ) -> None:
        if isinstance(object, Matrix):
            if self.shape == object.shape:
                for i, row in enumerate(object):
                    for j, element in enumerate(row):
                        self.set(i, j, element)

            else:
                self.fill(self._empty_element())
                
                for i, row in enumerate(object):
                    for j, element in enumerate(row):
                        try:
                            self.set(i, j, element)
                        except IndexError:
                            break
        
        elif isinstance(object, (list, tuple)):
            self.fill(self._empty_element())
            
            for i, row in enumerate(object):
                for j, element in enumerate(row):
                    try:
                        self.set(i, j, element)
                    except IndexError:
                        break
            
    def _fill_data(
        self,
        object: Optional[Iterable] = None,
        fill: Optional[Union[int, float, str, bool]] = None,
    ) -> None:
        element = self._empty_element() if fill is None else fill
        
        self.__data = [[element for _ in range(self.columns)] for _ in range(self.rows)]

        if object is not None:
            for i, row in enumerate(object):
                for j, item in enumerate(row):
                    try:
                        self.set(i, j, item)
                    except IndexError:
                        break
    
    def fill(self, value: Union[int, float, str, bool]) -> Self:
        """Fills the matrix with the specified value.

        Parameters
        ----------
        value : int or float or str or bool
            Value to fill the matrix with"""

        if not has_same_type(self.dtype, value):
            value = convert(value, self.dtype)

        for i in range(self.rows):
            for j in range(self.columns):
                self.set(i, j, value)
        
        return self

    def _empty_element(self) -> Union[int, float, str, bool]:
        if self.dtype == float:
            return 0.0

        elif self.dtype == str:
            return ""

        elif self.dtype == bool:
            return False

        else:
            return 0

    @property
    def size(self) -> int:
        """Number of elements in matrix"""

        return self.rows * self.columns

    @property
    def shape(self) -> tuple[int, int]:
        """Store current matrix shape"""

        return self.rows, self.columns

    @shape.setter
    def shape(self, new_shape: tuple[int, int]) -> None:
        self.reshape(new_shape)
    
    @overload
    def reshape(self, rows: int, columns: int) -> Self:
        """Reshapes the matrix to the specified number of rows and columns

        Parameters
        ----------
        rows : int
            The number of rows for the reshaped matrix
        columns : int
            The number of columns for the reshaped matrix"""

        pass

    @overload
    def reshape(self, new_shape: tuple[int, int]) -> Self:
        """Reshapes the matrix to the specified shape

        Parameters
        ----------
        new_shape : tuple[int, int]
            The new shape for the matrix"""

        pass

    def reshape(
        self,
        arg1: Optional[Union[tuple[int, int], int]] = None,
        arg2: Optional[int] = None,
    ) -> Self:
        if (
            arg2 is None
            and isinstance(arg1, tuple)
            and len(arg1) == 2
            and all(isinstance(item, int) for item in arg1)
        ):
            self.__rows, self.__columns = arg1

        elif isinstance(arg1, int) and isinstance(arg2, int):
            self.__rows, self.__columns = arg1, arg2

        else:
            raise TypeError(
                "Shape must be tuple of integers, or both rows and columns must be integers"
            )
            
        self._adjust_dimensions()

        return self
    
    def _adjust_dimensions(self) -> None:
        buffer = self.copy()
        
        self._fill_data(fill=self._empty_element())

        for i, row in enumerate(buffer):
            for j, element in enumerate(row):
                try:
                    self.set(i, j, element)
                except IndexError:
                    break

    @property
    def dtype(self) -> type:
        """Store element's current type"""

        return self.__dtype

    @dtype.setter
    def dtype(self, value: type) -> None:
        self.change_dtype(value)
    
    def change_dtype(
        self,
        value: type
    ) -> Self:
        """Changes the data type of the matrix.

        Parameters
        ----------
        value : type
            The new data type for the matrix"""
        
        if not isinstance(value, type):
            raise ValueError("dtype property must be an type object")
        
        if value not in self.__supported_types:
            raise ValueError(
                f"dtype property must take one of this values: {self.__supported_types}"
            )

        self.__dtype = value
        
        self.replace(
            [[convert(element, value) for element in row] for row in self.__data]
        )

        return self

    @property
    def columns(self) -> int:
        """Number of columns in matrix"""

        return self.__columns

    @columns.setter
    def columns(
        self,
        value: int
    ) -> None:
        self.change_columns_count(value)
    
    def change_columns_count(
        self,
        value: int,
    ) -> Self:
        """Changes the number of columns in the matrix.

        Parameters
        ----------
        value : int
            The new number of columns for the matrix.

        Raises
        ------
        TypeError
            If the value is not an integer."""
        
        if not isinstance(value, int):
            raise TypeError("Columns property must be an integer")
        
        self.__columns = value
        self._adjust_dimensions()
        
        return self

    @property
    def rows(self) -> int:
        """Number of rows in matrix"""

        return self.__rows

    @rows.setter
    def rows(
        self,
        value: int
    ) -> None:
        self.change_rows_count(value)
    
    def change_rows_count(
        self,
        value: int,
    ) -> Self:
        """Changes the number of rows in the matrix.

        Parameters
        ----------
        value : int
            The new number of rows for the matrix.

        Raises
        ------
        TypeError
            If the value is not an integer."""
            
        if not isinstance(value, int):
            raise TypeError("Rows property must be an integer")
        
        self.__rows = value
        self._adjust_dimensions()
        
        return self

    @property
    def permanent(self) -> Union[int, float]:
        """The permanent of the matrix."""
        return self.get_permanent()
    
    def get_permanent(self) -> Union[int, float]:
        """Calculate the permanent of the matrix."""
        
        if self.rows != self.columns:
            raise ValueError("Permanent is only defined for square matrices.")

        if self.size == 1:
            return self[0, 0]

        result = 0
        for permutation in self._permutations(range(self.rows)):
            product = 1
            for i, j in enumerate(permutation):
                product *= self[i, j]
            result += product

        return result

    def _permutations(self, last: Iterable) -> Iterable:
        if len(last) == 1:
            yield last
        else:
            for i in range(len(last)):
                rest = list(last[:i]) + list(last[i + 1 :])
                for p in self._permutations(rest):
                    yield [last[i]] + p

    @property
    def determinant(self) -> Union[int, float]:
        """The determinant of the matrix"""
        
        self.get_determinant()
    
    def get_determinant(self) -> Union[int, float]:
        """Calculate the determinant of the matrix"""

        if self.rows != self.columns:
            raise ValueError("Determinant is only defined for square matrices.")

        match self.size:
            case 1:
                result = self[0, 0]
            
            case 2:
                result = (
                    self[0, 0] * self[1, 1]
                    - self[0, 1] * self[1, 0]
                )
            
            case _:
                result = 0
                for j in range(self.columns):
                    submatrix = self.submatrix(
                        range(1, self.rows),
                        [column for column in range(self.columns) if column != j],
                    )
                    result += self[0, j] * submatrix.determinant * (-1) ** j

        return result

    @property
    def trace(self) -> Union[int, float]:
        """Calculates the trace of a square matrix.

        The trace of a square matrix is the sum of its diagonal elements."""

        if self.rows != self.columns:
            raise ArithmeticError("Trace is only defined for square matrices.")

        return sum(self[i, i] for i in range(self.rows))

    def set_precision(self, new_precision: int) -> None:
        """Sets the precision for numerical values in the matrix.

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

    def is_identity(self) -> bool:
        """Checks if the current matrix is an identity matrix.

        Returns
        -------
        bool
            True if the matrix is an identity matrix, False otherwise"""

        if self.rows != self.columns:
            return False

        for i in range(self.rows):
            for j in range(self.rows):
                if i == j:
                    if self[i, j] != 1:
                        return False
                else:
                    if self[i, j] != 0:
                        return False

        return True

    def transpose(self) -> Self:
        """Transposes the matrix.

        The transpose of a matrix is obtained by interchanging its rows and columns.
        This operation modifies the matrix in place"""

        buffer = self.deep_copy()

        self.reshape(self.columns, self.rows)

        for i in range(self.rows):
            for j in range(self.columns):
                self[i, j] = buffer[j, i]

        return self

    def inverse(self) -> Self:
        """Calculates the inverse of a square matrix.

        Returns
        -------
        Matrix
            The inverse matrix.

        Raises
        ------
        ValueError
            If the matrix is not square or it is singular (non-invertible).

        Notes
        -----
        The matrix must be square and non-singular (invertible) to have an inverse."""

        if self.rows != self.columns:
            raise ValueError("Inverse is only defined for square matrices.")

        determinant = self.determinant

        if determinant == 0:
            raise ValueError("Matrix is singular and does not have an inverse.")

        adjugate = self.adjugate()

        return adjugate * (1 / determinant)

    def adjugate(self) -> Self:
        """Calculates the adjugate of the matrix.

        Raises
        ------
        ValueError
            If the matrix is not square."""

        if self.rows != self.columns:
            raise ValueError("Adjugate is only defined for square matrices.")

        cofactors = Matrix(self.shape)

        for i in range(self.rows):
            for j in range(self.columns):
                submatrix = self.submatrix(
                    [row for row in range(self.rows) if row != i],
                    [col for col in range(self.columns) if col != j],
                )
                cofactor = (-1) ** (i + j) * submatrix.determinant
                cofactors.__data[i][j] = cofactor

        return cofactors.transpose()

    def swap_rows(self, row1: int, row2: int) -> Self:
        """Swaps two rows in the matrix.

        Parameters
        ----------
        row1 : int
            Index of the first row to swap.
        row2 : int
            Index of the second row to swap."""

        self.__data[row1], self.__data[row2] = self.__data[row2], self.__data[row1]
        return self

    def scale_row(self, row: int, scalar: Union[int, float]) -> Self:
        """Scales a row in the matrix by a scalar value.

        Parameters
        ----------
        row : int
            Index of the row to scale.
        scalar : int or float
            Scalar value to multiply the row by."""

        self.__data[row] = [scalar * element for element in self.__data[row]]
        return self

    def submatrix(self, rows_index: Iterable, columns_index: Iterable) -> Self:
        """Creates and returns a submatrix by selecting the specified ranges of rows and columns.

        Parameters
        ----------
        rows_index : Iterable
            The range of row indices to include in the submatrix.
        columns_index : Iterable
            The range of column indices to include in the submatrix.

        Returns
        -------
        Matrix
            The submatrix with the specified ranges of rows and columns.

        Notes
        -----
        This method creates a new matrix object with dimensions (len(rows_index), len(columns_index)),
        where the rows and columns within the specified ranges are included. The elements of the submatrix
        are obtained from the corresponding elements of the original matrix."""

        sub_rows = len(rows_index)
        sub_columns = len(columns_index)
        submatrix = Matrix((sub_rows, sub_columns))

        for i, row_index in enumerate(rows_index):
            for j, column_index in enumerate(columns_index):
                submatrix.__data[i][j] = self.__data[row_index][column_index]

        return submatrix

    def to_lower_triangular(self) -> Self:
        """Converts the matrix to lower triangular form.

        Returns
        -------
        Matrix
            The matrix in lower triangular form.

        Notes
        -----
        In a lower triangular matrix, all elements above the main diagonal are set to 0.
        """

        result = self.deep_copy()

        for i in range(result.rows):
            for j in range(i + 1, result.columns):
                result[i, j] = 0

        return result

    def to_upper_triangular(self) -> Self:
        """Converts the matrix to upper triangular form.

        Returns
        -------
        Matrix
            The matrix in upper triangular form.

        Notes
        -----
        In an upper triangular matrix, all elements below the main diagonal are set to 0.
        """

        result = self.deep_copy()

        for i in range(1, result.rows):
            for j in range(i):
                result[i, j] = 0

        return result

    def to_logical_matrix(self) -> Self:
        """Convert current matrix to logical matrix ((0, 1)-matrix)

        This function change all elements in matrix to bool and from this it follows that the matrix becomes a logical matrix
        """

        self.change_dtype(bool)

        return self

    def to_list(self) -> list[list[Union[int, float, str, bool]]]:
        """Converts the matrix to a Python list"""

        return self.__data

    def to_tuple(self) -> tuple[tuple[Union[int, float, str, bool]]]:
        """Converts the matrix to a Python tuple"""
        
        return tuple([tuple(row) for row in self])

    def copy(self) -> Self:
        """Creates a copy of the matrix"""

        return copy.copy(self)

    def deep_copy(self) -> Self:
        """Creates a deep copy of the matrix"""

        return copy.deepcopy(self)
