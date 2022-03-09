import pandas as pd

h = 8


def dosomththingz(a, z, y):
    """Divide z then multiply with rate then result.
    It is a dynamic function so you can always reuse it whenever you want
    :a: integer
    :z: dataFrame
    :y: list
    """
    z["xyz"] = z[y] / 60 / h
    z["abc"] = z["xyz"] * a
    return z["abc"].sum()


# Example
z = pd.DataFrame([1, 1, 1])
y = [2, 2, 2]

rs = dosomththingz(1000, z, y)
print(rs)


import pandas as pds

h = 8


def dosomththingz(param1, param2, param3):
    """Divide z then multiply with rate then result.
    It is a dynamic function so you can always reuse it whenever you want

    :param1: integer
    :param2: pandas DataFrame of length n
    :param3: dictionnary key
    """

    param2["xyz"] = param2[param3] / 60 / h
    param2["abc"] = param2["xyz"] * param1
    return param2["abc"].sum()


# Example
v = pds.DataFrame({"a": [120, 240, 60]})
rs = dosomththingz(1000, v, "a")
print(rs)


print("hi")
