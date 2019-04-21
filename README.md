# butterknife
A simple web scraping library for python3 utilizing BeautifulSoup

## Basic Usage
Example:
```
>>> from bs4 import BeautifulSoup
>>> from butterknife.scrape import Scrape
>>> example_scrape=Scrape(["https://en.wikipedia.org/wiki/List_of_sequenced_animal_genomes","https://en.wikipedia.org/wiki/List_of_sequenced_archaeal_genomes"])
>>> example_scrape.SoupifyAll()
>>> print ([i['url'] for i in example_scrape.pages])
['https://en.wikipedia.org/wiki/List_of_sequenced_animal_genomes', 'https://en.wikipedia.org/wiki/List_of_sequenced_archaeal_genomes']
>>> bodyout0=example_scrape.pages[0]['html'].select('body')
>>> bodyout0[0].text[:100]
'\n\n\n\n\n\n\n\nList of sequenced animal genomes\n\nFrom Wikipedia, the free encyclopedia\n\n\nJump to navigation'
```
Individual pages can use the PagePull object to get the source html as one large string.

```
>>> from butterknife.scrape import PagePull>>> page_test=PagePull("https://en.wikipedia.org/wiki/List_of_sequenced_archaeal_genomes")
>>> print(page_test.htmlcontent[:100])
b'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title'
>>> str(page_test)[:100]
'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title'
>>> 
```

