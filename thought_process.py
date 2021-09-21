# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from copy import deepcopy

print("requirements.txt")
print("numpy=={}".format(np.__version__))
print("pandas=={}".format(pd.__version__))
print("matplotlib=={}".format(mpl.__version__))
print("\n\n")

# showup_plt = True
showup_plt = False  # save


dframe = pd.read_csv(
    "2019-Winter-Data-Science-Intern-Challenge-Data-Set.csv")


total_items = dframe['total_items'].values
order_amount = dframe['order_amount'].values


print("Wrong calculation    :\t", end="")
print("AOV = {:.2f}".format(np.mean(order_amount)))


correct_aov = np.mean(np.divide(order_amount, total_items))
print("Correct calculation 1:\t", end="")
print("AOV = {:.2f}".format(correct_aov))

correct_aov = np.sum(order_amount) / np.sum(total_items)
print("Correct calculation 2:\t", end="")
print("AOV = {:.2f}".format(correct_aov))


# answer b

print("\n\n")
print("dframe.info()")
dframe.info()


print("\n")
print("Q: How many shops are there?")
print("A: There are {} different shops.".format(
    len(set(dframe['shop_id']))))
print("Q: How many users are there?")
print("A: There are {} different users.".format(
    len(set(dframe['user_id']))))

payment_method = list(set(dframe['payment_method']))
print("Q: How many payment methods are there?")
print("A: There are {} methods to pay for merchandises, "
      "including {}, and {}.".format(
          len(payment_method),
          ', '.join(payment_method[:-1]),
          payment_method[-1]))


# answer b

def plot_all_together(data):
    plt.hist(data, bins=40, normed=0, facecolor='blue',
             edgecolor='black', alpha=.7)
    plt.xlabel('Price of sneaker')
    plt.ylabel('Frequency')
    plt.title('Put all sneakers from all shops together')
    if showup_plt:
        plt.show()
    else:
        plt.savefig("Q1b_all_together.png", dpi=300)
        plt.close()
    return


plot_all_together(order_amount / total_items)


diff_shops = sorted(set(dframe['shop_id']))
diff_price = []
diff_numbr = []
diff_total_items = []
diff_total_amoun = []

for i in diff_shops:
    subdf = dframe[dframe['shop_id'] == i]

    sub_order = subdf['order_amount'].values
    sub_items = subdf['total_items'].values
    sub_price = sub_order / sub_items
    assert len(set(sub_price)) == 1
    sub_price = list(set(sub_price))[0]

    print("Shop #{:3d}: sneaker price is {}.".format(
        i, sub_price), end="")
    print("\tThere are {:2d} orders and {:3d} sold items in total.".format(
        len(sub_order), np.sum(sub_items)))

    diff_price.append(sub_price)
    diff_numbr.append(len(sub_order))
    diff_total_items.append(np.sum(sub_items))
    diff_total_amoun.append(np.sum(sub_order))


def subplot_different_shops(data, bins, text):
    plt.hist(data, bins=bins, normed=0, facecolor='blue',
             edgecolor='black', alpha=.7)
    plt.xlabel(text)
    plt.ylabel('Frequency')
    plt.title('{} in different shops'.format(text))
    if showup_plt:
        plt.show()
    else:
        plt.savefig("Q1b_diff_shops_{}.png".format(
            text.split()[-1]), dpi=300)
        plt.close()
    return


subplot_different_shops(diff_price, 200, 'Price of sneakers')
subplot_different_shops(diff_numbr, 40, 'Number of orders')
subplot_different_shops(diff_total_items, 200, 'Number of sold items')
subplot_different_shops(diff_total_amoun, 200, 'Total sold order amount')


# answer b

# We want to remove the outliers

copy_shops = deepcopy(diff_shops)
copy_price = deepcopy(diff_price)
copy_numbr = deepcopy(diff_numbr)
copy_total_items = deepcopy(diff_total_items)
copy_total_amoun = deepcopy(diff_total_amoun)

outlier_idx = copy_price.index(max(copy_price))
print("\n\n")
print("The outlier is the shop #{}, selling the sneaker with the price"
      " of ${}. There are {} items sold in {} orders, and the total amount"
      " is ${}.".format(diff_shops[outlier_idx], diff_price[outlier_idx],
                        copy_total_items[outlier_idx], copy_numbr[outlier_idx],
                        copy_total_amoun[outlier_idx]))


del copy_shops[outlier_idx]
del copy_price[outlier_idx]
del copy_numbr[outlier_idx]
del copy_total_items[outlier_idx]
del copy_total_amoun[outlier_idx]


def subplot_different_shops_without_outliers(data, text, outlier='price'):
    plt.hist(data, bins=40, normed=0, facecolor='blue',
             edgecolor='black', alpha=.7)
    plt.xlabel(text)
    plt.ylabel('Frequency')
    # plt.title('{} in different shops without outliers'.format(text))
    plt.title('{} in different shops without {} outliers'
              ''.format(text, outlier))
    if showup_plt:
        plt.show()
    else:
        plt.savefig("Q1b_{}_outlier_{}.png".format(
            outlier, text.split()[-1]), dpi=300)
        plt.close()
    return


subplot_different_shops_without_outliers(copy_price, 'Price of sneakers')
subplot_different_shops_without_outliers(copy_numbr, 'Number of orders')
subplot_different_shops_without_outliers(
    copy_total_items, 'Number of sold items')
subplot_different_shops_without_outliers(
    copy_total_amoun, 'Total sold order_amount')


# copy_shops = deepcopy(diff_shops)
# copy_price = deepcopy(diff_price)
# copy_numbr = deepcopy(diff_numbr)
# copy_total_items = deepcopy(diff_total_items)
# copy_total_amoun = deepcopy(diff_total_amoun)

outlier_idx = copy_total_items.index(max(copy_total_items))
print("")
print("The outlier is the shop #{}, selling the sneaker with the price"
      " of ${}. There are {} items sold in {} orders, and the total amount"
      " is ${}.".format(diff_shops[outlier_idx], diff_price[outlier_idx],
                        copy_total_items[outlier_idx], copy_numbr[outlier_idx],
                        copy_total_amoun[outlier_idx]))


del copy_shops[outlier_idx]
del copy_price[outlier_idx]
del copy_numbr[outlier_idx]
del copy_total_items[outlier_idx]
del copy_total_amoun[outlier_idx]


subplot_different_shops_without_outliers(
    copy_price, 'Price of sneakers', 'items')
subplot_different_shops_without_outliers(
    copy_numbr, 'Number of orders', 'items')
subplot_different_shops_without_outliers(
    copy_total_items, 'Number of sold items', 'items')
subplot_different_shops_without_outliers(
    copy_total_amoun, 'Total sold order_amount', 'items')
