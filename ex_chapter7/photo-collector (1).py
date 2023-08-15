#!/usr/bin/python3
################################################################################
import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import wget # pip3 install --user wget
import csv
################################################################################
url = 'https://waarnemingen.be'
# Print messages part 1 to ask for input
print("="*80)
print("User input to collect photos and metadata from "+url)
print("="*80)
date_after = input("\nGive date after (in YYYY-MM-DD format): ")
url_photos = url + "/photos/?date_after=" + date_after # 2021-08-01
date_before = input("\nGive date before (in YYYY-MM-DD format): ")
url_photos = url_photos + "&date_before=" + date_before # 2021-08-01
print("\nSpecies groups: [1] Birds | [2] Mammals | [3] Reptiles and amphibians | [4] Butterflies")
species_group = input("Give number of species group: ") # species_group = "4"
url_photos = url_photos + "&species_group=" + species_group # 4
print("\nProvinces: [14] Limburg | [15] West-Vlaanderen | [16] Oost-Vlaanderen | [17] Antwerpen")
province = input("Give number of province: ") # province = "15"
url_photos = url_photos + "&province=" + province # 15
print("\nRarities: [1] >= common | [2] >= relatively common | [3] >= rare | [4] very rare")
rarity = input("Give number of rarity: ") # rarity = "3"
url_photos = url_photos + "&rarity=" + rarity # 3'
################################################################################
# Print messages part 2
print("\n")
print("="*80)
print("Running photo collector script")
print("URL={}".format(url_photos))
print("="*80)
# Fetch webpage and save in soup object
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
request = urllib.request.Request(url_photos, headers = headers)
response = urllib.request.urlopen(request)
response_data = response.read().decode('utf-8')
soup = BeautifulSoup(response_data, 'html.parser')
# Create photos folder if it does not exist
if not os.path.isdir("photos"):
    os.mkdir("photos")
os.chdir("photos")
################################################################################
# In soup object: look for all figure class lightbox-gallery
figures_list = soup.find_all("figure", {"class":"lightbox-gallery"})
counter = 1
with open('metadata.csv', mode='w') as result_file:
    result_writer = csv.writer(result_file,delimiter=';')
    # header row for csv
    result_writer.writerow(["id","scientific name","common name","location","photo name"])
    for figure in figures_list:
        # Parse metadata using tags
        image = figure.find("img")
        image_url = url + image["src"]
        image_url = image_url.replace("?w=500&h=375","")
        filename = wget.download(image_url)
        print("\nImage: {}".format(image_url))
        common_name = figure.find("span", {"class":"species-common-name"})
        print("Species common name: {}".format(common_name.string))
        scientific_name = figure.find("i", {"class":"species-scientific-name"})
        print("Species scientific name: {}".format(scientific_name.string))
        location = figure.find_all("a", {"class":"mod-stealth"})[2]
        location_text = location.text.strip()
        print("Location: {}".format(location_text))
        # Save metadata row to file
        result_writer.writerow([counter,scientific_name.string,common_name.string,location_text,filename])
        # Increase counter
        counter+=1
# Close csv file
result_file.close()
################################################################################