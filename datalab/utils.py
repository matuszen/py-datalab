import sys
from datetime import datetime
from typing import Optional, Union, TextIO, Iterable, overload


def _log(
    *values: object,
    type: Optional[Union[str, None]] = "info",
    show_time: Optional[Union[bool, None]] = True,
    separator: Optional[Union[str, None]] = " ",
    ending: Optional[Union[str, None]] = "\n",
) -> None:
    """Write log messages to the standard output or standard error.

    Parameters
    ----------
    `*values` : object
        Variable number of values to be logged.
    `type` : str or None, optional
        Type of log message. Default is 'info'.
    `show_time` : bool or None, optional
        Specifies whether to include the current timestamp in the log message. Default is True.
    `separator` : str or None, optional
        Separator between values in the log message. Default is a single space.
    `ending` : str or None, optional
        String appended at the end of the log message. Default is a new line.

    Notes
    -----
    - If `type` is not one of 'ERROR', 'ERR', or 'BUG', the log message is written to the standard output.
    - If `type` is one of 'ERROR', 'ERR', or 'BUG', the log message is written to the standard error.

    Examples
    --------
    >>> log("This", "is", "an", "informational", "message", type="info")
    [20-06-2023 12:34:56][INFO] This is an informational message

    >>> log("An", "error", "occurred", type="error")
    [20-06-2023 12:34:56][ERROR] An error occurred"""

    formated_type = type.upper().strip()

    def write_output(output_stream: TextIO):
        if show_time:
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            output_stream.write(f"[{current_time}][{formated_type}]\t")

        for item in values:
            output_stream.write(f"{str(item)}{separator}")

        output_stream.write(ending)
        output_stream.flush()

    if formated_type not in ("ERROR", "ERR", "BUG"):
        write_output(sys.stdout)
    else:
        write_output(sys.stderr)


def _log_warning(
    *values: object,
    separator: Optional[Union[str, None]] = " ",
    ending: Optional[Union[str, None]] = "\n",
) -> None:
    """Logs warning messages to the standard error stream.

    Parameters
    ----------
    `*values` : object
        Variable number of values to be logged.
    `separator` : str or None, optional
        Separator between values in the log message. Default is a single space.
    `ending` : str or None, optional
        String appended at the end of the log message. Default is a new line.

    Examples
    --------
    >>> log_warning("Warning: Data may be incomplete.")
    [06-07-2023 10:30:45][WARNING] Warning: Data may be incomplete.\n

    >>> log_warning("Low disk space:", 2.5, "GB", separator=" ")
    [06-07-2023 10:30:45][WARNING] Low disk space: 2.5 GB\n"""

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    sys.stderr.write(f"[{current_time}][WARNING]\t")

    for item in values:
        sys.stderr.write(f"{str(item)}{separator}")

    sys.stderr.write(ending)
    sys.stderr.flush()


def _log_error(
    *values: object,
    separator: Optional[Union[str, None]] = " ",
    ending: Optional[Union[str, None]] = "\n",
) -> None:
    """Logs error messages to the standard error stream.

    Parameters
    ----------
    `*values` : object
        Variable number of values to be logged.
    `separator` : str or None, optional
        Separator between values in the log message. Default is a single space.
    `ending` : str or None, optional
        String appended at the end of the log message. Default is a new line.

    Examples
    --------
    >>> log_error("An error occurred.")
    [06-07-2023 10:30:45][ERROR] An error occurred.\n

    >>> log_error("Invalid input:", 42, separator=" - ")
    [06-07-2023 10:30:45][ERROR] Invalid input: - 42\n"""

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    sys.stderr.write(f"[{current_time}][ERORR]\t")

    for item in values:
        sys.stderr.write(f"{str(item)}{separator}")

    sys.stderr.write(ending)
    sys.stderr.flush()
