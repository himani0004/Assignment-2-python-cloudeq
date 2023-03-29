#The difference between discard and remove is that remove will through an error if doesn't exist but discard
# will not do. lets see with an example 

#remove function(will through an error if item is not in sets)
# set2 ={"himani","sharma","riya"}
# print(set2)
# set2.remove("riya")
# print(set2)  # when element exist
# set2.remove("vashisht")
# print("set2") # whwn element doesn't exist
  

#Discard function (will not through an error if item is don't exist)
set3={"hello","there","hie"}
print(set3)
set3.discard("hello")
print(set3)#when element exist
set3.discard("you")
print(set3)#when element doen't exist