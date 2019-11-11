from bs4 import BeautifulSoup as soup
import urllib.request as uReq

def searchUrlGenerator():
    print("Input the 9gag url: or input nothing to go to default:")
    page_url=input()
    if page_url.__contains__("https://9gag.com/"):
        return page_url
    return "https://9gag.com/"
def userAgentGenerator():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    header={'User-Agent':user_agent,}
    return header
def userAgentAndOtherDetaisGenerator():
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Referer': 'https://cssspritegenerator.com',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    return hdr


headers=userAgentAndOtherDetaisGenerator()
page_url=searchUrlGenerator()
request = uReq.Request(page_url,None,headers)
uClient = uReq.urlopen(request)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
print(page_url)
print(page_soup)
containers = page_soup.findAll("div", {"class": "list-stream"})
print(containers.__len__())
#out_filename = "movie_review.csv"
# header of csv file to be written
#headers = "review no,reviews \n"
# opens file, and writes headers
#f = open(out_filename, "w")
#f.write(headers)
review=[]
for container in containers:
    review.append(container.find("div",{"class":"text show-more__control"}))
for rev in review:
    rev_index=review.index(rev)
    if rev_index==None:
        continue
    rev_text=rev.text.replace(","," .. ")
    #if(rev_text.isascii()):
        #f.write(str(rev_index+1)+","+rev_text+"\n")
#f.close()
'''
   ___   ____    _    ____
  / _ \ / ___|  / \  / ___|
 | (_) | |  _  / _ \| |  _
  \__, | |_| |/ ___ \ |_| |
    /_/ \____/_/   \_\____|

'''