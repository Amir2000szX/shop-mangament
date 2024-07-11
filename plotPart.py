import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import arabic_reshaper
from bidi.algorithm import get_display

mpl.rcParams['font.family'] = 'Arial'
class analysis():

    def __init__(self):
        self.conn = sqlite3.connect("mydb.sqlite")
        self.query = "SELECT * FROM sells"
        self.file =pd.read_sql(self.query,self.conn)

    def read(self):
        print(self.file)
    def plotColorBuy(self):
        reshaped_colors = self.file["color"].apply(lambda x: get_display(arabic_reshaper.reshape(x)))
        color_counts = reshaped_colors.value_counts()

        plt.figure(figsize=(21, 12))
        plt.bar(reshaped_colors.unique(), color_counts )
        plt.title('Distribution of Colors')
        plt.axis('equal')

        plt.show()
    def plotTimeBuy(self):
        self.file["Date"] = pd.to_datetime(self.file["Date"])
        self.file["year"] = self.file["Date"].dt.year
        self.file["month"] = self.file["Date"].dt.month
        self.file["day"] = self.file["Date"].dt.day
        self.file["hour"] = self.file["Date"].dt.hour

        plt.figure(figsize=(20, 10))
        plt.subplot(1, 4 ,1)
        plt.bar(self.file["year"].unique(), self.file["year"].value_counts(),width=0.8 ,edgecolor='black',linewidth=1)
        plt.title('Distribution of Years')
        plt.xticks(self.file["year"].unique(),self.file["year"].unique())

        plt.subplot(1, 4 ,2)
        plt.bar(self.file["month"].unique(), self.file["month"].value_counts(),width=1.2,edgecolor='black',linewidth=1)
        plt.title('Distribution of Months')
        plt.xticks(self.file["month"].unique(),self.file["month"].unique())

        plt.subplot(1, 4 ,3)
        plt.bar(self.file["day"].unique(), self.file["day"].value_counts(),width=1.2,edgecolor='black',linewidth=1)
        plt.title('Distribution of Days')
        plt.xticks(self.file["day"].unique(),self.file["day"].unique())

        plt.subplot(1, 4 ,4)
        plt.bar(self.file["hour"].unique(), self.file["hour"].value_counts(),width=1.2,edgecolor='black',linewidth=1)
        plt.title('Distribution of Hours')
        plt.xticks(self.file["hour"].unique(),self.file["hour"].unique())

        plt.subplots_adjust(wspace=0.4)
        plt.show()

plt1 = analysis()
plt1.plotTimeBuy()
