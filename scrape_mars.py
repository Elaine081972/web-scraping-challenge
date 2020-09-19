from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver 
     #path for MAC 
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    #executable_path = {"executable_path": "C:/Users/Heather Bree/chromedriver_win32/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
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
    news_p["news_p"] = news_p

    # visit the URL from the Jet Propulsion Laboratory to scrape
    jet_url = 'http://jpl.nasa.gov/spaceimages/?search=&category=Mars/'
    browser.visit(jet_url)

    time.sleep(1)

    # use splinter to click the button to bring up the full resolution image of the Featured Image
    results = browser.find_by_id('full_image').first.click()

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

    time.sleep(4)

     










    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url
    }

    # BONUS: Find the src for the sloth image (need specific knowledge of page to grab that image)
    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Close the browser after scraping (splinter is finding it for us!! to close it)
    browser.quit()

    # Return results
    return costa_data
