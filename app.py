from operator import index
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
import datetime as dt

geolocator = Nominatim(user_agent="geoapiExercises")

data = pd.read_csv("data/scrubbed.csv", low_memory=False, sep=",")
data = data.astype({'city': 'string'})
# data = pd.read_csv("data/complete.csv", low_memory=False, sep=",", error_bad_lines=False)
pd.to_numeric(data['latitude'])



### Country Names
countryList = pd.Series(['Greenland','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
               'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda','uk/england', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'uk', 'United States', 'us', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'vietnam', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])

### State 
stateList = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
             'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
             'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
             'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
             'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

canada_states = ["ON", "QC", "NS", "NB", "MB", "BC", "PE","SK", "AB", "NL"]

european_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
                      'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
                       'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
                       'Poland', 'Portugal', 'Romania','Scotland', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']

american_countries = [    "Antigua and Barbuda",    "Bahamas",    "Barbados",    "Belize",    "Canada",    "Costa Rica",    "Cuba",    "Dominica", "Dominican Republic",
    "El Salvador",     "Grenada",    "Guatemala",    "Haiti",    "Honduras",    "Jamaica",  "Mexico", "Nicaragua",
    "Panama",    "Saint Kitts and Nevis","Saint Lucia"  ,"Saint Vincent and the Grenadines","Trinidad and Tobago", "United States"]

### Make Country and Statelist to lower case
pandastates = pd.Series(stateList).str.lower()
pandasCountries = countryList.str.lower()
canada_states = pd.Series(canada_states).str.lower()
# european_countries= pd.Series(european_countries).str.lower()
# american_countries = pd.Series(american_countries).str.lower()


# states = data["state"]
# print(states.head())

### Split date into two columns: date and time
def split_datetime(data):
    data_split = data["datetime"].str.split(" ", n=1, expand=True)
    data[["date", "time"]] = data_split
    data.drop("datetime", axis=1, inplace=True)
    data.drop("date posted", axis=1, inplace=True)
    return data

def put_back_datetime():
    df = pd.read_csv("data/coordEu.csv", low_memory=False, sep=",")
    df['datetime'] = df[['date', 'time']].apply(lambda x: ' '.join(x), axis=1)
    df.to_csv("data/coordEu.csv", sep=",", index=False)


### Prints how many rows are missing information per coloum
def missing(dff):
    print (round((dff.isnull().sum() * 100/ len(dff)),2).sort_values(ascending=False))


### finds all rows where missing city or country, if state is there then update country with US
def update_country_state(data):
    data['country'] = data['country'].fillna('fuck')
    data['city'] = data['city'].fillna('')
    print("try to change:")
    for x in data.index: 
        if (data.loc[x, "country"] == "fuck") | (data.loc[x, "country"]== "Fuck"):
            state = data.loc[x,"state"]
            for stat in pandastates:
                if state == stat:
                    data.loc[x,"country"] = "United States"
                    break
            for stat in canada_states:
                if state == stat:
                    data.loc[x,"country"] = "Canada"
                    break
            for country in pandasCountries:
                if (data.loc[x,"city"].find(country)) > 0:
                    data.loc[x,"country"] = country.capitalize()
                    break
        data.loc[x,"country"] = data.loc[x,"country"].capitalize()

### Opdater lande så de får fuldt navn
def update_ca_and_uk(data):
    for x in data.index:
        name = data.loc[x,"country"].lower()
        if (name == "ca") | (name == "canada"):
            data.loc[x, "country"] = "Canada"
        elif (name == "uk") | (name == "gb"):
            data.loc[x, "country"] = "United Kingdom"
        elif (name == "us") | (name == "united states") | (name == "usa"):
            data.loc[x, "country"] = "United States"
        elif (name == "au") | (name == "australia"):
            data.loc[x,"country"] = "Australia"
        elif (name == "De") | (name == "de"):
            data.loc[x,"country"] = "Germany"

