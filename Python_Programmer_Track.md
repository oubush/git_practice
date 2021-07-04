
# Python Programmer Track (DataCamp, 2021)

## Introduction to Data Science in Python

- importing a module, creating variables
- functions: positional, keyword arguments
- working with pandas: load data, select columns, select rows with logic
- plotting data
```
from matplotlib import pyplot as plt
plt.plot(x_values, y_values)
plt.show()
```
- multiple lines
```
from matplotlib import pyplot as plt
plt.plot(data1.x_values, data1.y_values)
plt.plot(data2.x_values, data2.y_values)
plt.show()
```
- axes and title labels
```
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title")
```
- legends
```
plt.plot(x, y1, label="label1")
plt.plot(x, y2, label="label2")
plt.plot(x, y3, label="label3")
plt.legend()
```
- arbitrary text
```
plt.text(xcoord, ycoord, "Text Message")
```
- change font size or color
```
plt.title("Plot title", fontsize=20)
plt.legend(color="green")
```
- change line style or width, add markers
```
plt.plot(x, y, linewidth=1, linestyle='-', marker='x')
```
- setting a style
```
plt.style.use(style_name)
style_name = {'fivethirtyeight', 'ggplot', 'seaborn', 'default}
```
- a scatter plot
```
plt.scatter(x, y, color='green', marker='s', alpha=0.1)
```
- a bar chart
```
plt.bar()
plt.barh()
```
- adding error bars
```
plt.bar(df.x, df.y, yerr=df.error)
```
- stacked bar charts
```
plt.bar(df.precinct, df.dog, label='Dog')
plt.bar(df.precinct, df.cat, bottom=df.dog, label='Cat')
plt.legend()
plt.show()
```
- a histogram
```
plt.hist(data, bins=nbins, range=(xmin, xmax), density=True/False)
```

## Data Types for Data Science in Python

- Lists
```
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
```
- Reading from a file using CSV reader
`csv.reader()` reads a file object and returns the lines from the file as tuples

```
import csv
csvfile = open('filename.csv', 'r')
for row in csv.reader(csvfile):
    print(row)
csvfile.close()
```
- Counter: special dictionary used for counting data, measuring frequency
```
from collections import Counter
counter = Counter(data)
counter..most_common(N)  # returns the counter values in descending order
```
from collections:
- defaultdict 
- OrderedDict
- namedtuple

## Data Manipulation with pandas

- Exploring a DataFrame
```
df.head()
df.info()
df.shape
df.describe()
df.values
df.columns
df.index
```
- sorting
```
df.sort_values(by=..., ascending=True/False)
```
- summary statistics
```
df['col_name'].median()
df['col_name'].mode()
df['col_name'].min()
df['col_name'].max()
df['col_name'].var()
df['col_name'].std()
df['col_name'].sum()
df['col_name'].quantile()
df['col_name'].agg(func)
```
- cumulative statistics
```
df['col_name'].cumsum()
df['col_name'].cummax()
df['col_name'].cummin()
df['col_name'].cumprod()
```
- duplicates
```
df.drop_duplicates(subset='col_name')
```
- counting, proportions
```
df.value_counts()
df.value_counts(normalize=True)
```
- grouped summary statistics
```
df.groupby("col_name_1")["col_name_2"].mean()
df.groupby("col_name_1")["col_name_2"].agg([min, max, sum])
```
- pivot tables
```
df.pivot_table(values="col_name_1", index="col_name_2")  # default: mean
df.pivot_table(values="col_name_1", index="col_name_2", aggfunc=...)
df.pivot_table(values="col_name_1", index="col_name_2", colums="col_name_3")
df.pivot_table(values="col_name_1", index="col_name_2", colums="col_name_3", fill_value=0)  # filling missing values
df.pivot_table(values="col_name_1", index="col_name_2", colums="col_name_3", fill_value=0, margins=True)  # summing
```
- slicing
```
df.columns
df.index
df = df.set_index('col_name')
df.reset_index()
df.reset_index(drop=True)
df.sort_index()
```
- visualization
```
df.hist()
df.plot(x='...', y='...', kind={'bar', 'line', 'scatter'}, title='...', rot=N)
```
- missing values
```
df.isna()
df.isna().any()
df.isna().sum()
df.dropna()
df.fillna(0)
```

## Python Data Science Toolbox (Part 1)

- user-defined functions
```
def func():
    ...
    return ...
```
- scopes searched: local / enclosing functions / global / built-in
- default arguments
- flexible arguments: `*args`
- flexible key word arguments: `**kwargs`
- Anonymous functions: `lambda x: x**2`
- errors and exceptions
```
raise ValueError
```

```
try:
    ...
except TypeError:
    ...
```

## Python Data Science Toolbox (Part 2)

