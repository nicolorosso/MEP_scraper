import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL to the webpage containing information about the ITRE members
url = 'https://www.europarl.europa.eu/committees/it/itre/home/members'

# Use the requests library to get the HTML content of the webpage
content = requests.get(url)

# Use the BeautifulSoup library to parse the HTML content
soup = BeautifulSoup(content.text, 'html.parser') 

# Create an empty list to store information about the members
deputati = []

# Find the table containing information about the members
table = soup.find("div", attrs = {"class": "erpl_member-list"})

# Define a function that extracts information from a row
def extract_info(row):
    deputato = {}
    deputato['Name'] = row.find("div", attrs = {"class": "erpl_title-h5 t-item"}).text
    deputato['link'] = row.a['href']
    deputato['Carica'] = row.find_all("div", attrs = {"class": "sln-additional-info mb-25"})[0].text
    deputato['Gruppo Politico'] = row.find_all("div", attrs = {"class": "sln-additional-info mb-25"})[1].text
    deputato['Paese'] = row.find("div", attrs = {"class": "sln-additional-info "}).text
    return deputato

# Iterate through each row in the table
for row in table.findAll('div', attrs = {'class':'col-6 col-sm-4 col-md-3 col-lg-4 col-xl-3 text-center mb-3 erpl_member-list-item a-i'}):
    deputati.append(extract_info(row))

# Create a DataFrame from the list of dictionaries
dev = pd.DataFrame.from_dict(deputati)

# Remove rows where the country is Italy or the role is "Membro sostituto"
dev = dev.drop(dev[dev.Paese == 'Italia'].index)
dev =  dev.drop(dev[dev.Carica == 'Membro sostituto'].index)

# Create an empty list to store email addresses
emails = []

# Define a pattern for finding email addresses in the links
email_pattern = 'a[href^=mailto]'

# Define a function that extracts email addresses from a link
def extract_email(link):
    # Use the requests library to get the HTML content of the profile page
    content = requests.get(link)
    soup = BeautifulSoup(content.text, 'html.parser')

    for email in soup.select(email_pattern2):
        data = email['href']
        data = data.split('?')[0]  # remove `?subject=?`
        data = data.replace('mailto:', '') # remove mailto:
        data = data.replace(r"[at]", "@").replace(r"[dot]", ".")
        data = data[::-1]
        emails.append(data)

#Iterate through each link in the 'link' column of the DataFrame
for link in dev['link']:
extract_email(link)

#Create a regular expression to match email addresses that are not from the eurodep domain
regex = re.compile("^[A-Za-z0-9._%+-]+@(?!europarl.europa.eu)[A-Za-z0-9.-]+.[A-Za-z]{2,4}$")

#Filter the list of email addresses to exclude those that do not match the regular expression
filtered = [i for i in emails2 if not regex.match(i)]

#Add the filtered email addresses to the DataFrame as a new column called 'emails'
dev['emails'] = filtered

#Export the code to an excel file
dev.to_excel(r'your directory', index=False, header=True)

