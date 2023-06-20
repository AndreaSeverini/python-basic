# Import the pandas library, a powerful tool for data manipulation and analysis.
# Pandas is built on the Numpy package and its primary data structure is the DataFrame.
# DataFrames are essentially multidimensional arrays with attached row and column labels.
import pandas

# We're creating a DataFrame from a list of lists. Each sub-list represents a row in the DataFrame.
# The 'columns' parameter allows us to name the columns.
data_frame = pandas.DataFrame([['Andrea', 'Severini', '29'], ['Luca', 'Panzeri', '33']],
                              columns=['Name', 'Surname', 'Age'])
print(data_frame)

# We can also create a DataFrame from a dictionary where the keys become the column names,
# and the associated values become the data for those columns.
data_frame_2 = pandas.DataFrame({'Name': ['Andrea', 'Luca'],
                                 'Surname': ['Severini', 'Panzeri'],
                                 'Age': ['29', '33']})

print(data_frame_2)

# Here, we're verifying the types of our two DataFrames, just to confirm that we've successfully created DataFrame objects.
print(type(data_frame), type(data_frame_2))

# We can perform various operations on DataFrame columns. Here, we're using the .max() method to find the maximum 'Age'.
# Note that since 'Age' is currently stored as a string, max() will return the maximum lexicographic value,
# not the maximum numerical value. To get the numerical maximum, you'd need to convert 'Age' to an integer or float first.
print(data_frame.Age.max())

# If you're curious to see all available methods and attributes for a DataFrame object, you can use the dir() function.
print(dir(data_frame))

# pandas can read data from a variety of formats. Here, we're reading data from a CSV file into a DataFrame using read_csv().
books_data_frame = pandas.read_csv('Books.csv')
print(books_data_frame)

# We can also read data from an Excel file into a DataFrame using read_excel().
# Note: You'll need the openpyxl or xlrd library installed to use this function.
books_excel_data_frame = pandas.read_excel('Books.xls')
print(books_excel_data_frame)

# Finally, we're reading data from a JSON file into a DataFrame using read_json().
# We're specifying the encoding as 'utf-8-sig' to handle a potential BOM (Byte Order Mark) in the file.
books_json_data_frame = pandas.read_json('Books.json', encoding='utf-8-sig')
print(books_json_data_frame)

# Here we're using DataFrame's .loc method to slice the DataFrame.
# We're selecting rows 2 through 5, and columns from 'Author' to 'Year'.
df = books_json_data_frame.loc[2:5,"Author":"Year"]
print(df)

# Here we're using .loc to select all rows of the 'Author' column.
df2 = books_json_data_frame.loc[:,"Author"]
print(df2)

# DataFrame's .iloc method allows us to slice the DataFrame using integer indexes.
# Here we're selecting rows 2 through 5, and the column at index 3.
df3 = books_json_data_frame.iloc[2:5,3:4]
print(df3)

# The .drop method allows us to remove a column or row from the DataFrame.
# Here we're removing the 'Author' column. axis=1 means we're dropping a column, not a row.
df4 = books_json_data_frame.drop("Author", axis=1)
print(df4)

# We can add a new column to the DataFrame by simply assigning values to it like this.
# Here we're creating a new column 'Numbers' and populating it with the numbers 1 through 10.
df4['Numbers'] = [1,2,3,4,5,6,7,8,9,10]
print(df4)

# We can perform operations on DataFrame columns directly.
# Here we're adding 10 to each number in the 'Numbers' column.
df4['Numbers'] = df4['Numbers'] + 10
print(df4)

# The .T attribute is used to transpose the DataFrame, i.e., switch the rows and columns.
dff = books_json_data_frame.T
print(dff)

# We can also add new columns to the transposed DataFrame.
# Here we're adding a new column '10' and populating it with the given values.
dff["10"] = ["Mockingbird", "Franz", "1980", "Action"]
print(dff)

# Finally, we transpose the DataFrame again to return it to its original orientation.
dff = dff.T
print(dff)
