
API.py

What is the idea behind this project?
I want to track my results of all the module i have completed in the previous semester. I want to have an overview of each module i have completed and an overview of all results for each module. This would be a good way of tracking my perforamance and also it would be reusable for further analysis with other application that i design. This API would deal as easy accessible data to integrate into any other project. 
In real world an API like this would be convenient to track data of multiple students. It could be used to further analyse and visualize in a dashboard (like Studenthub for FHNW students)

In order to do that, I created a json file with all the existing data for my modules and results. Then I used Flask to create a locally run application on port 8000. For the before mentioned json data, i created Endpoint URLs:

For all modules:                        http://127.0.0.1:8000/modul
For all results of a specific module:   http://127.0.0.1:8000//modul/<name of module>

Why did I chose REST api and not GraphQL
First of all it is very easy to implement for a easy problem like this. The resuest functions are very simple to implement and do exactly what I need them to do.




Selenium Crawler

What is the idea behind this project?
I want to have an overview of all the news articles in the news portal of the FHNW. Furthermore i want to track the number of likes and comments of each of those articles. That way, I can further analyse the articles regarding their like and comments, which article has more interactions, which doesn't, and so on. Outside of this specific case, an idea like this would be very helpful for marketers or other industries that rely on news. They could track what kind of articles have a lot of traction and shift their business interests accordingly.

The Website I crawled is: https://inside.fhnw.ch/

I used Chrome to navigate through the website. For that I downloaded the appropriate chromedriver.

chrome version: chrome://settings/help
chromedrivers:  https://chromedriver.chromium.org/downloads

Using selenium, I logged in with my personal FHNW credentials (I removed them for privacy reasons, but created variables for the credentials that can be filled by the user of the script). Then I navigated through the website by locating elements and buttons. Each page on the news portal had 10 articles, which had likes and comments assigned to them. The Spider goes through 300 pages, and therefore extracts data for 3000 articles.
 
Locating elements: https://selenium-python.readthedocs.io/locating-elements.html

There is a test csv file with a test i made (test_result_webcrawling.csv)
