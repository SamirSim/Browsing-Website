import selenium #Library for navigating through webpages
from selenium import webdriver #Main driver used
from treelib import Node, Tree #Tool implementing tree structures

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#Here the path for the webdriver of Chrome is given as parameter, or can be added on the path variable of the system
driver.get('http://curlie.org/')

tree = Tree() #Initialize the tree structure to save the categories
categories = driver.find_elements_by_xpath('//aside/div/h2[@class="top-cat"]/a')
#Extract the main categories using a XPATH query
#Here it return all the a elements that are in the hierarchy aside-div...with a h2 tag that has 'top-cat' as a class attribute
urls = []
tree.create_node("Curlie Site", "curlie") #Create the root node, with "curlie" as ID

for category in categories: #Loop through all the main categories
    tree.create_node(category.text, category.text, parent="curlie")
    #Create a node with as a name the name of the category, and as ID the name, and as parent the root node
    urls.append((category.get_attribute("href"), category.text)) #Fill a list of couples of categorie's link and name

for url in urls: #Loop through all the links saved previously
    driver.get(url[0]) #Get the link of the category, and navigate through it using the webdriver
    parentId = url[1] #Get the name of the category
    categories = driver.find_elements_by_xpath('//section[@class="children"]/div/div[@class="cat-item"]/a')
    #Get all the children categories of the current category
    
    for category in categories: #Loop through all the categories
        tree.create_node(category.text, parentId+category.text, parent=parentId)
        #Create a node with as a name the name of the category, and as ID the name of the father node appended with the category name (I explain why in the attached document), and as parent the root node
        urls.append((category.get_attribute("href"), parentId+category.text))
        #Add to the same list the new category link and name, so the program will pass through it too

tree.show() #Display the final tree

tree.save2file('tree.txt') #Save the structure into a text file




