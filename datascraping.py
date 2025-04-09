from bs4 import BeautifulSoup
import requests
import pandas as pd




url="https://www.allrecipes.com/recipes/17057/everyday-cooking/more-meal-ideas/5-ingredients/main-dishes/"




head=( {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

webpage=requests.get(url,headers=head)


soup=BeautifulSoup(webpage.content,'html.parser')




listitems=soup.find('section',attrs={'class':"comp taxonomysc mntl-taxonomysc"}).find_all('a')
linkslist=[]
for listitems in listitems:
    href=listitems.get("href")
    linkslist.append(href)

link_list=linkslist[19:]

print(link_list)


def get_title(soup_other):
    recipeTitle = soup_other.find("h1", attrs = {"class" : 'article-heading text-headline-400'}).text.strip()
    return recipeTitle


def get_time(soup_other):

    recipeTme =soup_other.find("div", attrs = {"class" : 'mm-recipes-details__content'}).text.strip()
    return recipeTme
def get_ingredients(soup_other):

    recipeIng = soup_other.find("ul", attrs = {"class" : 'mm-recipes-structured-ingredients__list'}).text.strip()
    return recipeIng


d={"title":[],"prep time":[],"ingredients":[],"methord of prepration":[]}
for link in link_list:

    other_webpage=requests.get(link,headers=head)

    soup_other=BeautifulSoup(other_webpage.content,'html.parser')

    d["title"].append(get_title(soup_other))
    d["prep time"].append(get_time(soup_other))
    d["ingredients"].append(get_ingredients(soup_other))





df=pd.DataFrame.from_dict(d)

print(df)

