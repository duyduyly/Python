from enum import Enum


class Status(Enum):
    TODO = "todo"
    PROCESSING = "processing"
    DONE = "done"
    REMOVE = "removed"
    SKIP = "skip"
