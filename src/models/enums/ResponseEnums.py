from enum import Enum

class ResponseStatus(Enum):
    File_Not_allowed = "File type not allowed."
    File_size_exceed = "File size exceeds the maximum limit"
    File_is_Valid = "File is valid."