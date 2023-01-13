import requests
from bs4 import BeautifulSoup
import pandas as pd
regions= ['North_American_Teams','EMEA_Teams', 'Korean_Teams','Chinese_Teams', 'Brazilian_Teams','Japanese_Teams', 'Latin_America   n_Teams', 'Oceanic_Teams', 'PCS_Teams','Vietnamese_Teams']


with pd.ExcelWriter("teams.xlsx") as writer:
    for region in regions:
        url = f"https://lol.fandom.com/wiki/{region}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"class": "wikitable"})
        rows = table.find_all("tr")
        team_list = []
        for row in rows:
            cells = row.find_all("td")
            if cells and len(cells)>=3:
                team_name = cells[0].text
                social_media_links = cells[1].find_all("a")
                social_media = [link["href"] for link in social_media_links]
                names = cells[2].find_all("a")
                names_list = [name.text for name in names]
                print(f'Team Name: {team_name}\nSocial Media: {social_media}\nNames: {names_list}\n')

                team_list.append([team_name, social_media, names_list])
        df = pd.DataFrame(team_list, columns = ['Team Name', 'Social Media', 'Roster'])
        df.to_excel(writer, sheet_name=region,index = False)

"""
 roster = cells[3].text
        titles = cells[3].find_all("b")
        titles_list = [title.text for title in titles]
        names = cells[3].find_all("a")
        names_list = [name.text for name in names]
        print(f'Team Name: {team_name}\nSocial Media: {social_media}\nRoster: {titles_list}\nNames: {names_list}\n')
"""
