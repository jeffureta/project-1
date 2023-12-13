class EmptyRowError(Exception):
    """Exception raised for an empty row in the CSV file."""

    pass


class NoPhrasesFoundError(Exception):
    """Exception raised when no valid phrases are found in the CSV file."""

    pass


class CSVFileNotFoundError(Exception):
    """Exception raised when the CSV file is not found."""

    pass


class ImproperlyFormattedRowError(Exception):
    """Exception raised for an improperly formatted row in the CSV file."""

    pass
