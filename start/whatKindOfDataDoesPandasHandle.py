import pandas as pd


def dataFrameTest():
    # 创建 dataframe
    print("------ create a data frame ------")
    df = pd.DataFrame(
        {
            "name": ["Braund", "Alice", "Bonnell"],
            "age": [22, 35, 58],
            "sex": ["male", "male", "female"]
        }
    )
    # 输出表格
    print("-- data frame --")
    print(df)
    # 输出列
    print("-- name --")
    print(df["name"])

    print("-- age --")
    print(df["age"])

    print("-- max age --")
    print(df["age"].max())

    print("-- statistics data --")
    print(df.describe())

def seriesTest():
    # 创建 series
    print("\n\n")
    print("------ create a series ------")
    ages = pd.Series([22, 35, 58], name="age")
    print("-- age --")
    print(ages)


if __name__ == '__main__':
    dataFrameTest()
    print("\n\n")
    # seriesTest()
