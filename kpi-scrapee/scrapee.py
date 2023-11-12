import sys
from parse import parse
from scrape import scrape
from clean import clean


userSites = sys.argv[1]

with open(userSites) as s:
	sites = s.read()

listSites = sites.split(",")

scrapes = []

for site in listSites[:-1]:
	url = "http://wordpress.evergreen.edu/"+site+"/robots/"
	scrapes.append(scrape(url))

csv = "name,team_company,num_cx_visit,motorolla,fav_midnight_snack\n"

#print(scrapes)

for scrape in scrapes:
	csv = csv + clean(parse(scrape, "BEGINDATABEGIN", "DATAENDDATA"))

f = open("scraped.csv","w")
f.write(csv)
f.close()

print(csv)

