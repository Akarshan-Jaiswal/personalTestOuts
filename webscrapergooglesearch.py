'''https://www.google.com/search?q='''
from bs4 import BeautifulSoup as soup
import urllib.request as uReq

def searchUrlGenerator():
    print("Input the search string:")
    page_url=input()
    page_url=page_url.replace("+","%2B").strip().replace(" ","+")
    while(page_url.__contains__("++")):
        page_url=page_url.replace("++","+")
    page_url="https://www.google.com/search?q="+page_url
    return page_url
def userAgentGenerator():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    header={'User-Agent':user_agent,}
    return header
def userAgentAndOtherDetaisGenerator():
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Referer': 'https://cssspritegenerator.com',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    return hdr


headers=userAgentAndOtherDetaisGenerator()
page_url=searchUrlGenerator()
request = uReq.Request(page_url,None,headers)
uClient = uReq.urlopen(request)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
print("Opening",page_url)
error_check_No_Item= page_soup.find("p", {"style": "contenpadding-top:.33emt"})
if (error_check_No_Item=="No results containing all your search terms were found."):
    print("No results containing all your search terms were found. Please enter valid search string")
#print(containers.__len__())
print(page_soup)
out_filename = "google_search_result.txt"
f = open(out_filename, "w")
f.write(str(page_soup))
f.close()