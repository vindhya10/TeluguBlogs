import requests
from bs4 import BeautifulSoup
import csv
import re

def clean_text(text):
    # Remove English words
    text = re.sub(r'\b[a-zA-Z]+\b', '', text)
    # Remove extra punctuation and symbols
    text = re.sub(r'[^\w\s\u0C00-\u0C7F]', ' ', text)  # Retain Telugu characters and basic word separators
    # Remove multiple spaces and clean up
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def scrape_blogspot(blog_url, output_csv):
    try:
        # Make a GET request to fetch the raw HTML content
        response = requests.get(blog_url)
        response.encoding = 'utf-8'  # Ensure proper encoding to handle Telugu

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title and clean it
        title = soup.title.string if soup.title else 'No Title'
        title = clean_text(title)

        # Extract the main content (adjust the tag based on the actual blog structure)
        content = ''
        post_body = soup.find('div', class_='post-body')
        if post_body:
            content = post_body.get_text(separator=' ', strip=True)

        # Clean the content
        content = clean_text(content)

        # Write data to CSV
        with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([title, content])  # Writing the title and content

        print(f"Successfully scraped {blog_url}")

    except Exception as e:
        print(f"Error while scraping {blog_url}: {e}")

# List of blog URLs
blog_urls = ["http://telugupadyam.blogspot.com/", "http://kotthachiguru.blogspot.com/", "http://dprathap.blogspot.com/", "http://amritaveena.wordpress.com/", "http://vadaami.blogspot.com/", "http://ramakasharma.blogspot.com/", "http://prasadgummadi.blogspot.com/", "http://cckrao2000.blogspot.com/", "http://battibandh.wordpress.com/", "http://padma-theinvincible.blogspot.com/", "http://joruga-husharuga.blogspot.com/", "http://nsaicharan.blogspot.com/", "http://drrams.wordpress.com/", "http://ubusu.blogspot.com/", "http://janamnaadi.blogspot.com/", "http://paraani.blogspot.com/", "http://ravindranadhg.blogspot.com/", "http://oosulu.blogspot.com/", "http://ourspiro.blogspot.com/", "http://rajivputtagunta.blogspot.com/", "http://ramasanthi.blogspot.com/", "http://gopalkoduri.wordpress.com/", "http://indianteluguassociation.blogspot.com/", "http://teluguerrors.blogspot.com/", "http://telugu-bhaktiganga.blogspot.com/", "http://oohalanni-oosulai.blogspot.com/", "http://yogihistory.blogspot.com/", "http://shankharavam.blogspot.com/", "http://poddu.net/", "http://farmeristheking.blogspot.com/", "http://aksharaarchana.blogspot.com/", "http://kalpanarentala.wordpress.com/", "http://chaduvu.wordpress.com/", "http://psravikiran.blogspot.com/", "http://sameekshaclub.wordpress.com/", "http://navatarangam.com/", "http://kesland.blogspot.com/", "http://tiyyanitenugu.wordpress.com/", "http://jeevanasutraalu.blogspot.com/", "http://nishigandha-poetry.blogspot.com/", "http://funcounterbyphani.blogspot.com/", "http://telugulomeemunduku.blogspot.com/", "http://puranalu.blogspot.com/", "http://drpvsnp.blogspot.com/", "http://raj-wanderingthoughts.blogspot.com/", "http://satya-writes.blogspot.com/", "http://www.janani.net.in/news/", "http://saiabhay2000.blogspot.com/", "http://spoorti7.blogspot.com/", "http://sathyagraahi.blogspot.com/", "http://dinnipati.wordpress.com/", "http://manimanasa.blogspot.com/", "http://teepigurutulu.blogspot.com/", "http://nava-vasantham.blogspot.com/", "http://ram-kv.blogspot.com/", "http://ushamuraliyam.blogspot.com/", "http://puretelugu.blogspot.com/", "http://ap2us.blogspot.com/", "http://happyday4every1.blogspot.com/", "http://telugubudugu.blogspot.com/", "http://chaitanyapaturu.blogspot.com/", "http://teluguvadini.blogspot.com/", "http://teluguwebchannel.blogspot.com/", "http://madhuvu.blogspot.com/", "http://naakathalu.blogspot.com/", "http://sridharchandupatla.blogspot.com/", "http://palaka-balapam.blogspot.com/", "http://telugutetalu.blogspot.com/", "http://for-what-iam-here.blogspot.com/", "http://veeresham.blogspot.com/", "http://nikosam.blogspot.com/", "http://ekantham.blogspot.com/", "http://telugu-cartoons.blogspot.com/", "http://iditelusa.blogspot.com/", "http://www.pranahita.org/", "http://suridu.blogspot.com/", "http://blaagu.com/chitralekha", "http://teluguman.blog.com/", "http://theuntoldhistory.blogspot.com/", "http://mavuduruvenugopal.blogspot.com/", "http://shashitarangam.blogspot.com/", "http://jarasodhichepparadhe.blogspot.com/", "http://scienceintelugu.blogspot.com/", "http://antulenialochanalu.wordpress.com/", "http://daadu91204.blogspot.com/", "http://punnami.blogspot.com/", "http://yamajala.blogspot.com/", "http://ulipikatte.blogspot.com/", "http://rangulakala.blogspot.com/", "http://gsashok.wordpress.com/", "http://indianshiva.blogspot.com/", "http://loguttu.blogspot.com/", "http://teluguwritings.blogspot.com/", "http://kondaveetisatyavati.wordpress.com/", "http://viraamam.blogspot.com/", "http://ashala-harivillu.blogspot.com/", "http://prasanthi.wordpress.com/", "http://kasturimuralikrishna.wordpress.com/", "http://kadapapvm.blogspot.com/", "http://raajakeeyam.blogspot.com/", "http://manogatam.blogspot.com/", "http://naa-gola.blogspot.com/", "http://computer-mobile.blogspot.com/", "http://avakaigongura.blogspot.com/", "http://telugublog.techiesteps.com/", "http://kollurisomasankar.blogspot.com/", "http://abtmmiddleschoole.blogspot.com/", "http://sastry-satakam.blogspot.com/", "http://ramurasa.blogspot.com/", "http://venugaanam.blogspot.com/", "http://naveenblogworld.blogspot.com/", "http://praveentelugu.blogspot.com/", "http://lifeasaprism.blogspot.com/", "http://chandamaama.blogspot.com/", "http://siva4u1980.blogspot.com/", "http://telugaksharam.blogspot.com/", "http://apelectricitysamasyalu.wordpress.com/", "http://naajnapakaalu.blogspot.com/", "http://jyothiv.blogspot.com/", "http://manchicoffeelanti-blog.blogspot.com/", "http://janaj4u.blogspot.com/", "http://jaatara.blogspot.com/", "http://venky-mythoughts.blogspot.com/", "http://manogna-ssv.blogspot.com/", "http://vookadampudu.wordpress.com/", "http://swatichinuku.blogspot.com/", "http://kadhalu-kaburlu.blogspot.com/", "http://harisheece.blogspot.com/", "http://vihaaram.blogspot.com/", "http://vasundhararam.wordpress.com/", "http://padanisalu.blogspot.com/", "http://alalapaikalatiga.blogspot.com/", "http://arunagjintelugu.blogspot.com/", "http://solarflare-naa-prapancham.blogspot.com/", "http://viseshaalu.blogspot.com/", "http://venkateshuoh.blogspot.com/", "http://poornachander.wordpress.com/", "http://fingersthatpointedme.blogspot.com/", "http://sraavanam.wordpress.com/", "http://yourslavanya.blogspot.com/", "http://nuvvusetty.wordpress.com/", "http://mahi-rachanalu.blogspot.com/", "http://manalomanamaata.blogspot.com/", "http://abhagyanagaram.blogspot.com/", "http://abouttelugumedia.blogspot.com/", "http://hydbachelors.wordpress.com/", "http://abhinayani.blogspot.com/", "http://maramaraalu.blogspot.com/", "http://blaagadistaa.blogspot.com/", "http://trajarao.wordpress.com/", "http://computerera.co.in/blog", "http://kadhalu.blogspot.com/", "http://bommalaata.blogspot.com/", "http://nalonenu.blogspot.com/", "http://lalithya.blogspot.com/", "http://naagodava.blogspot.com/", "http://diviseema.blogspot.com/", "http://npulipati.blogspot.com/", "http://blaagu.com/naidubaava", "http://himabindugodavarthy.wordpress.com/", "http://blog.vikatakavi.net/", "http://blogaagni.blogspot.com/", "http://netijen.blogspot.com/", "http://vaagdevi.wordpress.com/", "http://hrudayamjali.blogspot.com/", "http://rpalakurthy.wordpress.com/", "http://raagaalap.blogspot.com/", "http://prajakala.org/mag", "http://poraatam.blogspot.com/", "http://paradarsi.wordpress.com/", "http://padamatisandhya.blogspot.com/", "http://onlinejunk.blogspot.com/", "http://swagathalu.blogspot.com/", "http://venkatasivaprasadpulla.blogspot.com/", "http://gannarapu.wordpress.com/", "http://kaizen123.blogspot.com/", "http://sharath-myblog.blogspot.com/", "http://rohiniprasadk.blogspot.com/", "http://liscience.blogspot.com/", "http://kareemullah.blogspot.com/", "http://poorniman.blogspot.com/", "http://seshus.blogspot.com/", "http://lingathegreat.blogspot.com/", "http://vamshi-krishna.blogspot.com/", "http://bulsvas.blogspot.com/", "http://kavitalu.blogspot.com/", "http://swathikumari.wordpress.com/", "http://vjyothi.blogspot.com/", "http://jyothivalaboju.blogspot.com/", "http://japes.wordpress.com/", "http://teluguavakai.blogspot.com/", "http://kaalidasu.wordpress.com/", "http://wowmusings.blogspot.com/", "http://kitchenindia.blogspot.com/", "http://sukasi.blogspot.com/", "http://hrudayatarangalu.blogspot.com/", "http://gemsofhindupur.blogspot.com/", "http://ntr-everything.blogspot.com/", "http://edocheppalani.blogspot.com/", "http://pillitala.blogspot.com/", "http://myrebelxt.blogspot.com/", "http://desimultiplex.blogspot.com/", "http://xtracinema.blogspot.com/", "http://chitrollaasa.blogspot.com/", "http://www.chanduonline.com/", "http://vinodkumar-bommalata.blogspot.com/", "http://teluguveera-levara.blogspot.com/", "http://brundaavani.blogspot.com/", "http://harivillu.blogspot.com/", "http://nparupalli.blogspot.com/", "http://vasamtam.blogspot.com/", "http://smruthulu.blogspot.com/", "http://praveenspen.blogspot.com/", "http://snehama.blogspot.com/", "http://localizing.blogspot.com/", "http://kp-sundarakanda.blogspot.com/", "http://sitraalu.blogspot.com/", "http://vidyanath.blogspot.com/", "http://salabanjhikalu.blogspot.com/", "http://saakshi.blogspot.com/", "http://vareesh.blogspot.com/", "http://satyasodhana.blogspot.com/", "http://sambhavami.blogspot.com/", "http://sangrahaalayam.blogspot.com/", "http://sreekaaram.wordpress.com/"]

# Output file where data will be saved
output_csv = 'scraped_blogs_teluguv.csv'

# Write headers to CSV file
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Content'])

# Scrape each blog and save the results
for blog_url in blog_urls:
    scrape_blogspot(blog_url, output_csv)
