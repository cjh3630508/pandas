import pandas as pd


def readTitanic():
    print("-- read titanic --")
    # titanic = pd.read_excel("../testFiles/titanic.xlsx")
    titanic = pd.read_csv("../testFiles/titanic.csv")
    print("-- titanic --")
    print(titanic)
    print("-- first 3 rows --")
    print(titanic.head(3))
    print("-- last 3 rows --")
    print(titanic.tail(3))
    print("-- dtypes --")
    print(titanic.dtypes)
    print("-- info --")
    print(titanic.info())


def writeTitanic():
    print("-- start write titanic csv --")
    # titanic = pd.read_excel("../testFiles/titanic.csv")
    titanic = pd.read_csv("../testFiles/titanic.csv")
    # index=False 不输出 dataframe 索引
    titanic.to_csv("../testOutputFiles/titanicOutput.csv", index=False)
    print("-- end write titanic --")


if __name__ == '__main__':
    readTitanic()
    writeTitanic()
