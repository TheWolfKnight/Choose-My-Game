from random import choice
from json import loads


if __name__ == "__main__":
    exit(1)


class ChooseHandling(object):
    def __init__(self, inpt: list[str]):
        self.inpt = inpt
        self.ch: dict = self._getValidChoice()

    def _getValidChoice(self) -> dict:
        while True:
            tmp: dict = loads(choice(self.inpt))

            if tmp["app_type"] == 1:
                return tmp

    def choiceOut(self) -> str:
        hr: float = 0

        try:
            hr: float = self.ch["hours_forever"]
        except KeyError:
            pass

        r: str = """
The game you will be playing now is:
Name: {},
Houres Played: {}
        """.format(self.ch["name"], hr)

        return r
