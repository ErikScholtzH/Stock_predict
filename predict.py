import quandl
import pandas
import numpy
import matplotlib.pyplot
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import datetime

#data being pulled from quandl
quandl.ApiConfig.api_key = "KQmy_Miw-rVLxRzXxHai"
df = quandl.get("WIKI/AMZN")
df = df[["Adj. Close"]]

#creating graph
df["Adj. Close"].plot(figsize = (21,9), color = "g")
matplotlib.pyplot.legend(loc = "upper left")
matplotlib.pyplot.show()

forecast = 30

df["prediction"] = df[["Adj. Close"]].shift(-forecast)

#removing last 30 days so we can predict them instead
x = numpy.array(df.drop(["prediction"],1))
x = preprocessing.scale(x)
forecast_x = x[-forecast:]
x = x[:-forecast]

y = numpy.array(df["prediction"])
y = y[:-forecast]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)

#testing how accurate prediction is compared to last 30 days
confidence = clf.score(x_test,y_test)
print("Confidence: "+str(confidence))

forecast_predicted = clf.predict(forecast_x)

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()

dates = pandas.date_range(start  ="2018-03-28", end = "2018-04-26")

matplotlib.pyplot.plot(dates, forecast_predicted, color = "b")
matplotlib.pyplot.legend(loc = "upper left")
df["Adj. Close"].plot(color = "g")
matplotlib.pyplot.xlim(xmin = datetime.date(2017,4,26))
matplotlib.pyplot.show()
