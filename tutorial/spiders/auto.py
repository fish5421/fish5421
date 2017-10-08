from bs4 import BeautifulSoup
import scrapy


number_of_pages = 1
int_page = 1
url_list = []
vins = []
int_matches = 0
#user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
while int_page <= number_of_pages:
        # url with search results
        url = "https://www.cars.com/for-sale/searchresults.action/?bsId=20203&bsId=20206&bsId=20211&bsId=20217&bsId=20216&kw=cruise%20control&mlgId=28859&page=" + str(int_page) + "&perPage=100&prMx=30000&rd=40&searchSource=GN_REFINEMENT&sort=price-lowest&stkTypId=28881&yrId=58487&yrId=56007&yrId=51683&yrId=47272&zc=48073"

        int_page += 1
        url_list.append(url)
       


class QuotesSpider(scrapy.Spider):
    name = "auto"
    start_urls = url_list
    #print(start_urls)

    # def check_advert(arg_url):
    #     global int_matches
    #     baseurl = "http://www.cars.com"
    #     mainurl = baseurl + arg_url
    #     print(mainurl)
    #     time.sleep(random.randint(1, 5))
    
    #     try: 
    #         r = requests.get(mainurl, data=None, headers={'User-Agent': user_agent})
    #         print("Passed")
    #     except requests.exceptions.ConnectionError:
    #         print("Failed")
    #         r.status_code = "Connection refused"

 
    #     soup = BeautifulSoup(r.content, 'lxml')
    #     heds = soup.find_all('div', class_ = "facet__details", limit = 5)
    #     links = []
    #     for h in heds:
    #         a = h.find('strong').next_sibling
    #         links.append(a)
    #     #b = a.find(string="VIN:")
    #     #print(b)
    #   #  if b is not None:
    #    #     c = b.get_text()
    #     #    print(b)
    #      #   links.append(a)
        
    # #print(links)
    #     x = len(links)
    #     if x > 0:
    # #print(x)
    #         y = links[4]
    # #hello = [z.strip(' ') for z in hello]
    #         z = str(y)
    #         xyz = z.replace(" ", "")
    #     #print(xyz)
    #         vins.append(xyz)

    
    

    def parse(self, response):
        divs = response.xpath('//div')
        divs.xpath('//div[re:test(@class, "listing-row__image")]//@href').extract()
        urls_auto = divs.xpath('//div[re:test(@class,"listing-row__image")]//@href').extract()
        print(urls_auto)
        #for ad_link in urls_auto:
        # check each advert for a white car with panoramic roof and red leather seats
        # for each ad link, check to see if it matches
            #check_advert(ad_link)
        #print(urls_auto)
        thefile = open('test.txt', 'w')
        for item in urls_auto:
            thefile.write("%s\n" % item)




    

       