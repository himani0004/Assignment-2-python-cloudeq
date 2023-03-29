#symmetric differnce update that shows the element that are  not common in given sets.
#using two sets
x={1,2,3,4}
y={1,5,6,7}
x.symmetric_difference_update(y)
print(x) 

#using three sets it will give error as it takes only one argument
x={1,2,3,4}
y={1,5,6,7}
z={8,9}
x.symmetric_difference_update(y,z)
print(x)  