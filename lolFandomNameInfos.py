import requests
from bs4 import BeautifulSoup

names_list=['Agurin']

for name in names_list:
    url = f"https://lol.fandom.com/wiki/{name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Extract the name
    all_info = soup.find("table",{"id":"infoboxPlayer"})
    soloqueue_ids = "N/A"
    if all_info:
        rows = all_info.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 2:
                label = cells[0].text
                data = cells[1].text
                if label == "Country of Birth":
                    country_of_birth = data
                elif label == "Nationality":
                    nationality = data
                elif label == "Birthday":
                    birthday = data
                elif label == "Team":
                    team = data
                elif label == "Role":
                    role = data
                elif label == "Soloqueue IDs":
                    soloqueue_ids = data
                elif label == "Name":
                    player_name=data

        social_media_links = soup.find("table", {"class": "blockbox"})
        if social_media_links:
            social_media = []
            for link in social_media_links.find_all("span"):
                print(link.find("title"))
                print(link)
            print(f'Social Media: {social_media}')
        else:
            print("No social media links found.")
        print(
            f'Player Name: {player_name}\nCountry of Birth: {country_of_birth}\nNationality: {nationality}\nBirthday: {birthday}\nTeam: {team}\nRole: {role}\nSoloqueue Ids: {soloqueue_ids}\nSocial Media: {"a"}\n')
    else:
        print("No infoboxPlayer found.")