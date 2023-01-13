# MEP_scraper
The above code will scrape information about members of the ITRE (Industry, Research and Energy) committee of the European Parliament from the website https://www.europarl.europa.eu/committees/it/itre/home/members and extract their name, link to their profile page, role, political group, country of origin and email addresses. 

The information will be stored in a DataFrame and only members that are not from Italy and not substitute members will be kept. This particular feature can be easily changed or removed by commenting (#) on the dev = dev.drop(dev[dev.Paese == 'Italia'].index) line. 

Emails that are not of eurodep domain will be removed. 
