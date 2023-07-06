from datalab.utils import *


class Matrix:
    @overload
    def __init__(self, rows: int, columns: int, dtype: type = int) -> None:
        pass

    @overload
    def __init__(self, shape: tuple[int, int], dtype: type = int) -> None:
        pass

    @overload
    def __init__(self, object: Iterable) -> None:
        pass

    def __init__(
        self,
        arg1: Optional[Union[Iterable, tuple[int, int]]] = None,
        arg2: Optional[Union[int, type]] = None,
        dtype: Optional[type] = int,
    ) -> None:
        if (
            isinstance(arg1, tuple)
            and len(arg1) == 2
            and (isinstance(arg1[0], int) and isinstance(arg1[1], int))
        ):
            self._initialize_data_structure(shape=arg1, dtype=dtype)

        elif isinstance(arg1, int) and isinstance(arg2, int):
            self._initialize_data_structure(shape=(arg1, arg2), dtype=dtype)

        else:
            self._initialize_data_structure(object=arg1)

        self.__precision = 4
        self.__supported_types = int, float, str, bool

    def __str__(self) -> str:
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

        output = ""

        for row in buffer:
            output += "│ "

            for value, max_length in zip(row, max_element_lengths):
                output += f"{value}{' ' * (max_length - len(value) + 1)}"

            output += "│\n"

        return output

    def __setitem__(
        self, index: Union[tuple, int], value: Union[int, float, str, bool]
    ) -> None:
        if (
            isinstance(index, tuple)
            and isinstance(index[0], int)
            and isinstance(index[1], int)
            and len(index) == 2
        ):
            row, column = index
        elif isinstance(index, int):
            row = index
            column = None
        else:
            raise ValueError(
                "The index you are referring to must be of the form: object[int][int], or object[int, int]"
            )

        for supported_type in self.__supported_types:
            if self.dtype == supported_type:
                converted_value = supported_type(value)
                break

        if column is not None:
            self.__data[row][column] = converted_value
        else:
            self.__data[row] = converted_value

    def __getitem__(self, index: Union[tuple, int]) -> Union[int, float, str, bool]:
        if (
            isinstance(index, tuple)
            and isinstance(index[0], int)
            and isinstance(index[1], int)
            and len(index) == 2
        ):
            rows, columns = index
            return self.__data[rows][columns]

        elif isinstance(index, int):
            return self.__data[index]

        else:
            raise ValueError(
                "The index you are referring to must be of the form: object[int][int], or object[int, int]"
            )

    def _estimate_data_type(
        self, data: list[list[Union[int, float, str, bool]]]
    ) -> type:
        type_counts = {int: 0, float: 0, str: 0, bool: 0}

        for row in data:
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

    def _fill_data(self, object: Optional[Iterable] = None) -> None:
        empty_element = self._empty_element()

        self.__data = [
            [empty_element for _ in range(self.columns)] for _ in range(self.rows)
        ]

        if object is not None:
            for i, row in enumerate(object):
                for j, element in enumerate(row):
                    try:
                        self.__data[i][j] = element
                    except IndexError:
                        self.__data[i][j] = empty_element

    def _initialize_data_structure(
        self,
        object: Optional[Iterable] = None,
        shape: Optional[tuple[int, int]] = None,
        dtype: Optional[type] = None,
    ) -> None:
        if object is not None:
            rows_count = len(object)
            buffer = [0 for _ in range(rows_count)]

            for i, row in enumerate(object):
                buffer[i] = len(row)

            self.__rows = rows_count
            self.__columns = max(buffer)
            self.__dtype = self._estimate_data_type(object)
            self._fill_data(object)

        elif shape is not None:
            self.__rows, self.__columns = shape
            self.__dtype = dtype
            self._fill_data()

        else:
            raise ValueError(
                "Matrix._initilize_data_structure() has recived wrong parameters"
            )

    def _empty_element(self) -> Union[int, float, str, bool]:
        if self.dtype == float:
            return 0.0

        elif self.dtype == str:
            return ""

        elif self.dtype == bool:
            return False

        else:
            return 0

    def _adjust_dimensions(self) -> None:
        buffer = self.__data.copy()

        init_item = self._empty_element()

        self.__data = [
            [init_item for _ in range(self.columns)] for _ in range(self.rows)
        ]

        for i in range(self.rows):
            for j in range(self.columns):
                try:
                    self.__data[i][j] = buffer[i][j]
                except:
                    continue

    def _change_data_type(self, new_dtype: type) -> None:
        if new_dtype not in self.__supported_types:
            raise ValueError(
                f"dl.Matrix.dtype must take one of this value: {self.__supported_types}"
            )

        self.__data = [[new_dtype(element) for element in row] for row in self.__data]

    @property
    def size(self) -> int:
        return self.rows * self.columns

    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.columns

    @shape.setter
    def shape(self, new_shape: tuple[int, int]) -> None:
        if isinstance(new_shape, tuple):
            self.rows, self.columns = new_shape
        else:
            raise ValueError("`dl.Matrix.shape` property must be a tuple of integers")

    @property
    def dtype(self) -> type:
        return self.__dtype

    @dtype.setter
    def dtype(self, new_value: type) -> None:
        if new_value in (int, float, str, bool):
            self.__dtype = new_value
        else:
            raise ValueError("`dl.Matrix.dtype` property must be an type object")

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, new_value: int) -> None:
        if isinstance(new_value, int):
            self.__columns = new_value
            self._adjust_dimensions()
        else:
            raise ValueError("`dl.Matrix.columns` property must be an integer")

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, new_value: int) -> None:
        if isinstance(new_value, int):
            self.__rows = new_value
            self._adjust_dimensions()
        else:
            raise ValueError("`dl.Matrix.rows` property must be an integer")

    def change_dtype(self, new_dtype: type) -> str:
        self.dtype = new_dtype
        self._change_data_type(new_dtype)

    def set_precision(self, new_precision: int) -> None:
        if isinstance(new_precision, int):
            self.__precision = new_precision
        else:
            raise ValueError("Number precision must be an integer")

    @overload
    def reshape(self, rows: int, columns: int) -> None:
        pass

    @overload
    def reshape(self, new_shape: tuple[int, int]) -> None:
        pass

    def reshape(
        self,
        arg1: Optional[Union[tuple[int, int], int]] = None,
        arg2: Optional[int] = None,
    ) -> None:
        if (
            arg2 is None
            and isinstance(arg1, tuple)
            and isinstance(arg1[0], int)
            and isinstance(arg1[1], int)
            and len(arg1) == 2
        ):
            self.rows, self.columns = arg1
            self._adjust_dimensions()

        elif isinstance(arg1, int) and isinstance(arg2, int):
            self.rows, self.columns = arg1, arg2
            self._adjust_dimensions()

        else:
            raise ValueError(
                "Shape must be tuple of integers, or both rows and columns must be integers"
            )

    def to_list(self) -> list[list[Union[int, float, str, bool]]]:
        return self.__data

    def to_tuple(self) -> tuple[tuple[Union[int, float, str, bool]]]:
        buffer = [tuple() for _ in range(self.rows)]

        for i, row in enumerate(self.__data):
            buffer[i] = tuple(row)

        return tuple(buffer)

    def copy(self) -> list[list[Union[int, float, str, bool]]]:
        return self.__data
