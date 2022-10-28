from operator import index
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

data = pd.read_csv("data/cleanData.csv", low_memory=False, sep=",")
# data = pd.read_csv("data/complete.csv", low_memory=False, sep=",", error_bad_lines=False)
data = data.astype({'city': 'string'})
print(data.head(5))
print(data.dtypes)
print(data.info())
pd.to_numeric(data['latitude'])


# countries = data["Country"]

countryList = pd.Series(['greenland','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
               'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'uk', 'United States', 'us', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'vietnam', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'])

stateList = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
             'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
             'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
             'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
             'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

pandastates = pd.Series(stateList).str.lower()
pandasCountries = countryList.str.lower()
# print(pandastates.str.lower()) #lowercase states
# countryList.str.lower() #lowercase countries


# print(data[["Country"]])


# print(data[["Country"]])


states = data["state"]
print(states.head())

# print(data.count())

#plt.pie(data["shape"], labels=data["shape"])
# plt.show()

#plt.scatter(data['city'], data['country'])

#plt.title('Scatter plot')

# plt.xlabel('city')
# plt.ylabel('country')

# plt.show()


def split_datetime(data):
    data_split = data["datetime"].str.split(" ", n=1, expand=True)
    # print("we're in split")
    # print(type(data["datetime"]))
    # print(type(data_split)) 
    # print(data_split.info)
    # data_explode = data.explode("datetime")
    data[["date", "time"]] = data_split
    data.drop("datetime", axis=1, inplace=True)
    print(data.head(5))
    # print(data.info)
    return data


def missing_zero_values_table(df):
        zero_val = (df == 0).astype(int).sum(axis=0)
        # print(zero_val)
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mz_table = pd.concat([zero_val, mis_val, mis_val_percent], axis=1)
        mz_table = mz_table.rename(
        columns = {0 : 'Zero Values', 1 : 'Missing Values', 2 : '% of Total Values'})
        mz_table['Total Zero Missing Values'] = mz_table['Zero Values'] + mz_table['Missing Values']
        mz_table['% Total Zero Missing Values'] = 100 * mz_table['Total Zero Missing Values'] / len(df)
        mz_table['Data Type'] = df.dtypes
        # print("__________________")
        # print(mz_table)
        # print("____________________-")
        # mz_table = mz_table[
            # mz_table.iloc[:,1] != 0].sort_values(
        # mz_table = mz_table[mz_table.iloc[:,0] != 0].sort_values(
        # '% of Total Zero Missing Values', ascending=False).round(1)

        print ("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"      
            "There are " + str(mz_table.shape[0]) +
              " columns that have missing values.")
        # mz_table.to_excel('D:/sampledata/missing_and_zero_values.xlsx', freeze_panes=(1,0), index = False)
        return mz_table

def missing(dff):
    print (round((dff.isnull().sum() * 100/ len(dff)),2).sort_values(ascending=False))


def update_country_state(data):
    data['country'] = data['country'].fillna('fuck')
    data['city'] = data['city'].fillna('fuck')
    print("try to change:")
    # print(data.head(5))
    for x in data.index: 
        if data.loc[x, "country"] == "fuck":
        # print("hej" + str(x))
        # print(data.loc[x, "state"])
            state = data.loc[x,"state"]
            for stat in pandastates:
                if state == stat:
                    # print("found state")
                    # print(state)
                    data.loc[x,"country"] = "usa"
                    break
            for country in pandasCountries:
                # print(x)
                if (data.loc[x,"city"].find(country)) > 0:
                    data.loc[x,"country"] = country
                    break

def update_ca_and_uk(data):
    for x in data.index:
        name = data.loc[x,"country"]
        if name == "ca":
            data.loc[x, "country"] = "canada"
        elif name == "uk":
            data.loc[x, "country"] = "gb"
        elif (name == "us") | (name == "united states"):
            data.loc[x, "country"] = "usa"
        elif name == "au":
            data.loc[x,"country"] = "australia"

# to remove rows with no longitude or latitude or city
def dropLatLong(data):
    todrop = data[((data['longitude']== 0) & (data['latitude'] ==0) & (data['city'] == "fuck"))].index
    print(todrop)
    print(data.loc[todrop])
    # data.drop(todrop, inplace=True)

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

# to find indexes of rows with too much missing data
def countBadRows(data, lower):
    index = []
    for x in data.index:
        count_nan = data.loc[[x]].isna().sum().sum()
        if count_nan > lower:
            index.append(x)
    return index

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
    goodRows = data[(data['country'] == "usa")]
    return goodRows

def writeToNewFile(data):
    print(data.head)
    data.to_csv("data/usa.csv", sep=",",index=False)

if __name__ == "__main__":
    #    display(data.head(10))
    # print("iii")
    # update_ca_and_uk(data)
    # dropLatLong(data)
    # findMissingCitiesFromLatLong(data)
    # print(missing_zero_values_table(data))
    # print(countBadRows(data, 2))
    # data = split_datetime(data)
    # print(data)
    # data.drop("stupid", axis=1, inplace=True)
    # print(data.head)
    newData = onlyUsa(data)
    writeToNewFile(newData)
    # print("new file should exist")

    # missing(data)
    # print("")
    # print(missing_zero_values_table(data)) #now countries where fixed but we still have lot of empty states
    # missing(data)
    # column = data['longitude'] 
    # count = column[column == 0].count()
    # print('Count of zeros in longitude : ', count )
