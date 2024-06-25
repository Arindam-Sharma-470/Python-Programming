import pandas as pd #Importing pandas

#Creating Series
#Creating series from dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}

myVar1 = pd.Series(calories, index = ["day1", "day2"]) #Only '420' and '380' are included
print(myVar1)
print(pd.__version__) #Pandas Version

#Creating series in pandas from a list
a = [1, 2, 3]
myVar2 = pd.Series(a, index = ['a', 'b', 'c']) # Creating labels
#If labels are not created explicitly then the indices of elements act as labels
print(myVar2) #Printing the series
print(myVar2['b']) #Accessing series through labels

#Creating DataFrames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "proteins": [24, 35, 56],
  "carbohydrates": [55, 74, 88]
}
myVar3 = pd.DataFrame(data, index = ['day1', 'day2', 'day3']) #Named Indices/Labels
print(myVar3)

#Accessing data
print(myVar3.loc['day3']) #Accessing row 2 -> Returns a series
print(myVar3.loc[['day2', 'day3']]) #Returns a DataFrame

#If labels are not given then the indices act as the labels
#print(myVar3.loc[2]) #Accessing row 3 -> Returns a series
#print(myVar3.loc[[1, 2]]) #Returns a DataFrame

#Reading CSV files
myVar4 = pd.read_csv("data.csv")
print(myVar4.to_string()) #to_string() attribute prints the total data set
print("Before setting max_rows and printing without to_string() attribute:")
print(myVar4) # This would not print the total data set. In this case, Pandas prints only
#the first five rows and the last five rows
print(pd.options.display.max_rows) #By default the value is set to 60. It means that
#if there are more than 60 rows in my dataset then only first 5 rows and last 5 rows along
#with the respective headers would be printed.
#It also means that if no. of rows in my dataset <= 60 then even without the
#to_string() attribute the total dataset would be printed.
pd.options.display.max_rows = 1000 #Here the maximum no. of rows is set to 1000. It means
#that if the dataset contains more than 1000 rows then first 5 rows and last 5 rows 
#along with the respective headers would be printed.
print("After setting max_rows and printing without to_string() attribute:")
print(myVar4)

#Reading JSON files
myVar5 = pd.read_json("data.json")
print(myVar5) #the max_rows have been set to 1000 earlier so using to_string() 
#attribute is not necessary

#Viewing Data\

#The head() method returns the headers and 
# a specified number of rows, starting from the top.
print(myVar4.head(6))
#if the number of rows is not specified, the head() method will return the top 5 rows.

#The tail() method returns the headers and a 
# specified number of rows, starting from the bottom.
print(myVar4.tail(6))
#if the number of rows is not specified, the tail() method will return the bottom 5 rows.

print(myVar4.info()) #Provides information about the dataset

#Reading a text file. sep needs to be provided and sep is set to comma by default.
#myVar = pd.read_csv("sample.txt", sep = '\s')
#print(myVar6)

#Reading excel files
#myVar = pd.read_excel("small.xlsv")
#For importing multiple excel sheets:
#myVar = pd.read_excel("small.xlsv", sheet_name = 1)
#Python uses '0' indexing i.e. first sheet is numbered as sheet 0 and so on.
#In case of multiple sheets only the 'sheet_name' parameter is to be provided and
#numbers or strings can be passed in the 'sheet_name'

#Outputting dataframes

#print(myVar.to_csv("sample.csv"), index = False) 
#index- True implies writing the dataframe's index

#print(myVar.to_csv("sample.txt", sep = ' ')) #sep is necessary

#print(myVar.to_json("sample.json"))

#print(myVar.to_excel("sample.xlsv"))

#print(myVar5.to_json("myVar.json"))

#Updating specific cells
myVar3.at['day1', 'calories'] = 89
myVar3.iat[1, 1] = 100
print(myVar3)

#Updating an entire row
myVar3.loc['day1'] = [421, 25, 55, 56]
print(myVar3)

#Updating an entire column
myVar3['calories'] = [44, 45, 74]
print(myVar3)

