import pandas as pd


def selectSubSet():
    print("-- start select subset --")
    titanic = pd.read_csv("../testFiles/titanic.csv")
    # 选择多列
    print("-- get age and sex --")
    ageSex = titanic[["Age", "Sex"]]
    print(ageSex.head())
    # 条件过滤
    print("-- get age > 35 --")
    print(titanic["Age"] > 35)
    ageAbove35 = titanic[titanic["Age"] > 35]
    print(ageAbove35.head())
    # 条件过滤 isin
    print("-- class 2 and 3 --")
    cabin2_3 = titanic[titanic["Pclass"].isin([2, 3])]
    print(cabin2_3.head())
    # 行列过滤
    print("-- get names of the passengers older than 35 year old --")
    ageAbove35Name = titanic.loc[titanic["Age"] > 35, "Name"]
    print(ageAbove35Name.head())
    print("-- row 10 to 25, col 3 to 5 --")
    rowCol = titanic.iloc[9:25, 2:5]
    print(rowCol)
    # 选择后赋新值（会覆盖原来的值）
    titanic.iloc[0:3, 3] = "anonymous"
    print(titanic.head())

if __name__ == '__main__':
    pd.set_option('display.max_columns', 24,
                  'display.width', 1000)
    selectSubSet()
