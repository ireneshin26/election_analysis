#3.2.11 Skill Drill 1 (Dictionary)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(f"{county} has {voters:,.0f} registered voters.")




