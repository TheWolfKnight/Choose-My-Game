from bs4 import BeautifulSoup
from tempfile import TemporaryFile
import requests


if __name__ == "__main__":
    exit(1)


class ReqHandling(object):
    def __init__(self, url: str, login_content: dict[str, str]=None):
        self.url = url
        self.req: str = None
        if not self._getAccesse():
            raise ConnectionError

    def _getAccesse(self) -> bool:
        try:
            r = requests.get(self.url, timeout=10)
        except requests.ReadTimeout:
            return False
        if not r.ok:
            return False
        self.req = r
        return True

    def _getContent(self) -> str:
        if not self.req:
            return None
        soup = BeautifulSoup(self.req.text, features="html.parser")
        return soup.prettify()

    def getParsedContent(self) -> dict:
        text: str = self._getContent()
        ret: str = None

        with TemporaryFile('r+') as fp:
            fp.write(text)
            fp.seek(0)
            for line in fp.readlines():
                if "var rgGames" in line:
                    ret = line[line.index('[')+1:line.index('];')]
                    break

        r: list[str] = []
        last_idx: int = 0
        counter: int = 0
        skip: bool = False

        for idx, val in enumerate(ret):
            if skip:
                skip = False
                continue
            if val == '{':
                counter += 1
            elif val == '}':
                counter -= 1
            if counter == 0:
                r.append(ret[last_idx:idx+1])
                last_idx = idx+2
                skip = True

        return r
