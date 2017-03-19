import requests
import json
from os.path import join
from cali_condemned_inmates import get_inmates_by_date
from xlrd import open_workbook

BASE_URL = 'http://api.wunderground.com/api/322de266ae1a62c5/history_'

def county_to_zipcode():
    book_counties = open_workbook('zip_codes.xlsx')
    sheet_counties = book_counties.sheet_by_index(0)

    zip_codes = {}

    for row in range(1, sheet_counties.nrows):
        zip_codes[sheet_counties.cell(row, 0).value] = sheet_counties.cell(row, 1).value

    return zip_codes
    # counties = []
    # for i in get_inmates():
    #     if i['Trial County'] in counties:
    #         pass
    #     else:
    #         counties.append(i['Trial County'])


def generate_url(county, date):
    url = ""

    url_date = date[6:] + date[0:2] + date[3:5]

    zip_code = county_to_zipcode()[county]

    query = '/q/'

    json_ext = '.json'

    url = str(BASE_URL) + str(url_date) + str(query) + str(zip_code) + str(json_ext)

    return url

def fetch_data(url, name):
    fname = str(name) + '_weather.json'
    resp = requests.get(url)
    with open(fname, 'wb') as f:
        f.write(resp.content)

def parse_data(url, name):
    fname = str(name) + '_weather.json'
    fetch_data(url, name)
    f = open(fname, 'r')
    raw_data = f.read()
    f.close()
    return json.loads(raw_data)

def get_weather_condition(url, name):
    parsed_data = parse_data(url, name)
    low_temp = parsed_data['history']['dailysummary'][0]['mintempi']
    high_temp = parsed_data['history']['dailysummary'][0]['maxtempi']
    conditions = [low_temp, high_temp]

    return conditions

def get_weather(birthday):
    inmate_profiles = get_inmates_by_date(birthday)

    weather = {}

    for i in inmate_profiles:
        if i['LastName'] in weather.keys():
            pass
        else:
            url = generate_url(i['Trial County'], i['Offense Date'])
            weath_condition = get_weather_condition(url, i['LastName'])
            weather[i['LastName']] = weath_condition

    return weather

def weather_message(birthday):
    weather_conditions = get_weather(birthday)
    inmate_profiles = get_inmates_by_date(birthday)

    message = ""

    for w in weather_conditions.keys():
        if weather_conditions[w][0] is "" or weather_conditions[w][1] is "":
            new_message = "There is no weather data for the time and location where " + str(w) + " committed their crime."
        else:
            sample_message = """There was a high of {high_temp} degrees fahrenheit, and a low of {low_temp} in {trial_county}, where {inmate_last_name} committed their crime on {offense_date}."""

            for i in inmate_profiles:
                if i['LastName'] is w:
                    t = i['Trial County']
                    od = i['Offense Date']

            new_message = sample_message.format(
                high_temp = weather_conditions[w][1],
                low_temp = weather_conditions[w][0],
                trial_county = t,
                inmate_last_name = w,
                offense_date = od)

        message += new_message

    return message














