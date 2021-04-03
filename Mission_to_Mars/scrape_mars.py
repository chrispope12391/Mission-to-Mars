from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
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
    mars_results = soup.find_all('div', class_='content_title')

    mars_scrape = {}
    mars_teaser = []

    mars_scrape['title'] = soup.find('div', class_='content_title').text
    browser.quit()
    
    return mars_scrape
