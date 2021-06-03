
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
