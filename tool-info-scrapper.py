import requests
from bs4 import BeautifulSoup

# Amazon URL
max_page = 7
url = f"https://www.amazon.com/s?k=tools&crid=X89T1N59CQZE&sprefix=tools%2Caps%2C651&ref=nb_sb_noss_1"

output_file_path = "./tool-name-list.txt"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Clear old file
with open(output_file_path, "w"):
    pass

for page in range(1, max_page + 1):
    
    response = requests.get(f"{url}&page={page}", headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract tool names (from product titles)
        tool_info_list = []
        
        for tool_section in soup.find_all("div", class_="a-section a-spacing-base"):
            title = tool_section.find("span", class_="a-size-base-plus a-color-base a-text-normal")
            image = tool_section.find("div", class_="a-section aok-relative s-image-square-aspect")
            
            if image and title:
                title_textx=title.get_text()
                image_url=image.find("img", class_="s-image").get("src")
    
                tool_info_list.append((title_textx, image_url))

        # Print extracted names
        print(f"Extracted Tool Info On Page {page}")

        with open(output_file_path, "a", encoding="utf-8") as file:
            for idx, tool_info in enumerate(tool_info_list, start=1):
                file.write(f"{tool_info[0]};{tool_info[1]}\n")

    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
