from operator import index
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

data = pd.read_csv("data/smallDataset.csv", low_memory=False, sep=",")
data = data.astype({'city': 'string'})
# data = pd.read_csv("data/complete.csv", low_memory=False, sep=",", error_bad_lines=False)
pd.to_numeric(data['latitude'])



### Country Names
countryList = pd.Series(['Greenland','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
               'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'uk', 'United States', 'us', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'vietnam', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])

### State 
stateList = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
             'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
             'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
             'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
             'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

### Make Country and Statelist to lower case
pandastates = pd.Series(stateList).str.lower()
pandasCountries = countryList.str.lower()

states = data["state"]
print(states.head())

### Split date into two columns: date and time
def split_datetime(data):
    data_split = data["datetime"].str.split(" ", n=1, expand=True)
    data[["date", "time"]] = data_split
    data.drop("datetime", axis=1, inplace=True)
    return data

### Prints how many rows are missing information per coloum
def missing(dff):
    print (round((dff.isnull().sum() * 100/ len(dff)),2).sort_values(ascending=False))


### finds all rows where missing city or country, if state is there then update country with US
def update_country_state(data):
    data['country'] = data['country'].fillna('fuck')
    data['city'] = data['city'].fillna('fuck')
    print("try to change:")
    for x in data.index: 
        if data.loc[x, "country"] == "fuck":
            state = data.loc[x,"state"]
            for stat in pandastates:
                if state == stat:
                    data.loc[x,"country"] = "United States"
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

# Removes rows with no longitude or latitude or city
def dropLatLong(data):
    todrop = data[((data['longitude']== 0) & (data['latitude'] ==0) & (data['city'] == "fuck"))].index
    print(todrop)
    print(data.loc[todrop])


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
    print('no')

### TODO: Make Europe Data set

if __name__ == "__main__":
    #    display(data.head(10))
    # print("iii")
    # update_country_state(data)
    # update_ca_and_uk(data)
    # dropLatLong(data)
    # findMissingCitiesFromLatLong(data)
    # print(missing_zero_values_table(data))
    # print(countBadRows(data, 2))
    # data = split_datetime(data)
    # print(data)
    # data = data.drop(columns=['stupid1', 'stupid2'])
    # print(data.head)
    # newData = onlyUsa(data)
    #data = dropComments(data)

    # print("new file should exist")
    #dropRows(data)

    # missing(data)

    binLongAndLat(data)
    writeToNewFile(data)


    # insertIdColumn(data)
    # print("")
    # print(missing_zero_values_table(data)) #now countries where fixed but we still have lot of empty states
    # missing(data)
    # column = data['longitude'] 
    # count = column[column == 0].count()
    #print('Count of zeros in longitude : ', count )