- Iterables: lists, strings, dictionaries, file connections
- `iter()` method creates an iterator
- Iterator produces next value with next()
```
word = 'Da'
it = iter(word)
next(it)
'D'
next(it)
'a'
```
- Iterating at once with `*`
- Iterating over file connections by lines
- using `enumerate()`
- using `zip()`
- print zip with `*`
- if too much data, load data in chunks
```
for chunk in pd.read_csv('data.csv', chunksize=1000):
    ...
```
- list comprehensions:   
`[output expression for iterator variable in iterable]`
```
new_nums = [num + 1 for num in nums]
pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
```
- conditionals on the iterable
```
[num ** 2 for num in range(10) if num % 2 == 0]
```
- conditionals on the output expression
```
[num ** 2 if num % 2 == 0 else 0 for num in range(10)]
```
- advanced list comprehension
```
[output expression +
conditional on output for iterator variable in iterable +
conditional on iterable]
```
- dict comprehensions
```
pos_neg = {num: -num for num in range(9)}
```
- generator expressions: Use `( )` instead of `[ ]`
```
(2 * num for num in range(10))
```
- list comprehension returns a list, generator returns a generator object
- generator functions: yields a sequence of values instead of returning a single value
```
def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1
```

## Writing Efficient Python Code

- efficient: minimal completion time + minimal resource consumption
- focus on readability
- using Python's constructs as intended
- The Python Standard Library: built-in types, built-in functions, built-in modules
- `range()`, `enumerate()`, `map()`
- NumPy arrays: broadcasting, boolean indexing

- See all available magic commands with `%lsmagic`
- Calculate runtime with IPython magic command `%timeit` (line magic)
- Setting the number of runs(`-r`) and/or loops (`-n`)
```
%timeit -r2 -n10 ...
```
- cell magic: `%%timeit`
- Saving the output to a variable (`-o`)
```
times = %timeit -o ...
times.timings
times.best
times.worst
```
- code profiling: runtime (Detailed stats on frequency and duration of function calls)
- Line-by-line analyses
- Package used: `line_profiler` 
```
%load_ext line_profiler
%lprun -f
```
- Code profiling: memory (Detailed stats on memory consumption)
- Package used: `memory_profiler`
```
%load_ext memory_profiler
%mprun -f
```

- `collections` module: Specialized container datatypes
```
namedtuple : tuple subclasses with named ,elds
deque : list-like container with fast appends and pops
Counter : dict for counting hashable objects
OrderedDict : dict that retains order of entries
defaultdict : dict that calls a factory function to supply missing values
```
- `itertools` module: Functional tools for creating and using iterators
```
Infinite iterators: count, cycle, repeat
Finite iterators: accumulate, chain, zip_longest, etc.
Combination generators: product, permutations, combinations
```
- `set` theory
```
intersection(): all elements that are in both sets
difference(): all elements in one set but not the other
symmetric_difference(): all elements in exactly one set
union(): all elements that are in either set
```
- Fast membership testing: Using the `in` operator
- eliminating loops: with built-ins, with built-in modules, with NumPy
- Best practice for iterating over a pandas DataFrame:
    - Iterating with `.iloc`
    - Iterating with `.iterrows()`
    - Iterating with `.itertuples()`
    - pandas `.apply()` method
    - use vectorization
## Working with Dates and Times in Python

