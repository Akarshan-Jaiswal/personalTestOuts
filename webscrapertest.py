from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
#print("Input URL of the IMDB review page of movie:")
#page_url=input()
page_url = "https://www.imdb.com/title/tt0816692/reviews?ref_=tt_urv"
uClient = uReq(page_url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
print(page_url)
containers = page_soup.findAll("div", {"class": "content"})
print(containers.__len__())
out_filename = "movie_review.csv"
# header of csv file to be written
headers = "review no,reviews \n"
# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)
review=[]
for container in containers:
    review.append(container.find("div",{"class":"text show-more__control"}))
for rev in review:
    rev_index=review.index(rev)
    if rev_index==None:
        continue
    rev_text=rev.text.replace(","," .. ")
    if(rev_text.isascii()):
        f.write(str(rev_index+1)+","+rev_text+"\n")
f.close()