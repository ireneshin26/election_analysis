#3.2.11 Skill Drill 2 (List of Dictionaries)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#naming variable for the dictionary inside the list
for county_dict in voting_data:
    print(county_dict)

#stating the number of times it needs to iterate - in this case, as many items as there are in the list.
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

#classify the values variable
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#then do f-string to pull both keys and values in and combine.
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,.0f} registered voters.")