#Updating based on a condition
myVar3.loc[myVar3['calories'] > 30, 'carbohydrates'] = 99
print(myVar3)

#Updating based on a function
myVar3['proteins'] = myVar3['carbohydrates'].apply(lambda x: x + 5)
print(myVar3)

#Adding headers
data = [
   [420, 380, 390],
   [50, 40, 45],
   [24, 35, 56],
   [55, 74, 88]
]
myVar6 = pd.DataFrame(data) 
#myVar3.columns = ['First', 'Second', 'Third']
#Another method
myVar6 = myVar6.rename(columns={0:'First', 1: 'Second', 2: 'Third'})
print(myVar6)

#No. of rows and columns
no_of_rows = len(myVar6)
print("No. of rows in myVar6: ", no_of_rows)

num = myVar6.shape
num_list = list(num)
no_of_rows_and_columns = pd.DataFrame(num_list, index = ('Rows', 'Columns'))
no_of_rows_and_columns.columns = ['Shape']
print(no_of_rows_and_columns)

#Filtering data
print("Filtering data: ")
filtered_myVar6 = myVar6[myVar6['First'] > 50]
print(filtered_myVar6)

#Sorting data
print("Sorting data: ")
sort_myVar6 = myVar6.sort_values(by = 'Third')
print(sort_myVar6)

#Grouping data
print("Grouping data")
group_myVar6 = myVar6.groupby("First").mean()
print(group_myVar6)

#Removing duplicates
myVar6.iat[3, 0] = 50
myVar6_cleaned = myVar6.drop_duplicates(subset="First", keep="first")
print(myVar6_cleaned)

#Dropping missing data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', None, 'David', 'Eve', None],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eve@example.com', 'frank@example.com']
}

customers = pd.DataFrame(data)

# Remove rows where 'name' column has missing values
customers_cleaned = customers.dropna(subset=['name'])

print(customers_cleaned)

#Changing data type of column
data = {
    'student_id': [1, 2],
    'name': ['Ava', 'Kate'],
    'age': [6, 15],
    'grade': [73.0, 87.5]
}

students = pd.DataFrame(data)

# Convert the 'grade' column from float to int
students['grade'] = students['grade'].astype(int)

print(students)

#Fill in missing value
data = {
    'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
    'quantity': [None, None, 779, 849],
    'price': [135, 821, 9319, 3051]
}

products = pd.DataFrame(data)

# Fill missing values in the 'quantity' column with 0
products['quantity'] = products['quantity'].fillna(0)

# Convert the 'quantity' column to int if needed
products['quantity'] = products['quantity'].astype(int)

print(products)

#Concatenate dataframes
data1 = {
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
}

data2 = {
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenate the two DataFrames vertically
result = pd.concat([df1, df2], ignore_index=True)
#ignore_index = True reindexes the concatenated dataframe
print(result)

#Pivot the data
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(index='month', columns='city', values='temperature', aggfunc='max')

# Example DataFrame
data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}

weather = pd.DataFrame(data)

# Pivot the DataFrame
pivoted_weather = pivotTable(weather).reset_index()

# Rename columns for better readability
pivoted_weather.columns.name = None

print(pivoted_weather)

#Melting
data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

report = pd.DataFrame(data)

# Reshape the DataFrame from wide to long format using melt
melted_report = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

print(melted_report)

#Use melt function: The melt function is used to reshape the DataFrame from wide to long format.
#id_vars=['product'] specifies that product column should remain as identifier variables.
#var_name='quarter' specifies the new column name for the melted columns (quarter_1, quarter_2, etc.).
#value_name='sales' specifies the new column name for the values that are melted.

#Method Chaining
data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

animals = pd.DataFrame(data)

# Filter animals weighing more than 100 kilograms
filtered_animals = animals[animals['weight'] > 100]

# Sort by weight in descending order
sorted_animals = filtered_animals.sort_values(by='weight', ascending=False)
print(sorted_animals)
df = pd.DataFrame(sorted_animals['name'])
print(df)