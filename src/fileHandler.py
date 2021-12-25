from os.path import isfile


import json


if __name__ == "__main__":
    exit(1)


class FileHandler(object):
    def __init__(self, prefix_path: str):
        self.prefix_path = prefix_path

    def _isValidSaveFile(self, filename: str) -> bool:
        if isfile(f"{self.prefix_path}/{filename}"):
            return True
        return False

    def writeHardFile(self, filename: str, data: dict[str, (str|int)]) -> None:
        pass

    def readHardFile(self, filename: str) -> dict[str, (str|int)]:
        pass

