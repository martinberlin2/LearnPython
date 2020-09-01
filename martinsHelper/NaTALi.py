# NaTALi.py - Native Testing Automatization Library
# Test Automatization by Python for Python. No external software

# Import :
# import NaTALi
# evalTC = NaTALi.evalTC
# execFuncWithExc = NaTALi.execFuncWithExc
# execMethWithExc = NaTALi.execMethWithExc
# exec_TCAlt = NaTALi.exec_TCAlt

# Usage:
# -- one testcase = one line:
# def evalTC(nr, desc, result, expected): #-> void but logging.info.
# logs TestCase number, the description, PASSED, or FAILED with the result.
# -- get result:
# these both execute function resp. method with args, catch exceptions and return them as string, otherwise the normal result:
# def execFuncWithExc(functionName, args): # -> result, Exception given as String from Exception. functionName not in ""
# def execMethWithExc(object, method, args): #-> result, Exception given as String from Exception. method not in ""
#
# Example:
# evalTC(6, "setValue2d out_of_range > len", execMethWithExc(list, List2D.setValue2d, [list,3,1,"a_value_ExcTest"]), "Out_of_range_Exc")
# Testcase number 6 executes list.setValue2d(3,1,"a_value_ExcTest") which tries to set the string "a_value_ExcTest" in list[3][1] (or whatever the internal implemetation of that "list" object is). This list represents a TicTacToe board, so is max [2][2], and setValue2d is expected to give the string "Out_of_range_Exc" instead of the real exception.
#
# -- older stuff for older TCs (without expected exceptions):
# def exec_TCAlt(functionName, nr, exp, args)
# def exec_TC(result, nr, exp, args)
#
# TODO ? differ expected and unexpected exception - but the ladder will give another string anyway

import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

from martinsHelper import divers

# logging.basicConfig(filename='./NaTALi.log',
# level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
# logging.info('Example of logging with ISO-8601 timestamp')

logging.info("---- NaTALi Native Testing Automatization Library ready ----")


def evalTC(
    nr, desc, result, expected
):  # nr = TC-Nr, desc = short TC description, result = TC executed with execFuncWithExc or execMethWithExc (some legacy with exec_TC -> void, aber logging.info.
    addLeadingZeros = divers.addLeadingZeros
    eval = "PASSED"
    rs = "start"
    try:
        rs = str(result)
    except Exception as ex:  # kommt da ein String raus? ja
        logging.info(
            "---Unexpected exception! "
        )  # should execMethWithExc or execFuncWithExc have done
        rs = str(ex)
    otherResultString = ""
    if rs != str(expected):
        eval = "FAILED"
        otherResultString = "---Result:" + rs + "!"  # + expected + "!"
    outstr = (
        str(addLeadingZeros(nr, 2))
        + " "
        + eval
        + " ....TC: "
        + desc
        + otherResultString
    )
    logging.info(outstr)


def execFuncWithExc(
    functionName, args
):  # -> result, Exception given as String from Exception. functionName not in ""
    try:
        result = functionName(*args)
    except Exception as ex:
        result = str(ex)
    return result


def execMethWithExc(
    object, method, args
):  # -> result, Exception given as String from Exception. method not in ""
    result = "start"
    try:
        result = getattr(object, method(*args))
        # result = object.method(*args) -- geht nicht
    except Exception as ex:
        result = ex
    # logging.info (result)
    return result


def CompFiles(
    result, expected
):  # --> (Zeilennr, Spaltennr) or "ExpectedFileNotFound" (prio), "ResultFileNotFound", "FilesAreEqual"
    rsfile = "./" + result
    exfile = "./" + expected
    import os.path

    if os.path.isfile(exfile) == False:
        return "ExpectedFileNotFound"
    if os.path.isfile(rsfile) == False:
        return "ResultFileNotFound"

    line = -1
    col = 0

    with open(exfile, "r") as efile, open(rsfile, "r") as rfile:
        rtext = rfile.readline()
        etext = efile.readline()
        # logging.info(rtext)
        # logging.info(etext)
        while rtext + etext != "":
            line = line + 1
            if rtext != etext:
                col = compare_strings(rtext, etext)  # kein Check auf "StringsAreEqual"
                # logging.info("Abweichung Zeile, Spalte: ", line, col)
                # logging.info("rtext=", rtext,"#")
                # logging.info("etext=", etext,"#")
                # logging.info(line, col)
                return (line, col)
            # with open(result, "r") as rfile:
            rtext = rfile.readline()
            etext = efile.readline()
            # logging.info("rtext=", rtext)
            # logging.info("etext=", etext)
        # close()
        # logging.info("FilesAreEqual")
    return "FilesAreEqual"


def compare_strings(
    a, b
):  # -> Pos of first different char, from 0, or "StringsAreEqual"
    pos = 0
    while True:
        if pos == len(a):
            if pos == len(b):
                return "StringsAreEqual"
            return pos
        if pos == len(b):
            return pos
        # logging.info("-- pos:" + str(pos) + "!" + a[pos] + "!" + b[pos] + "!")
        if a[pos] != b[pos]:
            return pos
        pos = pos + 1
        # if pos > 100:
        # return "Loop Error"


def exec_tc_alt(
    function_name, nr, exp, args
):  # functionName nicht in "" !  # still used in test_List.py  # no exception handling
    from martinsHelper import divers

    addLeadingZeros = divers.addLeadingZeros
    result = function_name(*args)
    if result == exp:
        logging.info("TC " + addLeadingZeros(nr, 2) + " PASSED")
        return "passed"
    logging.info(
        "TC " + addLeadingZeros(nr, 2) + " FAILED, Result:" + str(result) + "!"
    )
    return "failed"
