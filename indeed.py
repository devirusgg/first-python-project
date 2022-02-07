import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=java&limit={LIMIT}"

def extract_indeed_pages():
    #requests로 url을 읽어옴
    result = requests.get(URL)

    #읽어온 url텍스트중 html만 찾음
    soup = BeautifulSoup(result.text, "html.parser") 

    #html만 찾은 정보에서 div만 찾음
    pagination = soup.find("div", {"class":"pagination"})

    #모든 a태그를 찾음
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results =soup.find_all("td", {"class": "resultContent"})
        #print(results)

    for result in results:
        title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).string
        company = result.find("span", {"class": "companyName"}).string
        print( "title: "+ title +"\n" + "company: " + company +"\n\n" )

    return jobs

    #깃허브 테스트 주석
    #깃허브 테스트 주석 2