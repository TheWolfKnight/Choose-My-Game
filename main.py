from src import *


def main():
    req: ReqHandling = ReqHandling("https://steamcommunity.com/profiles/76561198147177044/games/?tab=all")
    ret = req.getParsedContent()
    choiceMaker: ChooseHandling = ChooseHandling(ret)
    print(choiceMaker.choiceOut())


if __name__ == "__main__":
    main()
    exit(0)

