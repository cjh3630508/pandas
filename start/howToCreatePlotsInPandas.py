import pandas as pd
import matplotlib.pyplot as plot


def plotAirQuality():
    print("-- start plot air quality--")
    print("-- air quality datas --")
    airQuality = pd.read_csv("../testFiles/air_quality_no2.csv", index_col=0, parse_dates=True)
    print(airQuality)
    print("-- plot all columns --")
    airQuality.plot()
    plot.show()
    print("-- plot onse column --")
    airQuality["station_paris"].plot()
    plot.show()
    print("-- compare the \(N0_2\) values measured in London versus Paris --")
    airQuality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
    plot.show()
    print("-- end plot air quality --")


if __name__ == '__main__':
    plotAirQuality()
