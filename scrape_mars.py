from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver 
     #path for MAC 
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    # path for windows - need to complete path!!!
    #executable_path = {"executable_path": "C:/Users/Heather Bree/chromedriver_win32/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # create mars data dict that we can insert into mongo
    mars_data = {}

    # visit Mars Nasa News site
    mars_url = 'http://mars.nasa.gov/news/'
    browser.visit(mars_url) 

    # gives it one second...can change to what you need for site to load
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # get the latest news title from the NASA Mars News Site and assign a variable
    news_title = soup.body.find_all('div', class_="content_title")[1].text
    
    # get the latest Paragraph text from the NASA Mars News Site and assign a variable
    news_p = soup.find('div', class_="article_teaser_body").text

    # add data to our mars data dict
    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p

    # visit the URL from the Jet Propulsion Laboratory to scrape
    jet_url = 'http://jpl.nasa.gov/spaceimages/?search=&category=Mars/'
    browser.visit(jet_url)

    time.sleep(1)

    # use splinter to click the button to bring up the full resolution image of the Featured Image
    results = browser.find_by_id('full_image').first.click()

    time.sleep(3)

    # scrape the new browser into soup and use soup to find the full resolution Featured Image
    # save image of url to variable 'img_url' + then to variable 'featured_image_url' for full path of image
    html = browser.html
    soup = bs(html, "html.parser")
    img_url = soup.find("img", class_="fancybox-image")["src"]
    featured_image_url = 'http://jpl.nasa.gov' + img_url

    # add data to our mars data dict
    mars_data["featured_image_url"] = featured_image_url

    # visit the space facts mars website
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url) 

    time.sleep(2) 

    # scrape the mars facts table using pandas and get 1st table
    tables = pd.read_html(facts_url) 
    df = tables[0]
    html_table = df.to_html()
    mars_facts = html_table.replace('\n', '')

    # add mars table data to mars dict data
    mars_data["mars_facts"] = mars_facts

    # visit USGS Astrogeology site 
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    astro_url = 'https://astrogeology.usgs.gov'
    time.sleep(5)

    # create hemisphere list of dictionaries
    mars_dict_list = []
    
    # use splinter to click the links/buttons to bring up the title & full resolution image of cerberus 
    first_results = browser.click_link_by_partial_text("Cerberus")
    
    time.sleep(2)
    # scrape the new browser into soup and use soup to find the title and full resolution image
    # save image of url to variable 'img_url' + then to variable 'cereberus_image_url' for full path of image
    # save image url string and title to a dictionary and add to list
    html = browser.html
    soup = bs(html, "html.parser")
    first_title = soup.body.find('h2', class_="title").text
    img_url = soup.find("img", class_="wide-image")["src"]
    cereberus_image_url = astro_url + img_url
    dictionary = {}
    dictionary["title"] = first_title
    dictionary["img_url"] = cereberus_image_url
    mars_dict_list.append(dictionary)

    # go back to main page
    browser.visit(usgs_url)

    # use splinter to click the links/buttons to bring up the full resolution image of shiaparelli 
    second_results = browser.click_link_by_partial_text("Schiaparelli")

    time.sleep(2)
   
    # scrape the new browser into soup and use soup to find the title and full resolution Schiaparelli Image
    # save image of url to variable 'img_url' + then to variable 'schiap_image_url' for full path of image
    # save image url string and title to a dictionary and add to list
    html = browser.html
    soup = bs(html, "html.parser")
    second_title = soup.body.find('h2', class_="title").text
    img_url = soup.find("img", class_="wide-image")["src"]
    schiap_image_url = astro_url + img_url
    dictionary = {}
    dictionary["title"] = second_title
    dictionary["img_url"] = schiap_image_url
    mars_dict_list.append(dictionary)

    # go back to main page
    browser.visit(usgs_url)

    # use splinter to click the links/buttons to bring up the full resolution image of syrtis 
    third_results = browser.click_link_by_partial_text("Syrtis")

    time.sleep(2)

    # scrape the new browser into soup and use soup to find the title & full resolution Syrtis Image
    # save image of url to variable 'img_url' + then to variable 'syrtis_image_url' for full path of image
    # save image url string and title to a dictionary and add to list
    html = browser.html
    soup = bs(html, "html.parser")
    third_title = soup.body.find('h2', class_="title").text
    img_url = soup.find("img", class_="wide-image")["src"]
    syrtis_image_url = astro_url + img_url
    dictionary = {}
    dictionary["title"] = third_title
    dictionary["img_url"] = syrtis_image_url
    mars_dict_list.append(dictionary)

    # go back to main page
    browser.visit(usgs_url)

    # use splinter to click the links/buttons to bring up the full resolution image of valles
    fourth_results = browser.click_link_by_partial_text("Valles")

    time.sleep(2)

    # scrape the new browser into soup and use soup to find the title and full resolution Valles Image
    # save image of url to variable 'img_url' + then to variable 'valles_image_url' for full path of image
    # save image url string and title to a dictionary and add to list
    html = browser.html
    soup = bs(html, "html.parser")
    fourth_title = soup.body.find('h2', class_="title").text
    img_url = soup.find("img", class_="wide-image")["src"]
    valles_image_url = astro_url + img_url
    dictionary = {}
    dictionary["title"] = fourth_title
    dictionary["img_url"] = valles_image_url
    mars_dict_list.append(dictionary)

    # add list of dictionaries to mars_data
    mars_data["mars_dict_list"] = mars_dict_list

    
    # Close the browser after scraping 
    browser.quit()

    # Return results
    return mars_data
