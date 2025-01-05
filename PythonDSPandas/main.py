# Code for Pandas functions usage

import pandas as pd

#Series
series_values = pd.Series(list("Pandas Library"))
print(f"Series with Strings= {series_values}")
series_values = pd.Series(list([10,23,24]))
print(f"Series with list= {series_values}")
list_values = list({10,23,24,(10,8)})
series_values = pd.Series(list_values,
                          index=['id','cid','subid','pass?'])
print(f"Series with set and custom index= "
      f"{series_values}")
series_values = pd.Series(list({"Name":"PythonProgrammer", "Country":"INDIA"}))
print(f"Series with dic= {series_values}")

#Data Frames
dataFrame_values = {"Names" : pd.Series(["Rama", "Krishna", "Arjun", "Rama"]),
             "Languages" : pd.Series(["Telugu", "Tamil",  "Sanskrit"]),
             "States" : pd.Series([1 , 2, 3, 4]),
             "Leads" : pd.Series(["Rama", "Krishna", "", "Bhim"]),
             }
dataFrame = pd.DataFrame(dataFrame_values)

#print(f"Data Frame is \n{dataFrame}")
print(f"Data Frame info is \n {dataFrame.info()}")
print(f"Data Frame is \n{dataFrame} ")
print(f"Changing Data Frame rows into columns using Transpose \n {dataFrame.T}")
print(f"Retrieving Top 2 elements is {dataFrame.head(2)}")
print(f"Retrieving Last 2 elements is {dataFrame.tail(2)}")

#Printing statistical information
print(f"Statistical information by default integer {dataFrame.describe()}")
#Printing statistical information for all
print(f"Statistical information for all \n{dataFrame.describe(include='all')}")

df = pd.DataFrame({
    'Group' :['ENGG','MEDICAL','ARTS','SCIENCE'],
    'Marks' : [998,992,989,929],
    'Students' : [101,106,280,234]},
    index=['one', 'two', 'three','four']
)
print(f"Data frame values are \n {df} \n and type of df in {type(df)}")

print(f"Data frame columns are {df.columns} \n and specific column is \n"
      f"{df['Group']}")

print(f"Data frame values using index and specific columns \n "
      f"{df.loc[['two', 'three'],['Students','Marks']]}")
#TODO try with nested dictionary


# July 18