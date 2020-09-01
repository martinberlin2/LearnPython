# 11:10 01.09 kata zwischendurch = restaurant.py
#
# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

import logging
from martinsHelper import NaTALi
from restaurant import restaurant

evalTC = NaTALi.evalTC
execFuncWithExc = NaTALi.execFuncWithExc
execMethWithExc = NaTALi.execMethWithExc


# änderung


def test_restaurant():
    logging.info(" ----- Start test_restaurant -----")
    evalTC(
        1,
        "KataOrder",
        execFuncWithExc(
            restaurant,
            ["milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"],
        ),
        "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke",
    )
    logging.info(" ----- End test_restaurant -----")
    print("\u2728")


test_restaurant()

