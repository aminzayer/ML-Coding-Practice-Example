from math import *


def euclidean_distance(x, y):
    print("√", end=" "),
    for i in x:
        print("(", x[i-1], "-", y[i-1], ")²+", end=" "),

    print("=", end=" "),

    return sqrt(sum(pow(a-b, 2) for a, b in zip(x, y)))


def manhattan_distance(x, y):
    for i in x:
        print("|", x[i-1], "-", y[i-1], "| +", end=" "),

    print("=", end=" "),
    return sum(abs(a-b) for a, b in zip(x, y))


def minkowski_distance(a, b, p):
    print("max [", end=" "),
    for i in a:
        print("|", a[i-1], "-", b[i-1], "| +", end=" "),

    print("=", end=" "),
    return sum(abs(e1-e2)**p for e1, e2 in zip(a, b))**(1/p)


def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])), 3)


def cosine_similarity(x, y):
    numerator = sum(a*b for a, b in zip(x, y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator), 3)


def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    print("\n|", set(x), " ∩ ", set(y)," = ", intersection_cardinality,
          "| / |", set(x), " ∪ ", set(y)," = " , union_cardinality, "| \n")
    print(intersection_cardinality, " / ", union_cardinality, end=" = "),
    return intersection_cardinality/float(union_cardinality)


#print(euclidean_distance([2, 0, 1, 2], [1, 1, 1, 1]))
#print(manhattan_distance([2, 0, 1, 2], [1, 1, 1, 1]))
#print(minkowski_distance([2, 0, 1, 2], [1, 1, 1, 1], 1))
print(jaccard_similarity([2, 0, 1, 2], [1, 1, 1, 1]))
print(jaccard_similarity(["A", "B", "C"], ["A", "D", "E", "F"]))
