# Import the pandas library, a high-level data manipulation tool developed by Wes McKinney.
# It is built on the Numpy package and its key data structure is called the DataFrame.
# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
import pandas

# Here, we're creating a DataFrame from a list of lists. Each inner list is treated as a row in the DataFrame.
# The 'columns' parameter allows us to specify the column names.
data_frame = pandas.DataFrame([['Andrea', 'Severini', '29'], ['Luca', 'Panzeri', '33']],
                              columns=['Name', 'Surname', 'Age'])
print(data_frame)

# We can also create a DataFrame from a dictionary. The keys of the dictionary become the column names,
# and the values (which must be lists) become the data for those columns.
data_frame_2 = pandas.DataFrame({'Name': ['Andrea', 'Luca'],
                                 'Surname': ['Severini', 'Panzeri'],
                                 'Age': ['29', '33']})

print(data_frame_2)

# Let's print the types of our two DataFrames. This should confirm that both variables are pandas DataFrame objects.
print(type(data_frame), type(data_frame_2))

# We can perform operations on columns in a DataFrame. For example, we can use the .max() method to find
# the maximum value in a column. Here, we find the maximum 'Age'.
# However, as the 'Age' column is of string type in this case, max() will give the lexicographically largest value,
# which might not be the actual maximum numeric value. You would need to convert 'Age' to int or float for accurate results.
print(data_frame.Age.max())

# Here we are printing all available methods and attributes for a DataFrame object, for us to see what we can do with it.
print(dir(data_frame))

# The pandas library makes it easy to read data from a variety of formats. Here, we read data from a CSV file.
# The read_csv() function takes the file path of the CSV file and converts it into a DataFrame.
books_data_frame = pandas.read_csv('Books.csv')
print(books_data_frame)

# Similarly, we can read data from an Excel file using the read_excel() function. This function also takes a file path,
# and returns a DataFrame. This will require the openpyxl or xlrd library to be installed in your environment.
books_excel_data_frame = pandas.read_excel('Books.xls')
print(books_excel_data_frame)