# https://www.geeksforgeeks.org/get-the-city-state-and-country-names-from-latitude-and-longitude-using-python/
def findMissingCitiesFromLatLong(data):
    indexs = data[((data['city'] == "fuck") & (data['longitude']!=0) & (data['latitude']!=0))].index
    print("fjen")
    print(indexs)
    
    for x in indexs:
        print(x)
        lon = data.loc[x, "longitude"]
        lat = data.loc[x, "latitude"]
        print(lon)
        print("type of lon: " + str(type(lon)))
        print(lat)
        print("type of lat: " + str(type(lat)))

        location = geolocator.reverse(str(lat)+","+str(lon))
        address = location.raw['address']
        city = address.get('city', '')
        data.loc[x,'city'] = city

# European lat long ish 
# 35.098861668792544, -27.302793202744642 lower left
# 35.9746770601455, 34.58455316767233     lower right
# 72.55041125948188, -27.836428606303063  upper left
# 73.59254794915556, 35.890174093751114   upper right
def lonlatEu(data):
    goodrows = data[(data["longitude"] < 36.0) & (data["longitude"] > -27 )]
    goodrows = goodrows[goodrows["latitude"] > 35]
    goodrows.to_csv("data/coordEu.csv", index=False)


#American
# 9.675998972033664, -34.85351656453326 lower right 
# 9.81713780335435, -174.33601411632287 lower left
# 70.88956610311078, -167.74854515121604 upper left
# 73.22453676932042, -23.397049596935993 upper right
def bylonlatUs(data):
    goodrows = data[(data["longitude"] < -30.0) & (data["longitude"] > -180.0 )]
    goodrows = goodrows[goodrows["latitude"] > 10]
    goodrows.to_csv("data/coordUs.csv", index=False)


# Removes rows with no longitude or latitude or city
def dropLatLong(data):
    data = data[((~(data['longitude']== 0.0)) & (~(data["latitude"] ==0.0)))]
    # print(todrop)
    # print(data.loc[todrop])
    return data


# to find indexes of rows with too much missing data
def countBadRows(data, lower):
    index = []
    for x in data.index:
        count_nan = data.loc[[x]].isna().sum().sum()
        if count_nan > lower:
            index.append(x)
    return index


#to streamline shape data
def cleanShapes(data):
    #TODO what do we want the shapes to be
    #TODO burde vi spørge Hans-Jürg hvor meget vi må ændre
    for x in data.index:
        shape = data.loc[x, "shape"]
        if (shape == "hexagon") | (shape == "dome") | (shape == "changed") | (shape == "crescent") :
            data.loc[x, "shape"] = "other" 
        elif (shape == "other"):#er other en shape?
            data.loc[x, "shape"] = "unknown" 
        elif (shape == "pyramid"):
            data.loc[x,"shape"] = "triangle" #for that one pyramid shape
        elif (shape == "round") | (shape == "sphere"): 
            data.loc[x,"shape"] = "circle"
        elif (shape == "cylinder"):
            data.loc[x,"shape"] = "cigar"
        data.loc[x,"shape"].capitalize() #because it looks nice


### ---------- TEST OG PRINT FUNCTIONS

### Drop Comment coloumn form data filde
def dropComments(data):
    data = data.drop(columns=['comments'])
    return data

### Drop rows, use when you want a test data set
def dropRows(data):
    data = data[(data.index < 10000)]
    data.to_csv("data/smallDataset.csv", sep=",",index=False)

### Print function
def more_info(data):
    cities = data['city'].unique()
    countries = data['country'].unique()
    states = data['state'].unique()
    print(cities)
    print()
    print(countries)
    print()
    print(states)

def onlyUsa(data):
    goodRows = data[(data['country'] == "United States")]
    return goodRows

#TODO det her kan gøres ved at sætte index=true i writeToNewFile
def insertIdColumn(data): 
    data[ID] = list(range(length(data)))
    return data

