#!/usr/bin/python3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
before = input("give date before ")

species_group={1:'birds',2:'mamals',3:'rep', 4:'butter'}
name = input("kies dier ")
getal=int(name)


provintie_group={14:'Lim',15:'west',16:'oost', 17:'ant'}
iets = input("kies provintie ")
provintie=int(iets)
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    url = 'https://waarnemingen.be/photos'
    params= urllib.parse.urlencode( {'date_after':'2021-08-01', 'date_before':'2021-08-01', 'species_group':'4', 'province':'15', 'rarity' : '3'})
    params = params.encode('utf-8')
    response = urllib.request.urlopen(url, params)
    
    
    response_data = response.read()
    content = response.read()
    soup = BeautifulSoup(content,'html.parser')
except Exception as e:
    print(str(e))


