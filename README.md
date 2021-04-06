# web-scraping-challenge
Created a launchable HTML file population with information regarding the planet Mars that was scraped from various websites.


## Getting Started

1. Create a new repository and title it as you please. My repository is titled "web-scraping-challenge.

1. Clone the new repository to your computer.

1. Inside your local git repository, create a directory for the web scraping challenge. Use a folder name to correspond to the challenge: Missions_to_Mars.

1. Add your notebook files to this folder as well as your flask app.

1. Push the above changes to GitHub or GitLab.

## Summary

### Scraping

The first thing we did was to create a jupyter notebook to create a road map for our app.py follow while creating a database to house all of our scraped Mars information. There are four different pieces we seeked to obtain:

1. The title and teaser article from the website Red Planet's featured article.
    * __Website:__ https://redplanetscience.com/

1. The featurewd image from the website Space Images (Mars).
    * __Website:__ https://spaceimages-mars.com/

1. A facts table of Earth and Mars from the website Galaxy Facts (mars).
    * __Website:__ https://galaxyfacts-mars.com/

1. The image and the name of each of Mar's Hemispheres from the website Mars Hemispheres.
    * __Website:__ https://marshemispheres.com/

### MongoDB and Flask Appliation

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. 

* Convert your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called ("/scrape") that will import your scrape_mars.py script and call your scrape function.
    * Store the return value in Mongo as a Python Dictionary.

* Once this is done, you should have a database in Mongo that resembles this:

![mongo](https://user-images.githubusercontent.com/75814760/113653370-55c38780-965b-11eb-90f7-f49a7372c886.jpg)

* Create a root route ("/") that will query your Mongo database and pass the mars data

* Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

* Once you have clicked your scrape button on your running Flask application and styled your index.html file to displayed the scraped data accordingly, you will end up with a final result that looks similarly to this:

![flask](https://user-images.githubusercontent.com/75814760/113653918-5872ac80-965c-11eb-8630-14628762290a.jpg)

## Built With
* Jupyter Notebook
* Visual Studio Code
* MongoDB
* Flask

## Languages
* Python
* Pandas
* BeautifulSoup
* Splinter
* HTML
* CSS
* Bootstrap

## Author(s)
* Chris Pope

## Contact:
__Email:__ popex107@umn.edu