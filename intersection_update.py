#intersection_update  method removes the items that is not present in  given sets and shows the common element
# between these sets.

#with two sets
a={1,3,5,6}
b={1,7,3,0}
a.intersection_update(b)
print(a)
#with three sets
x={1,3,5,6}
y={1,6,3,0}
z={1,6,3,4}
x.intersection_update(y,z)
print(x)


