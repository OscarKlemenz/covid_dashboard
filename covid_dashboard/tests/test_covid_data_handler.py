"""
Tests for the module covid_data_handler and scheduler
"""
import json
from covid_data_handler import last7day_infections, national_data_API_extract, parse_csv_data
from covid_data_handler import total_death_finder
from covid_data_handler import process_covid_csv_data
from covid_data_handler import covid_API_request
from app import schedule_covid_updates, display_update

def test_parse_csv_data():
    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639

def test_process_covid_csv_data():
    last7days_cases , current_hospital_cases , total_deaths = \
        process_covid_csv_data ( parse_csv_data (
            'nation_2021-10-28.csv' ) )
    assert last7days_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_544

def test_covid_API_request():
    data = covid_API_request()
    assert isinstance(data, dict)


def test_schedule_covid_updates():
    """
    Test for update scheduler
    """
    display_update.append({})

    schedule_covid_updates(update_interval=10, update_name='update test')


def test_data_types_covid_API_request():
    """
    Checks data is producing the correct data types
    """

    data = covid_API_request()['data']
    assert isinstance(data[0]['newCasesByPublishDate'], int)

def test_national_data_API_extract():
    """
    Checks national data is extracting the correct data 
    """
    stats = national_data_API_extract()
    data = covid_API_request("England", "nation")['data']

    for day in data:

        if day['hospitalCases']:
            hospital_cases = int(day['hospitalCases'])
            break
    
    #Checks deaths
    assert stats[1] == hospital_cases

def test_national_7days_infection():
    """
    Checks 7 days infection is getting the correct data 
    """
    data = covid_API_request("England", "nation")['data']
    test_7days = last7day_infections(data)

    stats = national_data_API_extract()

    assert stats[0] == test_7days

def test_total_deaths():
    """
    Checks total death finder is working properly 
    """
 
    data = covid_API_request("England", "nation")['data']
    func_deaths = total_death_finder(data)

    for day in data:
        if day["cumDailyNsoDeathsByDeathDate"]:

            test_total_deaths = day["cumDailyNsoDeathsByDeathDate"]
            break
    
    assert func_deaths == test_total_deaths
