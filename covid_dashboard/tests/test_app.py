"""
Tests for app module
"""

from app import *

def test_unschedule_covid_updates():
    """
    Checks scheduled updates can be removed from queue
    """

    display_update.append("test")
    unschedule_update("test", False)

    assert len(display_update) == 0

def test_time_difference():
    """
    Checks time difference finds the correct time difference
    between now and the input time
    """

    difference = time_difference("12:00")

    #Checks time output is a float 
    assert isinstance(difference, float)
    #Checks time until update is greater than 0 
    assert difference > 0 

def test_unschedule_update():
    """
    Checks unschedule_update removes update from queue
    """

    global display_update
    #Adds update to queue
    display_update.append('test')
    #Removes update
    unschedule_update('test', False)
    #Checks update has been removed
    assert len(display_update) == 0

def test_toast_builder():
    """
    Checks toast_builder constructs toasts correctly
    """
    global display_update

    name = 'update'
    chosen_time = '12:00'
    #Sets up the toast
    toast_builder(name,chosen_time,True,True,True)
    #Checks dictionary has been constructed correctly
    assert display_update[0]['title'] == name
    assert display_update[0]['update_time'] == chosen_time
    assert display_update[0]['repeat'] == True
    #Removes update for next test
    display_update.pop(0)

def test_update_covid_data():
    """
    Checks that alarm is unschedulued after
    covid data update
    """

    global current_data
    global display_update
    display_update.append(' ')

    update_covid_data(' ')

    assert len(display_update) == 0

def test_update_current_articles():
    """
    Checks that alarm is unschedulued after
    news article update
    """

    global current_articles
    global display_update
    display_update.append(' ')

    update_current_articles(' ')

    assert len(display_update) == 0