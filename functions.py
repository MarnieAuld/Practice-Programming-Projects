"""
Functions Programming Practice
"""


"""
Write a function that calculates which of two products is cheaper based on a quantity and price. 
The function will take 4 parameters - the quantity and price of each product, and output either "First" or "Second".
"""


def find_cheaper_product(first_product_quantity, first_product_price, second_product_quantity, second_product_price):
    first_product_cost = first_product_quantity * first_product_price
    second_product_cost = second_product_quantity * second_product_price
    if first_product_cost > second_product_cost:
        return "First"
    else:
        return "Second"


print(find_cheaper_product(2, 10, 4, 3))
