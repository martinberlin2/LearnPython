# 11:10 01.09 kata zwischendurch = restaurant.py
# https://www.codewars.com/kata/5d23d89906f92a00267bb83d?utm_source=newsletter&utm_medium=email&utm_campaign=weekly_coding_challenges_sponsored_by_scout_apm&utm_term=2020-08-25

# 6 kyu
# New Cashier Does Not Know About Space or Shift
# Some new cashiers started to work at your restaurant.
# They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
# All the orders they create look something like this:
# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
# The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
# Their preference is to get the orders as a nice clean string with spaces and capitals like so:
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
# The kitchen staff expect the items to be in the same order as they appear in the menu.
# The menu items are fairly simple, there is no overlap in the names of the items:

# 1. Burger
# 2. Fries
# 3. Chicken
# 4. Pizza
# 5. Sandwich
# 6. Onionrings
# 7. Milkshake
# 8. Coke


def restaurant(order):  # order = String, --> order als Liste
    # result = str('ert').title();
    s = "myorder"
    result = s.title()
    print(result)
    # result = title(order)
    return result
