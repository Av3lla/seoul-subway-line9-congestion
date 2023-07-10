import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/NanumGothic.ttf').get_name())

""" df1 = pd.read_csv("./data/상선일반평일.csv", encoding='cp949')
df2 = pd.read_csv("./data/하선일반평일.csv", encoding='cp949')
df3 = pd.read_csv("./data/상선일반휴일.csv", encoding='cp949')
df4 = pd.read_csv("./data/하선일반휴일.csv", encoding='cp949') """
df5 = pd.read_csv("./data/상선급행평일.csv", encoding='cp949')
df6 = pd.read_csv("./data/하선급행평일.csv", encoding='cp949')
df7 = pd.read_csv("./data/상선급행휴일.csv", encoding='cp949')
df8 = pd.read_csv("./data/하선급행휴일.csv", encoding='cp949')

""" normalWeekday = df1.copy()
for i in range(0, len(df1.index)):
    for j in range(1 , len(df1.columns)):
        normalWeekday.iloc[i, j] = df1.iloc[i, j] + df2.iloc[i, j]
print(normalWeekday)

normalWeekend = df3.copy()
for i in range(0, len(df3.index)):
    for j in range(1 , len(df3.columns)):
        normalWeekend.iloc[i, j] = df3.iloc[i, j] + df4.iloc[i, j]
print(normalWeekend) """

#급행 평일
fastWeekday = df5.copy()
for i in range(0, len(df5.index)):
    for j in range(1 , len(df5.columns)):
        fastWeekday.iloc[i, j] = df5.iloc[i, j] + df6.iloc[i, j]
print(fastWeekday)

#급행 휴일
fastWeekend = df7.copy()
for i in range(0, len(df7.index)):
    for j in range(1 , len(df7.columns)):
        fastWeekend.iloc[i, j] = df7.iloc[i, j] + df8.iloc[i, j]
print(fastWeekend)


#급행 평일 역별 혼잡도
fastWeekdayStation = fastWeekday.iloc[:, 1:].sum(axis='columns')
fastWeekdayStation.index = [fastWeekday.iloc[:, 0]]
print(fastWeekdayStation)

#급행 평일 시간별 혼잡도
fastWeekdayTime = fastWeekday.drop('구분', axis='columns').sum(axis='rows')
print(fastWeekdayTime)


#급행 휴일 역별 혼잡도
fastWeekendStation = fastWeekend.iloc[:, 1:].sum(axis='columns')
fastWeekendStation.index = [fastWeekend.iloc[:, 0]]
print(fastWeekendStation)

#급행 휴일 시간별 혼잡도
fastWeekendTime = fastWeekend.drop('구분', axis='columns').sum(axis='rows')
print(fastWeekendTime)

#급행 평일 역별 혼잡도 그래프
plt.figure('급행 평일 역별 혼잡도')
fastWeekdayStation.plot(kind='bar')
plt.xlabel('역', loc='right')
plt.ylabel('혼잡도 합', loc='top')

#급행 평일 시간별 혼잡도 그래프
plt.figure('급행 평일 시간별 혼잡도')
fastWeekdayTime.plot(kind='line')
plt.xlabel('시간', loc='right')
plt.ylabel('혼잡도 합', loc='top')

#급행 휴일 역별 혼잡도 그래프
plt.figure('급행 휴일 역별 혼잡도')
fastWeekendStation.plot(kind='bar')
plt.xlabel('역', loc='right')
plt.ylabel('혼잡도 합', loc='top')

#급행 휴일 시간별 혼잡도 그래프
plt.figure('급행 휴일 시간별 혼잡도')
fastWeekendTime.plot(kind='line')
plt.xlabel('시간', loc='right')
plt.ylabel('혼잡도 합', loc='top')

plt.show()