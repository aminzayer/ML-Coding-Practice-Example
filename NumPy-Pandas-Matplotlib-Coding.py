
"""""""""""
NumPy Coding

"""""""""""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

NumP_Array = np.array([[1, 2, 3], [4, 6, 7]])
NP1 = np.array([[1, 3], [4, 5]])
NP2 = np.array([[3, 4], [5, 7]])
MNP = NP1@NP2
MNP3 = np.dot(NP1, NP2)
MNP2 = NP1*NP2
MNP4 = np.multiply(NP1, NP2)
Sum1 = NP1+NP2
Sub1 = NP1-NP2
Sub2 = np.subtract(NP1, NP2)
np.sum(NP1)
Broad_Nump = NP1+3
NP3 = np.array([[3, 4]])
NP1+NP3
D = np.divide([12, 14, 16], 5)
D = np.floor_divide([12, 14, 16], 5)
np.math.sqrt(10)
ND = np.random.standard_normal((3, 4))
UD = np.random.uniform(1, 12, (3, 4))

# Generate Float No.
np.random.rand()
# Generate Integer No.
Random_Ar = np.random.randint(1, 50, (2, 5))
Ze = np.zeros((3, 4))
Ones = np.ones((3, 4))
Filter_Ar = np.logical_and(Random_Ar > 30, Random_Ar < 50)
F_Random_Ar = Random_Ar[Filter_Ar]
Data_N = np.array([1, 3, 4, 5, 7, 9])
Mean_N = np.mean(Data_N)
Median_N = np.median(Data_N)
Var_N = np.var(Data_N)
SD_N = np.std(Data_N)
NumP_Array = np.array([[1, 2, 3], [4, 6, 7]])
Var_Nump = np.var(NumP_Array, axis=1)
Var_Nump2 = np.var(NumP_Array, axis=0)


"""""""""
Pandas & Series Coding

"""""""""

Age = pd.Series([10, 20, 30, 40], index=['age1', 'age2', 'age3', 'age4'])
Age.age3
Filtered_Age = Age[Age > 10]


# Calling Values of the Series
Age.values
# Calling Indices of the Series
Age.index
Age.index = ['A1', 'A2', 'A3', 'A4']
Age.index

"""""""""
DataFrame

"""""""""
DF = np.array([[20, 10, 8], [25, 8, 10], [27, 5, 3], [30, 9, 7]])
Data_Set = pd.DataFrame(DF)
Data_Set = pd.DataFrame(DF, index=['S1', 'S2', 'S3', 'S4'])
Data_Set = pd.DataFrame(DF, index=['S1', 'S2', 'S3', 'S4'], columns=[
                        'Age', 'Grade1', 'Grade2'])
Data_Set['Grade3'] = [9, 6, 7, 10]
Data_Set.loc['S2']
Data_Set.loc[1][3]
Data_Set.iloc[1][3]
Data_Set.iloc[1, 3]
Data_Set.iloc[:, 0]
Data_Set.iloc[:, 3]
Filtered_Data = Data_Set.iloc[:, 1:3]
Data_Set.drop('Grade1', axis=1)
Data_Set = Data_Set.replace(10, 12)
Data_Set = Data_Set.replace({12: 10, 9: 30})
Data_Set.head(3)
Data_Set.tail(2)
Data_Set.sort_values('Grade1', ascending=True)
Data_Set.sort_index(axis=0, ascending=False)
Data = pd.read_csv('Data_Set.csv')

"""""""""
Visualization with Matplotlib

"""""""""
Year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]


Temp_I = [0.72, 0.61, 0.65, 0.68, 0.75, 0.90, 1.02, 0.93, 0.85, 0.99, 1.02]

plt.plot(Year, Temp_I)
plt.xlabel('Year')
plt.ylabel('Temp_Index')
plt.title('Global Warming', {'fontsize': 12, 'horizontalalignment': 'center'})
plt.show()


Month = ['Jan', 'Feb', 'March', 'April', 'May',
         'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

Customer1 = [12, 13, 9, 8, 7, 8, 8, 7, 6, 5, 8, 10]

Customer2 = [14, 16, 11, 7, 6, 6, 7, 6, 5, 8, 9, 12]


plt.plot(Month, Customer1)
plt.plot(Month, Customer2)
plt.show()


plt.plot(Month, Customer1, color='red', label='Customer1', marker='o')
plt.plot(Month, Customer2, color='blue', label='Customer2', marker='^')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Building Consumption')
plt.legend(loc='upper right')
plt.show()

plt.subplot(1, 2, 1)
plt.plot(Month, Customer1, color='red', label='Customer1', marker='o')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Building Consumption of Customer1')
plt.show()

plt.subplot(1, 2, 2)
plt.plot(Month, Customer2, color='blue', label='Customer2', marker='^')
plt.xlabel('Month')
plt.title('Building Consumption of Customer2')
plt.show()


plt.scatter(Month, Customer1, color='red', label='cutomer1')
plt.scatter(Month, Customer2, color='blue', label='cutomer2')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Scatter Plot of Building Consumption')
plt.grid()
plt.legend()
plt.show()


plt.hist(Customer1, bins=10, color='green')
plt.ylabel('Elec Consumption')
plt.title('Histogram')
plt.show()

plt.bar(Month, Customer1, width=0.8, color='b')
plt.show()


plt.bar(Month, Customer1, color='red', label='cutomer1')
plt.bar(Month, Customer2, color='blue', label='cutomer2')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Bar Chart')
plt.legend()
plt.show()

bar_width = 0.4

Month_b = np.arange(12)

plt.bar(Month_b, Customer1, bar_width, color='blue', label='Customer1')

plt.bar(Month_b+bar_width, Customer2, bar_width,
        color='red', label='Customer2')

plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Bar Chart')
plt.xticks(Month_b + (bar_width)/12, ('Jan', 'Feb', 'March', 'April',
           'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

plt.legend()
plt.show()


plt.xticks(Month_b + (bar_width)/12, ('Jan', 'Feb', 'March', 'April',
           'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


plt.boxplot(Customer1, notch=False, vert=True)

plt.boxplot([Customer1, Customer2], patch_artist=True,
            boxprops=dict(facecolor='red', color='red'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='blue'),
            medianprops=dict(color='yellow'))

plt.show()