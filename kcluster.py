import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Points of interest:
1970 - 1975 Vietnam war
The Troubles, 1968–1998
Falklands War, 1982
Gulf War, 1990–1991
Sierra Leone Civil War, 1991–2002
Bosnian War, 1992–1995
Kosovo War, 1998–1999
War in Afghanistan, 2001–2014
Iraq War, 2003–2011
Libya Conflict, 2011–present
Syria Conflict, 2011–present
Yemen Conflict, 2014–present
Global Coalition to Defeat ISIS, 2014–present 
"""
"""
Computational Plan:
we monitor arms trade and see if there are any markers of upcoming times of turmoil in trade patterns.
identify peaks of arms trade import into countries. c the dates these occur.
"""
# how does arms trade look like from 70s to 91s with relation to the gulf war
inutted_country = input("Country yo, first letter caps thnx")
#get the arms csv:
arms_df = pd.read_csv('ArmsTrade/final.csv')
arms_df.fillna(0, inplace=True)
all_countries = {row[0] for row in arms_df.iterrows()}
#identify all iraq related activities:
imported_iraq = {} #dict, year to number of weapons imported
exported_iraq = {} #dict, year to number of weapons exported
for index, row in arms_df.iterrows():
    if row[1] == inutted_country:
        for year in list(range(1970, 2021)):
            if year in imported_iraq:
                imported_iraq[year] += int(row[year-1970+2])
            else:
                imported_iraq[year] = int(row[year-1970+2])
    if row[0] == inutted_country+",":
        for year in list(range(1970, 2021)):
            if year in exported_iraq:
                exported_iraq[year] += int(row[year - 1970 + 2])
            else:
                exported_iraq[year] = int(row[year - 1970 + 2])

#read ged211.csv as df:
ged211_df = pd.read_csv('ArmsTrade/ged211.csv', dtype = "str")
ged_cols = list(ged211_df.columns)
#get all countries in ged211:
all_countries_ged211 = {row[ged_cols.index("country")] for index, row in ged211_df.iterrows()}
#map type: country to year to number of deaths
deaths_map = {country: {year: 0} for country in all_countries_ged211 for year in range(1970, 1989)}
for index, row in ged211_df.iterrows():
    if row[ged_cols.index("country")] in deaths_map:
        if row[int(ged_cols.index("year"))] in deaths_map[row[ged_cols.index("country")]]:
            deaths_map[row[ged_cols.index("country")]][int(row[ged_cols.index("year")])] += int(row[ged_cols.index("high")])
        else:
            deaths_map[row[ged_cols.index("country")]][int(row[ged_cols.index("year")])] = int(row[ged_cols.index("high")])
    else:
        deaths_map[row[ged_cols.index("country")]] = {}
        deaths_map[row[ged_cols.index("country")]][int(row[ged_cols.index("year")])] = int(row[ged_cols.index("high")])

for year in list(range(1970, 2021)):
    for country in deaths_map:
        if year not in deaths_map[country]:
            deaths_map[country][year] = 0
#normalizing:
for country in deaths_map:
    for year in deaths_map[country]:
        deaths_map[country][year] = deaths_map[country][year]/max(deaths_map[country].values())
for year in imported_iraq:
    imported_iraq[year] = imported_iraq[year]/max(imported_iraq.values())
for year in exported_iraq:
    exported_iraq[year] = exported_iraq[year]/max(exported_iraq.values())
print(imported_iraq)
print(deaths_map["Syria"])
#plot matplot for year to imports, exports, peace_idx?
plt.figure("China")
plt.plot(list(range(1970, 2021)), [imported_iraq[year] for year in list(range(1970, 2021))], label="imported", color="b")
#plt.plot(list(range(1970, 2021)), [exported_iraq[year] for year in list(range(1970, 2021))], label="exported")
plt.plot(list(range(1970, 2021)), [deaths_map[inutted_country][year] for year in list(range(1970, 2021))], label="peace_idx", color="g")
plt.show()