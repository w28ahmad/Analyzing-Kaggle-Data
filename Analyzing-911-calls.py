import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Opens up the file with the 911 data from kaggle
def readFile():
    df = pd.read_csv("911.csv")
    return df


# Prints the top 5 zipcodes for 911 calls
def top5zipcodes(df):
    newdf = df["zip"].value_counts()
    print(newdf.head(5))
    return newdf


# Prints the top 5 towns with 911 calls
def top5towns(df):
    newdf = df['twp'].value_counts()
    print(newdf.head(5))
    return newdf


# Prints the number of unique titles in the data
def uniqueTowns(df):
    print(df['title'].nunique())


# Adding new feature, a colomn for reasons
def reasonsCol(df):
    titles = df["title"]
    reasons = list(map(lambda t: t.split(":")[0], titles))
    df["reasons"] = reasons
    # print(df.head(5))
    return df


# Using the reasons column to see what is the most common reason for a 911 call
def commonReason(df):
    newdf = df["reasons"].value_counts()
    print(newdf)
    return newdf


# Countplot of 911 calls by reason
def reasonsCountPlot(df):
    sns.countplot(x="reasons", data=df)
    plt.show()


# Convert the timeStamp column into dateTime type
# Adds "day of week" column to the df
# Adds "Month" column to the df
def toTime(df):
    df["timeStamp"] = pd.to_datetime(df['timeStamp'])
    # time = df['timeStamp'].iloc[0]
    dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
    df["Day of Week"] = list(map(lambda date: dmap[date.weekday()], df["timeStamp"]))
    df["Month"] = list(map(lambda date: date.month, df['timeStamp']))
    newdf = df.groupby(['Month']).count()
    return [df, newdf]


# Plots a count plot of number of call per weekday catogorized by the reason
def weekDayCallCount(df):
    sns.countplot(x="Day of Week", data=df, hue="reasons")
    plt.show()


# Plots a count plot of the number of calls per month catogorized by reason
def monthCallCount(df):
    sns.countplot(x="Month", data=df, hue="reasons")
    plt.show()


# Plots a line plot of the number of calls per month
def monthCallLgraph(df):
    sns.lineplot(x=df.index, y="reasons", data=df)
    plt.show()


# Plots a regression lineplot of the number of 911 calls per month 
def monthCallImplot(df):
    df.reset_index(inplace=True)
    sns.lmplot(x='Month', y="reasons", data=df)
    plt.show()


# Adds a date column to the dataFrame
def toDate(df):
    df["Date"] = list(map(lambda date: date.date(), df["timeStamp"]))
    return df


# Creates a line graph of the date and the number of calls recieved that day
def dateLinePlot(df):
    newdf = df.groupby(["Date"]).count()
    sns.lineplot(x=newdf.index, y="reasons", data=newdf)
    plt.show()


# Creates a line plot for each of the 3 reasons, date vs number of 911 calls
def dateLinePlotbyReasons(df):
    EMSdf = df[df["reasons"]=="EMS"]
    Firedf = df[df["reasons"]=="Fire"]
    Trafficdf = df[df["reasons"]=="Traffic"]
    CreateLinePlot(EMSdf)
    CreateLinePlot(Firedf)
    CreateLinePlot(Trafficdf)


# Creates a line plot for dateLinePlotbyReasons() function
def CreateLinePlot(df):
    newdf = df.groupby(["Date"]).count()
    title = df["reasons"].iloc[0]
    sns.lineplot(x=newdf.index, y="reasons", data=newdf).set_title(title)
    plt.show()


# Creates an hour column in the data fram and then arranges the data to show calls in a Day of Week vs hours in a day
def heatmapDfHourVsDay(df):
    df["Hour"] = list(map(lambda date: date.hour, df["timeStamp"]))
    newdf = df.groupby(["Day of Week", "Hour"]).count().unstack()
    return newdf


# Creates a heatmap of the heatmapDfHourVsDay data
def hoursVsDayOfWeek(df):
    sns.heatmap(data=df["lat"], cmap="YlGnBu_r")
    plt.show()


# Creates a clustermap of the heatmapDfHourVsDay data
def hoursVsDaysClusterMap(df):
    sns.clustermap(data=df["lat"], cmap="YlGnBu_r")
    plt.show()


# Arranges the data to snow calls in a Day of week vs the Manth
def heatmapDfMonthVsDay(df):
    newdf = df.groupby(["Day of Week", "Month"]).count().unstack()
    return(newdf["lat"])


# Creates a Heatmap of the heatmapDfMonthVsDay data
def DayofWeekVsMonths(df):
    sns.heatmap(data=df, cmap="YlGnBu_r")
    plt.show()


# Creates a Clustermap of the heatmapDfMonthVsDay data
def DayofWeekVsMonthsClusterMap(df):
    sns.clustermap(data=df, cmap="YlGnBu_r")
    plt.show()


if __name__ == "__main__":
    df = readFile()

    # Creating more Features for the dataFrame
    df = reasonsCol(df)
    df, byMonth = toTime(df)
    df = toDate(df)
    heatmapDfHourVsDay = heatmapDfHourVsDay(df)
    heatmapDfMonthVsDay = heatmapDfMonthVsDay(df) 

    # Some Extra Findings
    # top5zipcodes(df)
    # top5towns(df)
    # uniqueTowns(df)
    # commonReason(df)

    # Plots of different features in the Dataset
    # reasonsCountPlot(df)
    # weekDayCallCount(df)
    # monthCallCount(df)
    # monthCallLgraph(byMonth)
    # monthCallImplot(byMonth)
    # dateLinePlot(df)
    # dateLinePlotbyReasons(df)

    # Heatmaps/ClusterMaps
    # hoursVsDayOfWeek(heatmapDfHourVsDay)
    # hoursVsDaysClusterMap(heatmapDfHourVsDay)
    # DayofWeekVsMonths(heatmapDfMonthVsDay)
    # DayofWeekVsMonthsClusterMap(heatmapDfMonthVsDay)





