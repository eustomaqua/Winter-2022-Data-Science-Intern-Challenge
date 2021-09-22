# Challenge Solutions

## Question 1

The solution code is included in "thought_process.py".

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

We could know from the data set that:

- There are 100 different shops.
- There are 301 different users.
- There are 3 methods to pay for merchandises, including debit, credit_card, and cash.

Besides, we could describe the price information of different shops using histograms since each shop sells only one model of shoe. 
Notice that there are outliers: one is the shop (id:78) selling expensive sneakers with the price of $25725, the other is the shop (id:42), selling 34063 sneaker items in 51 orders.

Some results are included in the folder "Question1-b".


### answer c

The value is that we could analyze the price of sneakers, the sales volumes, and the total income in different shops. So we would know the consumption level of users and provide users suggestions about similar goods, such as similar prices and so on. We could also provide shops suggestions about what sneakers they should sell, for example, selling too expensive sneakers may not be a good idea.


## Question 2

### instruction

access the data set
```SQL
SELECT * FROM Customers;
```

### answer a

```SQL
SELECT * FROM [Orders] WHERE ShipperID = 1
```

There are 54 orders shipped by Speedy Express in total.

![](Question2_answer_a.png)

### answer b

```SQL
SELECT EmployeeID as Employee, COUNT(*) as Counts FROM [Orders] GROUP BY Employee
SELECT * FROM [Employees] WHERE EmployeeID='4'
```

The EmployeeID with the most orders is 4, who has 40 orders.
The employee's last name is Peacock and the first name is Margaret.

![](Question2_answer_b1.png)
![](Question2_answer_b2.png)

### answer c

To find the answer, we need the information from three tables, that is, `Customers`, `Orders`, `OrderDetails`, and `Products`.

- The 'Customers' table has the column named `Country`, so we could find the costomers who came from Germany.
- Both the 'Customers' table and the 'Orders' table have the column named `CustomerID`.
- Both the 'Orders' table and the 'OrderDetails' table have the column named `OrderID`.
- The 'OrderDetails' table has the column named `ProductID`, and so is the table 'Products'.

We'd like to merge these three tables together and then discover the most popular merchandise, using the column named 'ProductID' in the table 'OrderDetails'. As long as we obtain the most popular ProductID, we could get the merchandise from the table `Products`.

Step 1. Join three tables ('OrderDetails', 'Orders', and 'Customers') and find the orders shipped to Germany.
```SQL
SELECT * FROM [OrderDetails]
LEFT JOIN Orders ON Orders.OrderID=OrderDetails.OrderID
LEFT JOIN Customers ON Customers.CustomerID=Orders.CustomerID
WHERE Customers.Country='Germany'
```

Step 2. Query the most popular product's ID. The answer is `ProductID=31` which has 5 orders.
```SQL
SELECT ProductID as product, COUNT(*) as counts FROM [OrderDetails]
LEFT JOIN Orders ON Orders.OrderID=OrderDetails.OrderID
LEFT JOIN Customers ON Customers.CustomerID=Orders.CustomerID
WHERE Customers.Country='Germany'
GROUP BY ProductID
```

Step3. View the information of products and find the exact merchandise. The answer is `ProductName=Gorgonzola Telino`.
```SQL
SELECT * FROM [Products] WHERE ProductID='31'
```

In summary, the product named 'Gorgonzola Telino' is ordered the most by customers in Germany. 
Here is more information about this product:
- ProductID: 31
- ProductName: Gorgonzola Telino
- SupplierID: 14
- CategoryID: 4
- Unit: 12 - 100 g pkgs
- Price: 12.5