```
from datetime import date
```
- Attributes of a date: `.year`, `.month`, `.day`, `.weekday()`
- Weekdays in Python
```
0 = Monday
1 = Tuesday
2 = Wednesday
...
6 = Sunday
```
- Math with dates
```
from datetime import timedelta
```
- ISO format: YYYY-MM-DD
```
d.isoformat()  # Turning dates into ISO format
```
- Turning dates into strings: `strftime`
```
print(d.strftime("%Y/%m/%d"))
2017/01/05
```
- Dates and Times
```
from datetime import datetime
```
```
dt = datetime(year=2017, month=10, 
day=1, hour=15, minute=23, second=25, 
microsecond=500000)
```
- Replacing parts of a datetime
```
dt_hr = dt.replace(minute=0, second=0, microsecond=0)
```
- Printing datetimes
```
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
2017-12-30 15:19:13

print(dt.strftime("%H:%M:%S on %d/%m/%Y"))
15:19:13 on 2017/12/30

print(dt.isoformat())
2017-12-30T15:19:13  # ISO 8601 Format
```
- Parsing datetimes with `strptime`
```
dt = datetime.strptime("12/30/2017 15:19:13",
"%m/%d/%Y %H:%M:%S")
```
- Parsing datetimes with Pandas
```
# A timestamp
ts = 1514665153.0
# Convert to datetime and print
print(datetime.fromtimestamp(ts))
```
- Working with durations
```
# Create example datetimes
start = datetime(2017, 10, 8, 23, 46, 47)
end = datetime(2017, 10, 9, 0, 10, 57)
# Subtract datetimes to create a timedelta
duration = end - start
# Subtract datetimes to create a timedelta
print(duration.total_seconds())
```
- Creating timedeltas
```
delta1 = timedelta(seconds=1)
delta2 = timedelta(days=1, seconds=1)
delta3 = timedelta(weeks=-1)
```
- UTC offset
```
# Import relevant classes
from datetime import datetime, timedelta, timezone
# US Eastern Standard time zone
ET = timezone(timedelta(hours=-5))
# Timezone-aware datetime
dt = datetime(2017, 12, 30, 15, 9, 3, tzinfo = ET)
print(dt)
'2017-12-30 15:09:03-05:00'
# India Standard time zone
IST = timezone(timedelta(hours=5, minutes=30))
# Convert to IST
print(dt.astimezone(IST))
'2017-12-31 01:39:03+05:30'
```
- Adjusting timezone vs changing tzinfo
```
print(dt)
'2017-12-30 15:09:03-05:00'
print(dt.replace(tzinfo=timezone.utc))
'2017-12-30 15:09:03+00:00'
# Change original to match UTC
print(dt.astimezone(timezone.utc))
'2017-12-30 20:09:03+00:00'
```
- Time zone database: Format: 'Continent/City'
```
from dateutil import tz
# Eastern time
et = tz.gettz('America/New_York')
```
- Loading datetimes with parse_dates
```
# Import W20529's rides in Q4 2017
rides = pd.read_csv('capital-onebike.csv',
parse_dates = ['Start date', 'End date'])
# Or:
rides['Start date'] = pd.to_datetime(rides['Start date'],
format = "%Y-%m-%d %H:%M:%S")
```
- Summarizing data in Pandas
```
rides['Duration'].mean()
rides['Duration'].sum()
rides['Duration'].sum() / timedelta(days=91)
rides['Duration seconds'] = rides['Duration'].dt.total_seconds()
# Average duration by month
rides.resample('M', on = 'Start date')['Duration seconds'].mean()
# First ride per group
rides.groupby('Member type').first()
rides['Start date'].dt.year
rides['Start date'].dt.weekday_name
```
- Timezones in Pandas
```
rides['Start date'].dt.tz_localize('America/New_York')

# Handle ambiguous datetimes
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
```

## Regular Expressions in Python
- Adjusting cases  
```
# Converting to lowercase
my_string.lower()
# Converting to uppercase
my_string.upper()
# Capitalizing the first character
my_string.capitalize()
```
- Splitting
```
my_string.split()
my_string.rsplit()
my_string.splitlines()
```
- Joining
```
separator.join(itarable)
```
- Stripping characters
```
my_string.strip()
my_string.rstrip()  # Remove characters from the right end
my_string.lstrip()  # Remove characters from the left end
```
- Finding substrings
```
string.find(substring)  # Returns -1 if substring not found
string.index(substring)  # Raises an exception if substring not found
string.count(substring)
```
- Replacing substrings
```
string.replace(old, new)
```
- Methods for string formatting:  
1. Positional formatting
```
'text {}'.format(value)
str.format()
# Specify data type to be used: {index:specifier}
```
3. Formatted string literals (Add prefix `f` to string)
```
f'literal string {expression}'
```
5. Template method
```
from string import Template
my_string = Template('Data science has been called $identifier')
my_string.substitute(identifier="sexiest job of the 21st century")
```
- f-strings are always advisable above all methods

- REGar EXressions or regex: the `re` module
```
import re
re.findall(r'regex', string)  # Find all matches of a pattern
re.split(r'regex', string)  # Split string at each match
re.sub(r'regex', new, string)  # Replace one or many matches with a string
```
- Supported metacharacters

Metacharacter | Meaning
--- | ---
\d | Digit
\D | Non-digit
\w | Word
\W | Non-word
\s | Whitespace
\S | Non-Whitespace

- Quantifiers  
Once or more: `+`  
Zero times or more: `*`  
Zero times or once: `?`  
n times at least, m times at most : `{n, m}`  

- Immediately to the left  
`r"apple+"` : `+` applies to `e` and not to `apple`

- Looking for patterns
```
re.search(r'regex', string)
re.match(r'regex', string)
```

- Special characters  
Match any character (except newline): `.`  
Start of the string: `^`  
End of the string: `$`  
Escape special characters: `\`  

- OR operator  
Character: `|`  
Set of characters: `[ ]`, example: `[a-zA-Z]`  
`^` transforms the expression to negative: `[^ ]`, example `[^0-9]`

- Greedy vs. non-greedy matching
**Greedy**: match as many characters as possible  
Return the longest match  
Standard quantifiers are greedy by default: `*`, `+`, `?`, `{num, num}`  

**Lazy**: match as few characters as needed*  
Returns the shortest match  
Append `?` to greedy quantifiers

- Advanced: grouping, capturing, altrnation. backreferences, lookaround

## Web Scraping in Python
## Writing Functions in Python
## Introduction to Shell
## Parallel Programming with Dask in Python
## Software Engineering for Data Scientists in Python
## Developing Python Packages
## Unit Testing for Data Science in Python
## Object-Oriented Programming in Python
