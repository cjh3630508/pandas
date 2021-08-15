import pandas as pd


def selectSubSet():
    print("-- start select subset --")
    titanic = pd.read_csv("../testFiles/titanic.csv")
    print("-- get age and sex --")
    ageSex = titanic[["Age", "Sex"]]
    print(ageSex.head())
    print("-- get age > 35 --")
    print(titanic["Age"] > 35)
    ageAbove35 = titanic[titanic["Age"] > 35]
    print(ageAbove35.head())


if __name__ == '__main__':
    selectSubSet()
