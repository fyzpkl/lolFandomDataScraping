import requests
from bs4 import BeautifulSoup

player_names = ['Agurin','Tolkin']

for player_name in player_names:
    # Construct the URL for the player's page
    player_url = f"https://lol.fandom.com/wiki/{player_name}"

    # Send an HTTP request to the webpage
    response = requests.get(player_url)

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the nationality picture element
    info_socialmedia = soup.find_all("table", {"class": "blockbox"})
    # iterating through all the links
    info_role = soup.find("span", {"class": "sprite role-sprite"})
    if info_role:
        role = info_role['title']
        print(role)
    else:
        print("Role not found")
    info_team_name = soup.find("span", {"class": "teamname"})
    for element in info_team_name:
        if info_team_name:
            team_name = info_team_name.text.strip()
            print(team_name)
        else:
            print("Team name not found")

    for each in info_socialmedia:
        # Find the anchor tags within the table element
        anchors = each.find_all("a")
        # Iterate through the anchor tags
        for anchor in anchors:
            href = anchor.get('href')
            print(href)


    



