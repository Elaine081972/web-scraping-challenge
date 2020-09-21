# web-scraping-challenge

This assignment "Mission to Mars" builds a web application. It combines the challenges of web-scraping data from various websites and displaying them in a single HTML page. 

1. A Jupyter Notebook file called "mission_to_mars.ipynb is used to complete the initial scraping and analysis.
BeautifulSoup, Pandas and Requests/Splinter are used for this:

- NASA Mars News is scraped for the latest Title and Paragraph Text
- Jet Propulsion Laboratory site is scraped for the featured image
- Space-Facts site is scraped for mars facts
- USGS Astrogeology site is scraped for the four hemisphere titles and images of mars

2. The Jupyter Notebook code is then consolidated into a Python script called scrape_mars.py. A function called scrape executes all of the scraping code and is returned into one Python dictionary containing all the data.

3. A flask app.py file creates the route /scrape to import the scrape_mars.py script and call the scrape function.
The return value is stored in mongo as a Python dictionary. A root route / is created that queries the Mongo database and passes the data into an HTML template to display the data.

4. An HTML file called index.html will take the mars dictionary and display all the data in the correct HTML elements. An initial page will display even without data, and clicking "scrape new data" will initiate the flask app to scrape the data and render on the HTML page.

Notes for running web application:

- executable path - make sure the necessary path is enabled depending on MAC or Windows user status
- a mongo database must be started and running successfully
- run the app.py file and a localhost port open for the HTML to display 

