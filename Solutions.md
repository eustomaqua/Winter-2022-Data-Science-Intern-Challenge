# Challenge Solutions

## Question 1

### answer a

The original calculation did not conserder the items in each order.

We have two possible methods to evaluate the data.
```python
import numpy as np
import pandas as pd

dframe = pd.read_csv(
    "2019-Winter-Data-Science-Intern-Challenge-Data-Set.csv")


total_items = dframe['total_items'].values
order_amount = dframe['order_amount'].values
```

1. Methon 1: Calculate the price of each sneaker that these shops sell, and then calculate their average. The AOV would be $387.74.
```python
correct_aov = np.mean(np.divide(order_amount, total_items))
print("Correct calculation 1:\t", end="")
print("AOV = {:.2f}".format(correct_aov))
```
2. Method 2: Calculate the sum of all orders, and then divide it by the sum of items of all orders. The AOV would be $357.92.
```python
correct_aov = np.sum(order_amount) / np.sum(total_items)
print("Correct calculation 2:\t", end="")
print("AOV = {:.2f}".format(correct_aov))
```

### answer b


### answer c


## Question 2

### instruction

access the data set
```SQL
SELECT * FROM Customers;
```

### answer a

```SQL
SELECT * FROM [Orders]
WHERE ShipperID = 1
```

There are 54 orders shipped by Speedy Express in total.

![](Question2_answer_a.png)

### answer b

```SQL
SELECT EmployeeID as Employee, COUNT(*) as Counts FROM [Orders] GROUP BY Employee
SELECT * FROM [Employees]
```

The EmployeeID with the most orders is 4, who has 40 orders.
The employee's last name is Peacock and the first name is Margaret.

![](Question2_answer_b1.png)
![](Question2_answer_b2.png)

### answer c

```SQL

```
