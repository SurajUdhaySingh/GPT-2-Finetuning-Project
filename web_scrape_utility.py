import requests
from bs4 import BeautifulSoup

def extract_text_from_wiki(title):
    try:
        # Replace spaces with underscores for proper Wikipedia URL format
        url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
        response = requests.get(url)
        response.raise_for_status()  # Checks for HTTP errors
        
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find("div", {"id": "mw-content-text"})
        
        if not content:
            raise ValueError("Could not find the main content on the page.")
            
        text = ""
        for paragraph in content.find_all("p"):
            text += paragraph.get_text() + "\n"
            
        # Create and write to the file
        filename = f"{title}.txt"
        with open(filename, "w", encoding="utf-8") as txt:
            txt.write(text)
            
        print(f"Wikipedia article was extracted from '{title}' and saved to '{filename}'")
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
