import requests


if __name__ == "__main__":
    exit(1)


class ReqHandling(object):
    def __init__(self, url: str):
        self.url = url

    def getContent(self) -> str:
        r = requests.get(self.url)
        if not r.ok:
            raise ConnectionError
        return r.text

    def getParsedContent(self) -> dict:
        text: str = self.getContent()
        pass
