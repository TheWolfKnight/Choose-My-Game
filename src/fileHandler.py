from os.path import isfile


import json


if __name__ == "__main__":
    exit(1)


class FileHandler(object):
    def __init__(self, prefix_path: str="../bin"):
        self.prefix_path = prefix_path

    def isValidSaveFile(self, filename: str) -> bool:
        if isfile(f"{self.prefix_path}/{filename}"):
            return True
        return False

    def writeHardFile(self, filename: str, data: dict[str, (str|int|dict)], writeState: chr='w') -> None:
        with open(f"{self.prefix_path}/{filename}", writeState) as fp:
            fp.write(json.dump(data))

    def readHardFile(self, filename: str) -> dict[str, (str|int|dict)]:
        r: dict[str, (str|int|dict)] = None
        with open(f"{self.prefix_path}/{filename}", 'r') as fp:
            r = json.load(fp.read())
        return r

