import os
from abc import ABC, abstractmethod

from my_app.model.WeeklyTodoJson import WeeklyTodoJson
from my_app.utils import *
from my_app.utils import setup_logger
import json


class IFileService(ABC):

    # Load And Return Json String
    @abstractmethod
    def load_str_json(self) -> str:
        pass

    # Check Folder And File if Don't Exist Create File and Folder
    @abstractmethod
    def create_folder_or_file(self, path, file_name) -> None:
        pass

    # Update Json File When updated Data
    @abstractmethod
    def update_json(self, json_class: WeeklyTodoJson) -> None:
        pass


class FileService(IFileService):
    __ROOT_FOLDER = "../resource"  # path to test local file here:("../../resource")
    __YEAR_FOLDER = get_now_datetime().year
    __WEEK_NO = get_week_no()
    __JSON_PATH = f"{__ROOT_FOLDER}/{__YEAR_FOLDER}/{__WEEK_NO}.json"
    __EMPTY_FILE_PATH = f"{__ROOT_FOLDER}/empty_json/empty_json.json"

    logging = setup_logger(name="File Service")

    def __init__(self):
        self.create_folder_or_file(f"{self.__ROOT_FOLDER}/{self.__YEAR_FOLDER}", f"{self.__WEEK_NO}.json")

    def load_str_json(self) -> str:
        try:
            with open(self.__JSON_PATH, "r") as j:
                self.logging.info(f"Load file {self.__JSON_PATH} was Success")
                return j.read()
        except OSError:
            self.logging.error(f"Load File {self.__JSON_PATH} was Failed")
            raise OSError

    def create_folder_or_file(self, path, file_name) -> None:
        if os.path.exists(f"{path}"):
            self.logging.info(f"Folder {path} Existed")
        else:
            self.logging.info(f"Created {path} Folder")
            os.mkdir(path)

        if os.path.exists(f"{path}/{file_name}"):
            self.logging.info(f"File {path}/{file_name} Existed")
        else:
            with open(f"{path}/{file_name}", "w") as file:
                with open(self.__EMPTY_FILE_PATH) as js:
                    file.write(js.read())

    def update_json(self, json_class: WeeklyTodoJson) -> None:
        try:
            with open(self.__JSON_PATH, "w") as f:
                json.dump(json_class.to_dict(), f)
            self.logging.info(f"Json File {self.__JSON_PATH} Updated Success")
        except OSError:
            self.logging.error(f"File {self.__JSON_PATH} Updated Failed!")
