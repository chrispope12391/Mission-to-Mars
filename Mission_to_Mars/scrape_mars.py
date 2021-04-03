from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    ##This will the 
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain mars article information
    # mars_title = soup.find_all('div', class_='content_title')
    # mars_teaser = soup.find('div', class_='article_teaser_body').text

    mars_scrape = {}

    mars_scrape['title'] = soup.find('div', class_='content_title').text
    mars_scrape['teaser'] = soup.find('div', class_='article_teaser_body').text
    browser.quit()
    
    # This will pull the featured image
    new_browser = Browser('chrome', **executable_path, headless=False)

    image_url = "https://spaceimages-mars.com/"
    new_browser.visit(image_url)

    new_browser.quit()

    return mars_scrape
