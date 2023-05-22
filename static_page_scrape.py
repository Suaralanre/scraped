# importing the required libraries for the web scraper
import requests 
from bs4 import BeautifulSoup
import csv

# url of website to be scraped 
url = "https://realpython.github.io/fake-jobs/"

# using requests module to access the url
r = requests.get(url)

r.raise_for_status()

# using the beautifulsoup library to create an
# instance of a soup object
# It is basically the page in binary.
# It is parsed with the inbuilt 'htmlparser'
# I could have installed the 'lxml' parser and used
# that instead
soup = BeautifulSoup(r.content, 'html.parser')

# attribute 'find' of the soup object
# is the entire page containing the jobs and other
# info in addition to their html and css tags.
# this code could also have been:
# all_jobs = soup.select('div #ResultsContainer')
# but using select creates a list of 
# tags(including their attributes and text)
# and the attributes.find and find_all don't apply.
all_jobs = soup.find('div', id='ResultsContainer')

# an instance of individual jobs
single_job = all_jobs.find_all('div', class_='card-content')


with open("jobs.csv", 'wb', newline='') as f:

    # creating a csv object to store the information from the instances
    job_object = csv.DictWriter(f, ['Role', 'Company', 'Location'])

    # creates a header for the table from the object's
    # initialized instance
    job_object.writeheader()

    # a for loop to get the information needed
    # from each instance of the job
    for job in single_job:
        role = job.find('h2', class_='title is-5').text
        company = job.find('h3', class_='subtitle is-6 company').text
        location = job.find('p', class_='location').text.strip()

        job_object.writerow({'Role': role, 'Company': company, 'Location': location})
