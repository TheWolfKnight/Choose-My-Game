from src import *


def main():
    req: ReqHandling = ReqHandling("https://steamcommunity.com/profiles/76561198147177044/games/?tab=all")
    req._getContent()


if __name__ == "__main__":
    main()
    exit(0)

