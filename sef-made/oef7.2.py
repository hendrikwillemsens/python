#!/usr/bin/python3

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
print("=========================================================")
print("User input from https://waarnemingen.be")
print("=========================================================")
after = input("give date after (YYYY-MM-DD format):")
print("\n")
before = input("give date before (YYYY-MM-DD format):")
print("\n")
species = input("[1] Birds  |   [2] Mammals  |    [3] Reptiles and ampibians  |    [4] Butterflies \n Give number of species group: ")
print("\n")
provinces = input("[14] Limburg  |   [15] West-Vlaanderen  |    [16] Oost-vlaanderen  |    [17] Antwerpen \n Give number of province: ")
print("\n")
Rarities = input("[1] >=common  |   [2] >=relatively common  |    [3] >=rare  |    [4] very rare \n Give number of rarity: ")
print("\n")

url = "https://waarnemingen.be/photos/?date_after={}&date_before={}&species_group={}&province={}&rarity={}".format(after, before, species, provinces, Rarities)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    response_data = response.read().decode('utf-8')
    soup = BeautifulSoup(response_data, 'html.parser')
    save_file = open('oef72.html','w')
    save_file.write(str(response_data))
    save_file.close()
    find = soup.find_all("a", {"class": "lightbox-gallery-image"})
    gewoon = soup.find_all("span", {"class": "species-common-name"})
    speciaal = soup.find_all("i", {"class": "species-scientific-name"})
    location = soup.find_all("a", {"class": "mod-stealth"})
    

    r = 1
    c = 1
    
    if c == 1:
        for lightbox in find:
            for name in gewoon:
                for scientific in speciaal:
                    media = lightbox.attrs
                    Image = "https://waarnemingen.be" + str(media["href"])
                    print("Image: {} ".format(Image))
                    
                    common = name.string
                    print("species common name: {}".format(common))
                    
                    hendrik = scientific.string
                    print("species scientific name: {}".format(hendrik))
                    print("\n")
                
                

                
           
    
       
        
           
    

except Exception as e:
    print(str(e))





