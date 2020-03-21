import pytest


@pytest.fixture
def simple_article() -> str:
    return "this is a simple article written by a simple person this article is used to validate the test"


@pytest.fixture
def simple_string() -> str:
    return "this is cool this this cool "


@pytest.fixture
def complex_sentences() -> str:
    [
        "Affirmative actions such as the New Economic and the National Development Policy which superseded it were implemented to advance the standing of the bumiputera consisting of Malays and the indigenous tribes who are considered the original inhabitants of Malaysia over non-bumiputera such as Malaysian Chinese and Malaysian Indians",
        "These policies provide preferential treatment to bumiputera in employment education scholarships business and access to cheaper housing and assisted savings",
        "However it has generated greater interethnic resentment",
        "There is ongoing debate over whether the laws and society of Malaysia should reflect secular or Islamic principles",
        "Islamic criminal laws passed by the Pan-Malaysian Islamic Party with the support of United Malays National Organisation (UMNO) state assemblymen in the state legislative assembly of Kelantan have been blocked by the federal government on the basis that criminal laws are the responsibility of the federal government",
        "Kuala Lumpur was the site of the first East Asia Summit in 2005",
        "Malaysia's foreign policy is officially based on the principle of neutrality and maintaining peaceful relations with all countries regardless of their political system",
        "The government attaches a high priority to the security and stability of Southeast and seeks to further develop relations with other countries in the region",
        "Historically the government has tried to portray Malaysia as a progressive Islamic while strengthening relations with other Islamic states",
        "A strong tenet of Malaysia's policy is national sovereignty and the right of a country to control its domestic affairs",
        "Malaysia signed the UN treaty on the Prohibition of Nuclear Weapons",
        "The Spratly Islands are disputed by many states in the area and a large portion of the South China Sea is claimed by China",
        "Unlike its neighbours of Vietnam and the Philippines Malaysia historically avoided conflicts with China",
        "However after the encroachment of Chinese ships in Malaysian territorial Malaysia has become active in condemning China",
        "Brunei and Malaysia in 2009 announced an end to claims of each other's land and committed to resolve issues related to their maritime borders",
        "The Philippines has a dormant claim to the eastern part of Sabah",
        "Singapore's land reclamation has caused and minor maritime and land border disputes exist with Indonesia",
        "Examples of the Malaysian Armed Forces weaponry assets",
        "Clockwise from top right: Scorpène-class submarine PT-91M MBT tank Malaysian Army paratrooper with M4 and Su-30MKM fighter aircraft",
        "Malaysia has never recognised Israel and has no diplomatic ties with and has called for the International Criminal Court to take action against Israel over its Gaza flotilla raid",
        "Malaysia has stated it will establish official relations with Israel only when a peace agreement with the State of Palestine has been reached and called for both parties to find a quick resolution to realise the two-state solution",
        "Malaysian peacekeeping forces have contributed to many UN peacekeeping missions such as in Congo Iran–Iraq Namibia Cambodia Bosnia and Herzegovina Somalia Kosovo East Timor and Lebanon",
        "The Malaysian Armed Forces have three branches: the Royal Malaysian Navy the Malaysian Army and the Royal Malaysian Air Force",
        "There is no conscription and the required age for voluntary military service is 18",
        "The military uses 1",
        "5% of the country's GDP and employs 1",
        "23% of Malaysia's manpower",
        "The Five Power Defence Arrangements is a regional security initiative which has been in place for almost 40 years",
        "It involves joint military exercises held among Malaysia Singapore Australia New Zealand and the United Kingdom",
        "Joint exercises and war games have also been held with and the United States",
        "Malaysia Philippines Thailand and Vietnam have agreed to host joint security force exercises to secure their maritime border and tackle issues such as illegal immigration piracy and smuggling",
        "Previously there were fears that extremist militants activities in the Muslim areas of the southern and southern would spill over into Malaysia",
        "Because of this Malaysia began to increase its border security",
        "Geography Main article: Geography of Malaysia Malaysia is within the equatorial region where a tropical rainforest climate is apparent all year round",
        "Malaysia is the 66th largest country by total land area with a land area of 329613 km2 (127264 sq mi)",
        "It has land borders with Thailand in West Malaysia and Indonesia and Brunei in East Malaysia",
        "It is linked to Singapore by a narrow causeway and a bridge",
        "The country also has maritime boundaries with and the Philippines",
        "The land borders are defined in large part by geological features such as the Perlis River the Golok River and the Pagalayan Canal whilst some of the maritime boundaries are the subject of ongoing contention",
        "Brunei forms what is almost an enclave in with the state of Sarawak dividing it into two parts",
        "Malaysia is the only country with territory on both the Asian mainland and the Malay archipelago",
        "Tanjung Piai located in the southern state of Johor is the southernmost tip of continental Asia",
        "The Strait of Malacca lying between Sumatra and Peninsular Malaysia is one of the most important thoroughfares in global commerce carrying 40 per cent of the world's trade",
        "The two parts of Malaysia separated from each other by the South China Sea share a largely similar landscape in that both Peninsular and East Malaysia feature coastal plains rising to hills and mountains",
        "Peninsular Malaysia containing 40 per cent of Malaysia's land extends 740 km (460 mi) from north to south and its maximum width is 322 km (200 mi)",
        "It is divided between its east and west coasts by the Titiwangsa rising to a peak elevation of 2183 metres (7162 ft) at Mount part of a series of mountain ranges running down the centre of the peninsula",
        "These mountains are heavily and mainly composed of granite and other igneous rocks",
        "Much of it has been eroded creating a karst landscape",
        "The range is the origin of some of Peninsular Malaysia's river systems",
        "The coastal plains surrounding the peninsula reach a maximum width of 50 kilometres (31 mi) and the peninsula's coastline is nearly 1931 km (1200 mi) long although harbours are only available on the western side",
        "Mount Kinabalu the highest summit in the country East Malaysia on the island of Borneo has a coastline of 2607 km (1620 mi)",
        "It is divided between coastal regions hills and valleys and a mountainous interior",
        "The Crocker Range extends northwards from dividing the state of Sabah",
        "It is the location of the 4095 m (13435 ft) high Mount the tallest mountain in Malaysia",
        "Mount Kinabalu is located in the Kinabalu National Park which is protected as one of the four UNESCO World Heritage Sites in Malaysia",
        "The highest mountain ranges form the border between Malaysia and Indonesia",
        "Sarawak contains the Mulu Caves the largest cave system in the world in the Gunung Mulu National Park which is also a World Heritage Site",
        "Around these two halves of Malaysia are numerous islands the largest of which is Banggi",
        "The local climate is equatorial and characterised by the annual southwest (April to October) and northeast (October to February) monsoons",
        "The temperature is moderated by the presence of the surrounding oceans",
        "Humidity is usually high and the average annual rainfall is 250 cm (98 in)",
        "The climates of the Peninsula and the East differ as the climate on the peninsula is directly affected by wind from the mainland as opposed to the more maritime weather of the East",
        "Local climates can be divided into three regions highland lowland and coastal",
        "Climate change is likely to affect sea levels and rainfall increasing flood risks and leading to droughts",
        "Biodiversity Main article: Wildlife of Malaysia Native species in Malaysia clockwise from top-right: oriental pied hornbills hawksbill sea turtle proboscis monkey Malayan tiger",
        "Malaysia signed the Rio Convention on Biological Diversity on 12 June 1993 and became a party to the convention on 24 June 1994",
        "It has subsequently produced a National Biodiversity Strategy and Action Plan which was received by the convention on 16 April 1998",
        "The country is megadiverse with a high number of species and high levels of endemism",
        "It is estimated to contain 20 per cent of the world's animal species",
        "High levels of endemism are found on the diverse forests of Borneo's mountains as species are isolated from each other by lowland forest",
        "There are about 210 mammal species in the country",
        "Over 620 species of birds have been recorded in Peninsular with many endemic to the mountains there",
        "A high number of endemic bird species are also found in Malaysian Borneo",
        "250 reptile species have been recorded in the country with about 150 species of and 80 species of lizards",
        "There are about 150 species of and thousands of insect species",
        "The Exclusive economic zone of Malaysia is 334671 km2 (129217 sq mi) and 1",
        "5 times larger than its land area",
        "It is mainly in the South China Sea",
        "Some of its waters are in the Coral Triangle a biodiversity hotspot",
        "The waters around Sipadan island are the most biodiverse in the world",
        "Bordering East Malaysia the Sulu Sea is a biodiversity hotspot with around 600 coral species and 1200 fish species",
        "The unique biodiversity of Malaysian Caves always attracts lovers of ecotourism from all over the world",
        "Nearly 4000 species of fungi including lichen-forming species have been recorded from Malaysia",
        "Of the two fungal groups with the largest number of species in Malaysia the Ascomycota and their asexual states have been surveyed in some habitats (decaying wood marine and freshwater ecosystems as parasites of some plants and as agents of biodegradation) but have not been or have been only poorly surveyed in other habitats (as endobionts in soils on dung as human and animal pathogens); the Basidiomycota are only partly surveyed: bracket fungi and mushrooms and toadstools have been studied but Malaysian rust and smut fungi remain very poorly known",
        "Without doubt many more fungal species in Malaysia have not yet been recorded and it is likely that many of those when found will be new to science",
        "Some species of Rafflesia can grow up to 1 m (3 ft 3 in) in diameter making them the largest flowers in the world",
        "About two thirds of Malaysia was covered in forest as of with some forests believed to be 130 million years old",
        "The forests are dominated by dipterocarps",
        "Lowland forest covers areas below 760 m (2490 and formerly East Malaysia was covered in such which is supported by its hot wet climate",
        "There are around 14500 species of flowering plants and trees",
        "Besides rainforests there are over 1425 km2 (550 sq mi) of mangroves in and a large amount of peat forest",
        "At higher altitudes oaks chestnuts and rhododendrons replace dipterocarps",
        "There are an estimated 8500 species of vascular plants in Peninsular Malaysia with another 15000 in the East",
        "The forests of East Malaysia are estimated to be the habitat of around 2000 tree species and are one of the most biodiverse areas in the world with 240 different species of trees every hectare",
        "These forests host many members of the Rafflesia genus the largest flowers in the with a maximum diameter of 1 m (3 ft 3 in)",
        "Conservation issues Main article: Environmental issues in Malaysia Logging along with cultivation practices has devastated tree cover causing severe environmental degradation in the country",
        "Over 80 per cent of Sarawak's rainforest has been cleared",
        "Floods in East Malaysia have been worsened by the loss of trees and over 60 per cent of the Peninsular's forest have been cleared",
        "With current rates of deforestation mainly for the palm oil industry the forests are predicted to be extinct by 2020",
        "is a major problem for animals fungi and plants as the forest is cut to make room for plantations",
        "Most remaining forest is found inside national parks",
        "Habitat destruction has proved a threat for marine life",
        "Illegal fishing is another major with fishing methods such as dynamite fishing and poisoning depleting marine ecosystems",
        "Leatherback turtle numbers have dropped 98 per cent since the 1950s",
        "Hunting has also been an issue for some with overconsumption and the use of animal parts for profit endangering many animals from marine to tigers",
        "Marine life is also detrimentally affected by uncontrolled tourism",
        "The Malaysian government aims to balance economic growth with environmental protection but has been accused of favouring big business over the environment",
        "Some state governments are now trying to counter the environmental impact and pollution created by and the federal government is trying to cut logging by 10 per cent each year",
        "28 national parks have been established; 23 in East Malaysia and five in the Peninsular",
        "Tourism has been limited in biodiverse areas such as Sipadan island",
        "Animal trafficking is a large issue and the Malaysian government is holding talks with the governments of Brunei and Indonesia to standardise anti-trafficking laws",
        "Economy Main article: Economy of Malaysia Tree map of Malaysia's exports in 2017 The Proton company is a Malaysian car manufacturer",
        "Malaysia is a relatively open state-oriented and newly industrialised market economy",
        "The state plays a significant but declining role in guiding economic activity through macroeconomic plans",
        "Malaysia has had one of the best economic records in Asia with GDP growing an average 6",
        "5 per cent annually from 1957 to 2005",
        "Malaysia's economy in 2014–2015 was one of the most competitive in Asia ranking 6th in Asia and 20th in the world higher than countries like Australia France and South Korea",
        "In 2014 Malaysia's economy grew 6% the second highest growth in ASEAN behind the Philippines' growth of 6",
        "1%",
        "The economy of Malaysia in terms of gross domestic product (GDP) at purchasing power parity (PPP) in April 2019 was estimated to be $999",
        "397 billion the third largest in ASEAN and the 25th largest in the world",
        "In 1991 Prime Minister Mahathir Mohamad (during his first period as Prime Minister) outlined his ideal in Vision 2020 in which Malaysia would become a self-sufficient industrialised nation by 2020",
        "Najib Razak has said Malaysia could attain developed country status much earlier from the actual target in 2020 adding the country has two program concept such as Government Transformation Programme and the Economic Transformation Programme",
        "According to a HSBC report Malaysia will become the world's 21st largest economy by 2050 with a GDP of $1",
        "2 trillion (Year 2000 dollars) and a GDP per capita of $29247 (Year 2000 dollars)",
        'The report also says "The electronic equipment petroleum and liquefied natural gas producer will see a substantial increase in income per capita',
        'Malaysian life expectancy relatively high level of schooling and above average fertility rate will help in its rapid expansion"',
        'Viktor Shvets the managing director of Credit Suisse has said "Malaysia has all the right ingredients to become a developed nation"',
        "Port Klang in Selangor the biggest and busiest port in Malaysia In the 1970s the predominantly mining and agricultural-based economy began a transition towards a more multi-sector economy",
        "Since the 1980s the industrial sector with a high level of investment has led the country's growth",
        "The economy recovered from the 1997 Asian Financial Crisis earlier than neighbouring countries did and has since recovered to the levels of the pre-crisis era with a GDP per capita of $14800",
        "Economic inequalities exist between different ethnic groups",
        "The Chinese make up about one-quarter of the population but accounts for 70 per cent of the country's market capitalisation",
        "Chinese businesses in Malaysia are part of the larger bamboo network a network of overseas Chinese businesses in the Southeast Asian market sharing common family and cultural ties",
        "International trade facilitated by the shipping route in adjacent Strait of Malacca and manufacturing are the key sectors",
        "Malaysia is an exporter of natural and agricultural resources and petroleum is a major export",
        "Malaysia has once been the largest producer of rubber and palm oil in the world",
        "Manufacturing has a large influence in the country's although Malaysia's economic structure has been moving away from it",
        "Malaysia remains one of the world's largest producers of palm oil",
        "The Petronas Towers house the headquarters of the national oil company Petronas and are the tallest twin-towers in the world",
        "In an effort to diversify the economy and make it less dependent on export goods the government has pushed to increase tourism to Malaysia",
        "As a result tourism has become Malaysia's third largest source of foreign exchange although it is threatened by the negative effects of the growing industrial economy with large amounts of air and water pollution along with deforestation affecting tourism",
        "The tourism sector came under some pressure in 2014 when the national carrier Malaysia Airlines had one of its planes disappear in March while another was brought down by a missile over Ukraine in July resulting in the loss of a total 537 passengers and crew",
        "The state of the airline which had been unprofitable for 3 years prompted the government in August 2014 to nationalise the airline by buying up the 30 per cent it did not already own",
        "Between 2013 and 2014 Malaysia has been listed as one of the best places to retire to in the world with the country in third position on the Global Retirement Index",
        "This in part was the result of the Malaysia My Second Home programme to allow foreigners to live in the country on a long-stay visa for up to 10 years",
        "In 2016 Malaysia ranked the fifth position on The World's Best Retirement Havens while getting in the first place as the best place in Asia to retire",
        "Warm climate with British colonial background made foreigners easy to interact with the locals",
        "The country has developed into a centre of Islamic banking and is the country with the highest numbers of female workers in that industry",
        "Knowledge-based services are also expanding",
        "To create a self-reliant defensive ability and support national development Malaysia privatised some of its military facilities in the 1970s",
        "The privatisation has created defence industry which in 1999 was brought under the Malaysia Defence Industry Council",
        "The government continues to promote this sector and its competitiveness actively marketing the defence industry",
        "Science policies in Malaysia are regulated by the Ministry of Science Technology and Innovation",
        "The country is one of the world's largest exporters of semiconductor devices electrical devices and IT and communication products",
        "Malaysia began developing its own space programme in and in 2006 Russia agreed to transport one Malaysian to the International Space Station as part of a multibillion-dollar purchase of 18 Russian Sukhoi Su-30MKM fighter jets by the Royal Malaysian Air Force",
        "The government has invested in building satellites through the RazakSAT programme",
        "Infrastructure The overall infrastructure of Malaysia is one of the most developed in and ranked 8th in Asia and 25th in the world",
        "Malaysia is ranked 19th in the world for its quality roads quality of port infrastructure and quality of air transport infrastructure but ranked 39th in quality of electricity supply",
        "Its telecommunications network is second only to Singapore's in Southeast Asia with 4",
        "7 million fixed-line subscribers and more than 30 million cellular subscribers",
        "The country has seven international ports the major one being the Port Klang",
        "There are 200 industrial parks along with specialised parks such as Technology Park Malaysia and Kulim Hi-Tech Park",
        "Fresh water is available to over 95 per cent of the population",
        "During the colonial period development was mainly concentrated in economically powerful cities and in areas forming security concerns",
        "Although rural areas have been the focus of great development they still lag behind areas such as the West Coast of Peninsular Malaysia",
        "The telecommunication network although strong in urban areas is less available to the rural population",
        "Energy Main articles: Energy policy of Malaysia and List of power stations in Malaysia Malaysia's energy infrastructure sector is largely dominated by Tenaga Nasional the largest electric utility company in Southeast Asia with over RM99",
        "03 billion of assets",
        "Customers are connected to electricity through the National Grid with more than 420 transmission substations in the Peninsular linked together by approximately 11000 km of transmission lines operating at 66 132 275 and 500 kilovolts",
        "The other two electric utility companies in the country are Sarawak Energy and Sabah Electricity",
        "In 2013 Malaysia's total power generation capacity was over 29728 megawatts",
        "Total electricity generation was 140985",
        "01 GWh and total electricity consumption was 116087",
        "51 GWh",
        "Energy production in Malaysia is largely based on oil and natural gas owing to Malaysia's oil reserves and natural gas reserves which is the fourth largest in Asia-Pacific region",
        "Transportation Main articles: Transport in Malaysia Rail transport in Malaysia and List of airports in Malaysia",
        "Demographics Main article: Demographics of Malaysia The percentage distribution of Malaysian population by ethnic group based on 2010 census Year Million 1950 6",
        "Malaysian Chinese in Perak There are also two other non-Bumiputera local ethnic groups",
        "24",
        "6 per cent of the population are Malaysian Chinese while 7",
        "3 per cent are Malaysian Indian",
        "The local Chinese have historically been more dominant in the business community",
        "Local Indian are majority of Tamils descent",
        "Malaysian citizenship is not automatically granted to those born in Malaysia but is granted to a child born of two Malaysian parents outside Malaysia",
        "Dual citizenship is not permitted",
        "Citizenship in the states of Sabah and Sarawak in Malaysian Borneo are distinct from citizenship in Peninsular Malaysia for immigration purposes",
        "Every citizen is issued a biometric smart chip identity card known as MyKad at the age of 12 and must carry the card at all times",
        "Malaysian Indians in Selangor The education system features a non-compulsory kindergarten education followed by six years of compulsory primary education and five years of optional secondary education",
        "Schools in the primary education system are divided into two categories: national primary schools which teach in Malay and vernacular schools which teach in Chinese or Tamil",
        "Secondary education is conducted for five years",
        "In the final year of secondary education students sit for the Malaysian Certificate of Education examination",
        "Since the introduction of the matriculation programme in 1999 students who completed the 12-month programme in matriculation colleges can enroll in local universities",
        "However in the matriculation system only 10 per cent of places are open to non-bumiputera students",
        "Population density (person per km2) in 2010 The infant mortality rate in 2009 was 6 deaths per 1000 births and life expectancy at birth in 2009 was 75 years",
        "With the aim of developing Malaysia into a medical tourism destination 5 per cent of the government social sector development budget is spent on health care",
        "The number of live births in Malaysia stood at 508203 babies in the year 2016",
        "This is a decline compared to 521136 the previous year",
        "There was also a decline in crude birth rate from 16",
        "7 (2015) to 16",
        "1 (2016) per 1000 population",
        "Male babies account for 51",
        "7% of all babies born in the year 2016",
        "The highest crude birth rate was reported at Putrajaya (30",
        "4) and the lowest was reported at Penang (12",
        "7)",
        "The Julau district has the highest crude birth rate nationwide at 26",
        "9 per 1000 population meanwhile the lowest crude birth rate was recorded in the Selangau district",
        "The total fertility rate in Malaysia remains below the replacement level at 1",
        "9 babies in 2017",
        "This is a decline of 0",
        "1 compared to the previous year",
        "The highest crude death rate was reported in Perlis at 7",
    ]


