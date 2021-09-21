# coding: utf-8

import numpy as np
import pandas as pd

dframe = pd.read_csv(
    "2019-Winter-Data-Science-Intern-Challenge-Data-Set.csv")


total_items = dframe['total_items'].values
order_amount = dframe['order_amount'].values


print("Wrong calculation    :\t", end="")
print("AOV = {:.2f}".format(np.mean(order_amount)))


# correct_aov = np.sum(order_amount * total_items) / np.sum(total_items)
correct_aov = np.mean(np.divide(order_amount, total_items))
print("Correct calculation 1:\t", end="")
print("AOV = {:.2f}".format(correct_aov))

correct_aov = np.sum(order_amount) / np.sum(total_items)
print("Correct calculation 2:\t", end="")
print("AOV = {:.2f}".format(correct_aov))
