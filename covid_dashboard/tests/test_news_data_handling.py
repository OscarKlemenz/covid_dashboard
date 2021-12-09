"""
Tests for the module news_data_handling
"""

from covid_news_handling import articles_to_return, news_API_request
from covid_news_handling import update_news

def test_news_API_request():
    assert news_API_request()
    assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()

def test_update_news():
    update_news('test')

def test_articles_to_return():
    """
    Checks only six or less articles are returned by function 
    """
    articles = update_news()
    output_articles = articles_to_return(articles)

    assert len(output_articles) <= 6

def test_article_removal():
    """
    Checks articles can be removed
    """
    articles_removed = []
    articles = update_news()
    
    #Puts first article in list in removed articles
    articles_removed.append(articles[0]['title'])

    articles_to_output = articles_to_return(articles, articles_removed)
    #Checks removed article hasnt been added 
    assert articles[0] != articles_to_output[0]

def test_non_removed_articles():
    """
    Checks that non-removed articles will be placed in articles to
    output
    """

    articles = update_news()
    articles_to_output = articles_to_return(articles)

    assert articles[0] == articles_to_output[0]

def test_news_formatting():
    """
    Checks that content of articles only change the description
    and not the title
    """
    
    pre_formatted = news_API_request()
    formatted = update_news()

    assert pre_formatted[0]['title'] == formatted[0]['title']
    assert pre_formatted[0]['description'] != formatted[0]['content']
