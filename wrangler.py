import json

# targeting select EV data
evData = json.load(open("data/ev_data.json"))

''' raw cols : 
    (8) VIN (1-10),County,City,State,Postal Code,
    (13) Model Year,Make,Model,Electric Vehicle Type,
    (17) Clean Alternative Fuel Vehicle (CAFV) Eligibility,
    (18) Electric Range,Base MSRP,Legislative District,
    (21) DOL Vehicle ID,Vehicle Location,Electric Utility,
    (24) 2020 Census Tract
'''

''' ex row:
    ['row-u6sz~kgcx~zrq2', '00000000-0000-0000-836B-A53E3F531CE3', 0, 1707937999, None, 1707938084, None, '{ }', 
    '5UXKT0C59G', 'Yakima', 'Zillah', 'WA', '98953', 
    '2016', 'BMW', 'X5', 
    'Plug-in Hybrid Electric Vehicle (PHEV)', 
    'Not eligible due to low battery range', 
    '14', '0', '15', '206822717', 
    'POINT (-120.26317 46.40556)', 
    'PACIFICORP', '53077002201', '2746', '4', 
    '22']
'''

print(evData["data"][0])

valid_counties = [
    "San Juan", "Island", "Clallam", "Jefferson", "Kitsap",
    "Grays Harbor", "Mason", "Thurston", "Pacific", "Lewis",
    "Wahkiakum", "Cowlitz", "Clark", "Skamania", "Klickitat",
    "Yakima", "Pierce", "King", "Snohomish", "Skagit",
    "Whatcom", "Okanogan", "Chelan", "Douglas", "Kittitas",
    "Grant", "Benton", "Franklin", "Walla Walla", "Columbia",
    "Garfield", "Asotin", "Whitman", "Adams", "Lincoln",
    "Spokane", "Ferry", "Stevens", "Pend Oreille"
]

county_data = {}

print(len(valid_counties))
for county in valid_counties:
    county_data[county] = { 
        "total" : 0,
        "brand" : {},
        "ranges" : [],
        "years" : {},
        "clean_eligibility" : {} 
    }

for row in evData["data"]:
    county = row[9]
    print(row[13], row[14], row[16], row[18], row[17])
    if county in valid_counties:
        county_data[county]["total"] += 1

cd_sorted = dict(sorted(county_data.items(), key=lambda item : item[1]["total"], reverse=True))

print(cd_sorted)