@pytest.fixture
def complex_article() -> str:
    return (
        "Prime Minister head cabinet head Since 2018 general election Malaysia governed Pakatan Harapan political "
        "alliance 24 February 2020 7th Prime Tun Mahathir Mohamad resign Prime Minister starting 1 March new "
        "coalition governed Malaysia led new 8th Prime Minister Tan Sri Muhyiddin Yassin legal system based "
        "English Common Law Although judiciary theoretically independence called question appointment judges lacks "
        "accountability highest court judicial system Federal Court followed Court Appeal two high courts one "
        "Peninsular Malaysia one East Malaysia special court hear cases brought death penalty use serious crimes "
        "murder terrorism drug trafficking kidnapping Separate running parallel civil courts Syariah Courts apply "
        "Shariah law Muslims areas family law religious Homosexuality illegal authorities impose punishment caning "
        "Race significant force Affirmative actions New Economic Policy National Development Policy superseded "
        "implemented advance standing consisting Malays indigenous tribes considered original inhabitants "
        "Malaysian Chinese Malaysian policies provide preferential treatment access cheaper housing assisted "
        "generated greater interethnic ongoing debate whether laws society Malaysia reflect secular Islamic "
        "Islamic criminal laws passed Islamic Party support United Malays National Organisation state assemblymen "
        "state legislative assembly Kelantan blocked federal government basis criminal laws responsibility federal "
        "States federal territories Malaysia Divisions Malaysia Districts Malaysia Perlis Kedah Penang Kelantan "
        "Terengganu Perak Selangor Negeri Sembilan Melaka Johor Pahang Sarawak Sabah West Malaysia East Malaysia "
        "States Malaysia federation 13 states three federal divided two 11 states two federal territories "
        "Peninsular Malaysia two states one federal territory East Malaysia state divided districts divided mukim "
        "Sabah Sarawak districts grouped Governance states divided federal state different powers reserved Federal "
        "government direct administration federal state unicameral State Legislative Assembly whose members "
        "elected State governments led Chief Ministers state assembly members majority party states hereditary "
        "Chief Minister normally required Malay appointed ruler upon recommendation Prime Except state elections "
        "convention state elections held concurrently federal administration carried local include city district "
        "municipal although autonomous statutory bodies created federal state governments deal certain federal "
        "constitution puts local authorities outside federal territories exclusive jurisdictions state although "
        "practice federal government intervened affairs state local 154 local consisting 14 city 38 municipal 97 "
        "district 13 states based historical Malay 9 11 Peninsular known Malay states retain royal King elected "
        "nine rulers serve King appoints governors serving term states without consultations chief minister state "
        "written Sabah Sarawak considerably autonomy notably separate immigration policies unique residency "
        "Federal intervention state lack disputes oil royalties occasionally led statements secession leaders "
        "several states Penang Johor Kelantan Sabah although followed serious independence movements list thirteen "
        "states state capital Johor Johor Bahru Kedah Alor Setar Kelantan Kota Bharu Malacca Malacca City Negeri "
        "Sembilan Seremban Pahang Kuantan Penang George Town Perak Ipoh Perlis Kangar Sabah Kota Kinabalu Sarawak "
        "Kuching Selangor Shah Alam Terengganu Kuala Terengganu Federal Territory Kuala Lumpur Federal Territory "
        "Labuan Federal Territory Putrajaya Foreign relations Malaysia Malaysian Armed Forces Mike Pompeo "
        "Putrajaya founding member Association Southeast Asian Nations Organisation Islamic Cooperation country "
        "participates many international organisations United Nations Economic Cooperation Developing 8 Countries "
        "Movement chaired NAM former British member Commonwealth Nations Kuala Lumpur site first East Asia Summit "
        "foreign policy officially based principle neutrality maintaining peaceful relations regardless political "
        "government attaches high priority security stability Southeast seeks develop relations countries "
        "Historically government tried portray Malaysia progressive Islamic nation strengthening relations Islamic "
        "strong tenet policy national sovereignty right country control domestic Malaysia signed UN treaty "
        "Prohibition Nuclear Weapons Spratly Islands disputed many states large portion South China Sea claimed "
        "China Unlike neighbours Vietnam Philippines Malaysia historically avoided conflicts encroachment Chinese "
        "ships Malaysian territorial Malaysia become active condemning Brunei Malaysia 2009 announced end claims "
        "committed resolve issues related maritime Philippines dormant claim eastern part land reclamation caused "
        "minor maritime land border disputes exist Malaysian Armed Forces submarine MBT tank Malaysian Army M4 "
        "fighter aircraft Malaysia never recognised Israel diplomatic ties called International Criminal Court "
        "take action Israel Gaza flotilla raid Malaysia stated establish official relations Israel peace agreement "
        "State Palestine called parties find quick resolution realise solution Malaysian peacekeeping forces "
        "contributed many UN peacekeeping Congo Namibia Cambodia Bosnia Herzegovina Somalia Kosovo East Timor "
        "Lebanon Malaysian Armed Forces three Royal Malaysian Navy Malaysian Army Royal Malaysian Air Force "
        "required age voluntary military service military uses employs Five Power Defence Arrangements regional "
        "security initiative place almost 40 involves joint military exercises held among New United Joint "
        "exercises war games held Indonesia Japan United Thailand Vietnam agreed host joint security force "
        "exercises secure maritime border tackle issues illegal piracy smuggling Previously fears extremist "
        "militants activities Muslim areas southern Philippines southern Thailand would spill Malaysia began "
        "increase border Geography Malaysia equatorial region tropical rainforest climate Malaysia 66th largest "
        "country total land area land area km sq land borders Thailand West Indonesia Brunei East linked Singapore "
        "narrow causeway country maritime boundaries Vietnam land borders defined large part geological features "
        "Perlis River Golok River Pagalayan whilst maritime boundaries subject ongoing Brunei forms almost enclave "
        "state Sarawak dividing two Malaysia country territory Asian mainland Malay Tanjung Piai located southern "
        "state Johor southernmost tip continental Strait Malacca lying Sumatra Peninsular one important "
        "thoroughfares global carrying 40 per cent two parts separated South China Sea share largely similar "
        "landscape Peninsular East Malaysia feature coastal plains rising hills Peninsular containing 40 per cent "
        "land extends 740 km north maximum width 322 km divided east west coasts Titiwangsa Mountains rising peak "
        "elevation metres Mount Korbu part series mountain ranges running centre mountains heavily mainly composed "
        "granite igneous Much creating karst range origin Peninsular river coastal plains surrounding peninsula "
        "reach maximum width 50 kilometres coastline nearly km although harbours available western Mount Kinabalu "
        "East island Borneo coastline km divided coastal hills mountainous Crocker Range extends northwards "
        "dividing state location high Mount Kinabalu tallest mountain Mount Kinabalu located Kinabalu National "
        "Park protected one four UNESCO World Heritage Sites Malaysia highest mountain ranges form border Malaysia "
        "Sarawak contains Mulu largest cave system Gunung Mulu National Park World Heritage Around two halves "
        "Malaysia numerous islands largest Banggi local climate equatorial characterised annual southwest "
        "northeast monsoons temperature moderated presence surrounding Humidity usually average annual rainfall "
        "250 cm climates Peninsula East climate peninsula directly affected wind opposed maritime weather Local "
        "climates divided three Climate change likely affect sea levels increasing flood risks leading Wildlife "
        "Malaysia oriental pied hornbills hawksbill sea turtle proboscis monkey Malayan tiger Malaysia signed Rio "
        "Convention Biological Diversity 12 June became party convention 24 June subsequently produced National "
        "Biodiversity Strategy Action Plan received convention 16 April country megadiverse high number species "
        "high levels endemism estimated contain 20 per cent animal High levels endemism found diverse forests "
        "species isolated lowland 210 mammal species 620 species birds recorded Peninsular many endemic mountains "
        "high number endemic bird species found Malaysian 250 reptile species recorded 150 species snakes 80 "
        "species 150 species thousands insect Exclusive economic zone Malaysia km sq times larger land mainly "
        "South China Sea waters Coral Triangle biodiversity waters around Sipadan island biodiverse Bordering East "
        "Sulu Sea biodiversity around 600 coral species 1200 fish unique biodiversity Malaysian Caves always "
        "attracts lovers ecotourism Nearly species including species recorded two fungal groups largest number "
        "species Ascomycota asexual states surveyed habitats marine freshwater parasites agents poorly surveyed "
        "habitats human animal Basidiomycota partly bracket fungi mushrooms toadstools Malaysian rust smut fungi "
        "remain poorly Without many fungal species Malaysia yet likely many new Rafflesia two thirds Malaysia "
        "covered forest forests believed 130 million years forests dominated dipterocarps Lowland forest covers "
        "areas 760 formerly East Malaysia covered rainforest supported hot wet around species flowering plants "
        "Besides km sq mangroves large amount peat higher rhododendrons replace estimated species vascular plants "
    )
