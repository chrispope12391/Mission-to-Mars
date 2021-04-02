from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain mars article information
    mars_results = soup.find_all('div', class_='col-md-8')

    mars_title = []
    mars_teaser = []

    # Identify the title and teaser article in each article
    for result in mars_results:

        # Error handling
        try:

            #identify and return the title
            title = result.find('div', class_='content_title').text
            #identify and return the teaser article
            teaser = result.find('div', class_='article_teaser_body').text
            mars_title.append(title)
            mars_teaser.append(teaser)

            #Print title and teaser article
            if (title and teaser):

                print('-------------------------------------------')
                print(title)
                print(teaser)

        except AttributeError as e:
            print("No Title Available")

    browser.quit()
    
    return mars_title[0]
    return mars_teaser[0]