def binLongAndLat(data):
    data['lat_bin'] = pd.qcut(data['latitude'], q=20)
    data['long_bin'] = pd.qcut(data['longitude'], q=20)

### Define name of new file
def writeToNewFile(data):
    print(data.head)
    data.to_csv("data/binnedSmallDataset.csv", sep=",",index=False)
    
### Clean Data 
def cleanData(data):
    dropLatLong(data)
    findMissingCitiesFromLatLong(data)
    update_country_state(data)
    update_ca_and_uk(data)
    #split_datetime(data)
    
## Remove everything other than Europe and North-America Country
    
### TODO: Make North-America Data set
def makeNorthAmericaDataSet(data):
    goodRows = data[data["country"].isin(american_countries)]
    goodRows.to_csv("data/american.csv", sep=",",index=False)
    print('no')

### TODO: Make Europe Data set
def makeEuropeanDataSet(data):
    goodRows = data[data["country"].isin(european_countries)]
    goodRows.to_csv("data/european.csv", sep=",",index=False)
    
def badData(data):
    badRows = data[~data["country"].isin(european_countries) & ~data["country"].isin(american_countries)]
    badRows.to_csv("data/badData.csv", sep=",", index=False)

def removeUnder1990():
    data = pd.read_csv("data/coordEu.csv", low_memory=False, sep=",")
    data['date'] = pd.to_datetime(data['date'])
    print(data.dtypes)
    goodRows = data[((data['date'].dt.year >= 1990 ))]
    goodRows = goodRows[~(goodRows['shape'].isnull())]
    goodRows.drop("duration (seconds)", axis=1, inplace=True)
    goodRows.drop("duration (hours/min)", axis=1, inplace=True)
    missing(goodRows)
    goodRows.to_csv("data/coordEu.csv", sep=",", index=False)


if __name__ == "__main__":
    #    display(data.head(10))
    # print("iii")
    # dropLatLong(data)
    # findMissingCitiesFromLatLong(data)
    # print(missing_zero_values_table(data))
    # print(countBadRows(data, 2))
    # data = split_datetime(data)
    # print(data)
    # data = data.drop(columns=['stupid1', 'stupid2'])
    print(data.info)
    print(data.dtypes)
    # newData = onlyUsa(data)
    #data = dropComments(data)

    # print("new file should exist")
    #dropRows(data)
    # makeEuropeanDataSet(data)
    # makeNorthAmericaDataSet(data)
    # badData(data)
    # missing(data)
    # data = dropLatLong(data)
    # data = split_datetime(data)
    # update_country_state(data)
    # update_ca_and_uk(data)
    # lonlatEu(data)
    # bylonlatUs(data)
    # badData(data)
    # missing(data)
    # removeUnder1990()
    put_back_datetime()


    # binLongAndLat(data)
    # writeToNewFile(data)


    # insertIdColumn(data)
    # print("")
    # print(missing_zero_values_table(data)) #now countries where fixed but we still have lot of empty states
    # missing(data)
    # column = data['longitude'] 
    # count = column[column == 0].count()
    #print('Count of zeros in longitude : ', count )



#["circle",  "sphere",   "triangle", "teardrop", "cigar",    "cylinder", "cone",    "diamonds","rectangle",   "light",  "flash",    "fireball", "cross",    "chevron",  "formation",  "unknown",  "changing", "other",    "disk",     "oval",    "egg" ],
#["#2A44E8", "#216EFF",  "#3028A6",  "#1E1866",  "#B37295",  "#D98BB4",  "#3B31CC", "#9D57C9", "#E8A495",    "#E06B0B", "#7A3A06", "#BA5909",  "#D1718C",  "#AB5C73",  "#04C441",    "#3FC404",  "#04BA71",  "#7CBA04",  "#68A3FF",  "#5CE1FF", "#38E6EB"]