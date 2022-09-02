x = 0
while x<=5: #this is the test condition to make sure that above variable is less than 5. if true do the following code:
    print(x)
    x = x + 1 #increment x by 1 and condition is tested until x is 5.



for num in range(5):
    print(num)

#Iterate through a List 3.2.10
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])



#Iterate through a Dictionary 3.2.10
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson":432438}

#Get the keys of the dictionary
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)