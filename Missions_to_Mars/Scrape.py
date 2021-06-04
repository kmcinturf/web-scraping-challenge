#Import our Modules
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time 

# # Extract
def Scrape():
   
    # Setup splinter browser driver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Go to Mars News Site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    #Scrape News Title and Paragraph text, then create Variable 

    #Parse home page to gather links to traverse   
    bs = BeautifulSoup(browser.html, 'html.parser')
    titles = bs.find_all('div',class_="content_title")
    Paragraph = bs.find_all('div',class_="article_teaser_body")

    for titles in titles:
        news_title=titles.text

    for Paragraph in Paragraph:
        news_p =Paragraph.text

    #Go to Mars News Site
    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)

    bs = BeautifulSoup(browser.html, 'html.parser')
    button = bs.find_all('div',class_="header")
    link = bs.find_all('a',class_ ="showimg fancybox-thumbs")
    #image_url = https://spaceimages-mars.com/image/featured/mars2.jpg
    link3 = bs.find_all('a',href=True)

    for a in link:
        featured_image_url=url2+a['href']

    #Go to Mars News Site
    url3 = 'https://galaxyfacts-mars.com'
    
    tables = pd.read_html(url3)
    table1=tables[0]
    table1.to_html("mars.html")
   
    #Mars Hemispheres
    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)
    bs = BeautifulSoup(browser.html, 'html.parser')
    results = bs.find_all('a',class_="itemLink product-item")
    h3_list = []
    aref_list = []
    for result in results:
        aref_list.append(result['href'])
        w=result.find_all("h3")
        for x in w:
            h3_list.append(x.text)

    bs = BeautifulSoup(browser.html, 'html.parser')
    img_url = []
    title = []
    for h3 in h3_list:
        time.sleep(1)
        #browser.click_link_by_href(url4 + aref)
        browser.links.find_by_partial_text(h3).click()
        time.sleep(1)
        bs = BeautifulSoup(browser.html, 'html.parser')
        image = bs.find_all("a",target="_blank", href=True)[2]
        for images in image:
            img_url.append(image['href'])
        browser.back()

    title=h3_list[0:4]

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "url4 + images/valles_marineris_enhanced-full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "url4 + images/full.jpg "},
    {"title": "Schiaparelli Hemisphere", "img_url": "url4 + images/schiaparelli_enhanced-full.jpg "},
    {"title": "Syrtis Major Hemisphere", "img_url": "url4 + images/syrtis_major_enhanced-full.jpg "}]
  
    
    return hemisphere_image_urls
    return news_title
    return news_p







