import os

from my_app.utils import *
from my_app.utils import setup_logger


class FileService:
    __ROOT_FOLDER = "../resource"
    __YEAR_FOLDER = get_now_datetime().year
    __WEEK_NO = get_week_no()
    __JSON_PATH = f"{__ROOT_FOLDER}/{__YEAR_FOLDER}/{__WEEK_NO}.json"
    __EMPTY_FILE_PATH = f"{__ROOT_FOLDER}/empty_json/empty_json.json"

    logging = setup_logger(name="File Service")

    def load_str_json(self):
        try:
            self.create_folder_or_file(f"{self.__ROOT_FOLDER}/{self.__YEAR_FOLDER}", f"{self.__WEEK_NO}.json")
            with open(self.__JSON_PATH, "r") as j:
                self.logging.info(f"Load file {self.__JSON_PATH} was Success")
                return j.read()
        except OSError:
            self.logging.error(f"Load File {self.__JSON_PATH} was Failed")
            raise OSError

    def update_json(self, json: str):
        try:
            with open(self.__JSON_PATH, "a") as j:
                j.write(json)
                self.logging.info("Update File was Success")
        except OSError:
            self.logging.error("Update File was Failed")
            raise OSError

    def create_folder_or_file(self, path, file_name):
        if os.path.exists(f"{path}"):
            self.logging.info(f"Folder {path} Existed")
        else:
            self.logging.info(f"Created {path} Folder")
            os.mkdir(path)

        if os.path.exists(f"{path}/{file_name}"):
            self.logging.info(f"File {path}/{file_name} Existed")
        else:
            with open(f"{path}/{file_name}", "w") as file:
                with open(self.__EMPTY_FILE_PATH) as json:
                    file.write(json.read())