## Tests/Examples
The scripts in tests aren't true tests as much as examples of usage that can be executed on their own if moved to the root directory. If you'd like to run them as a test suite, just execute tests.py:
```
user@computer:~/butterknife$ python3 tests.py 
===========================SCRAPETEST STARTED============================
Syracuse, New YorkCityDowntown Syracuse(aerial view; Onondaga Lake in background)
FlagNickname(s): The 'Cuse, Salt City, Emerald City, The Heart of New YorkLocation in Onondaga County and the state of New York.SyracuseLocation in state of New York and the USAShow map of New YorkSyracuseSyracuse (the United States)Show map of the United StatesCoordinates: 43°02′49″N 76°08′40″W﻿ / ﻿43.04694°N 76.14444°W﻿ / 43.04694; -76.14444Coordinates: 43°02′49″N 76°08′40″W﻿ / ﻿43.04694°N 76.14444°W﻿ / 43.04694; -76.14444Country United StatesState New YorkCountyOnondagaIncorporated1825 (village)Incorporated1847 (city)Named forSyracuse, SicilyGovernment • TypeMayor-Council • MayorBen Walsh (I) • Common Council
Members' List
President:• Helen Hudson (D)At Large Members:• Khalid Bey (D)• Michael Greene (D)• Timothy Rudd (D)• Steve Thompson (D)• D1: Joseph Carni (R)• D2: Chad Ryan (D)• D3: Susan Boyle (D)• D4: Latoya Allen (D)• D5: Joe Driscoll (D)
Area[1] • City25.61 sq mi (66.33 km2) • Land25.05 sq mi (64.87 km2) • Water0.56 sq mi (1.46 km2)  2.15%Elevation380 ft (116 m)Population (2010) • City145,170 • Estimate (2017)[2]143,396 • Density5,724.82/sq mi (2,210.33/km2) • Metro662,577Demonym(s)SyracusanTime zoneUTC−5 (Eastern) • Summer (DST)UTC−4 (Eastern Daylight Time)Area codes315, 680FIPS code36-73000GNIS feature ID0966966Websitewww.syrgov.net 


--------------------
New YorkCityClockwise, from top: Midtown Manhattan, Times Square, the Unisphere, the Brooklyn Bridge, Lower Manhattan with One World Trade Center, Central Park, the headquarters of the United Nations, and the Statue of Liberty
FlagSealWordmarkNickname(s): See Nicknames of New York CityInteractive map outlining New York CityNew YorkLocation within the state of New YorkShow map of New YorkNew YorkLocation within the United StatesShow map of the United StatesNew YorkLocation within North AmericaShow map of North AmericaCoordinates: 40°42′46″N 74°00′21″W﻿ / ﻿40.7127°N 74.0059°W﻿ / 40.7127; -74.0059Coordinates: 40°42′46″N 74°00′21″W﻿ / ﻿40.7127°N 74.0059°W﻿ / 40.7127; -74.0059[1]Country United StatesState New York
RegionMid-AtlanticConstituent counties / (boroughs)Bronx (The Bronx)Kings (Brooklyn)New York (Manhattan)Queens (Queens)Richmond (Staten Island)
Historic coloniesNew NetherlandProvince of New YorkSettled1624Consolidated1898Named forJames, Duke of YorkGovernment[2] • TypeMayor–Council • BodyNew York City Council • MayorBill de Blasio (D)Area[1] • Total468.484 sq mi (1,213.37 km2) • Land302.643 sq mi (783.84 km2) • Water165.841 sq mi (429.53 km2) • Metro13,318 sq mi (34,490 km2)Elevation[3]33 ft (10 m)Population (2010)[6] • Total8,175,133 • Estimate (2017)[7]8,622,698 • Rank1st, U.S. • Density28,491/sq mi (11,000/km2) • MSA (2017)20,320,876[4] (1st) • CSA (2017)23,876,155[5] (1st)Demonym(s)New YorkerTime zoneUTC−05:00 (EST) • Summer (DST)UTC−04:00 (EDT)ZIP Codes100xx–104xx, 11004–05, 111xx–114xx, 116xxArea code(s)212/646/332, 718/347/929, 917FIPS code36-51000GNIS feature ID975772Major airportsJohn F. Kennedy International Airport, Newark Liberty International Airport, LaGuardia AirportCommuter railLIRR, Metro-North, NJ TransitRapid transitSubway, Staten Island Railway, PATHGDP (City, 2015)US$807 billion[8]GMP (Metro, 2017)US$1.7 trillion[9]Largest borough by areaQueens – 109 square miles (280 km2)Largest borough by populationBrooklyn (2,636,735 – 2015 est)[10]Largest borough by GDP (2015)Manhattan – US$630 billion[8]WebsiteNYC.gov 


--------------------
Los Angeles, CaliforniaCityCity of Los Angeles
Clockwise from top: Downtown seen from Echo Park, Griffith Observatory, the Theme Building at Los Angeles International Airport, Venice Beach, Vincent Thomas Bridge, City Hall and the Hollywood Sign
FlagSealNickname(s): L.A., City of Angels,[1] The Entertainment Capital of the World, The Big Orange,[1] La-la-land, Tinseltown[1]Location within Los Angeles CountyLos AngelesLocation within Greater Los AngelesShow map of the Los Angeles metropolitan areaLos AngelesLocation within CaliforniaShow map of CaliforniaLos AngelesLocation within the United StatesShow map of the United StatesLos AngelesLocation within North AmericaShow map of North AmericaLos AngelesLocation on EarthShow map of EarthCoordinates: 34°03′N 118°15′W﻿ / ﻿34.050°N 118.250°W﻿ / 34.050; -118.250Coordinates: 34°03′N 118°15′W﻿ / ﻿34.050°N 118.250°W﻿ / 34.050; -118.250Country United StatesState CaliforniaCounty Los AngelesCSALos Angeles-Long BeachMSALos Angeles-Long Beach-AnaheimPuebloSeptember 4, 1781[2]City statusMay 23, 1835[3]IncorporatedApril 4, 1850[4]Named forOur Lady, Queen of the AngelsGovernment • TypeMayor-Council-Commission[5] • BodyLos Angeles City Council • MayorEric Garcetti (D)[6] • City AttorneyMike Feuer (D)[6] • City ControllerRon Galperin (D)[6]Area[7] • Total502.76 sq mi (1,302.15 km2) • Land468.74 sq mi (1,214.03 km2) • Water34.02 sq mi (88.12 km2)  6.7%Elevation[8]305 ft (93 m)Highest elevation[9]5,074 ft (1,547 m)Lowest elevation[9]0 ft (0 m)Population (2010)[10] • Total3,792,621 • Estimate (2017)[11]3,999,759 • Rank1st, California2nd, U.S. • Density8,483.02/sq mi (3,275.32/km2) • Urban[12]12,150,996 • Metro[13]13,131,431 (U.S.: 2nd) • CSA[14]18,679,763 (U.S.: 2nd)Demonym(s)AngelenoTime zoneUTC−08:00 (Pacific) • Summer (DST)UTC−06:00 (PDT)ZIP Codes
List
90001–90084, 90086–90089, 90091, 90093–90097, 90099, 90101–90103, 90174, 90185, 90189, 90291–90293, 91040–91043, 91303–91308, 91311, 91316, 91324–91328, 91330,91331, 91335, 913340,  91342–91349, 91352–91353, 91356–91357, 91364–91367, 91401–91499, 91504–91505, 91601–91609[15] 
Area codes213/323, 310/424, 747/818FIPS code06-44000GNIS feature IDs1662328, 2410877Primary AirportLos Angeles International AirportSecondary AirportsHollywood Burbank AirportJohn Wayne AirportLong Beach AirportOntario International AirportInterstates       U.S. Highways      
Former Routes
     
State Routes                
Unconstructed Routes
 
 
Former Routes
   
Rapid Transit        (under construction)  Commuter Rail  (planned)WebsiteOfficial website  


--------------------
===========================SCRAPETEST ENDED==============================
user@computer:~/butterknife$
```
Check the output, and if it looks right based on the individual test scripts you are good to go.
