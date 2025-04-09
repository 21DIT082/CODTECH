from bs4 import BeautifulSoup
import requests

def get_movie_details(movie_name):
    # Base IMDb search URL
    search_url = f"https://www.imdb.com/find/?q={'+'.join(movie_name.split())}&s=tt&ttype=ft"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first movie result
    result = soup.find('li', class_='ipc-metadata-list-summary-item')
    if not result:
        return None
    
    movie_link = "https://www.imdb.com" + result.a['href'].split('?')[0]
    movie_name = result.a.text.strip()
    
    # Get movie details page
    response = requests.get(movie_link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract details
    movie_details = {'name': movie_name, 'url': movie_link}
    
    try:
        movie_details['year'] = soup.find('span', {'class': 'sc-8c396aa2-2 itZqyK'}).text.strip()
    except AttributeError:
        movie_details['year'] = 'Not available'
    
    try:
        movie_details['rating'] = soup.find('span', {'data-testid': 'hero-rating-bar__aggregate-rating__score'}).text.strip()
    except AttributeError:
        movie_details['rating'] = 'Not yet rated'
    
    try:
        movie_details['genres'] = [g.text for g in soup.find_all('a', {'class': 'ipc-chip ipc-chip--on-baseAlt'})]
    except AttributeError:
        movie_details['genres'] = 'Not available'
    
    try:
        movie_details['summary'] = soup.find('span', {'data-testid': 'plot-xl'}).text.strip()
    except AttributeError:
        movie_details['summary'] = 'Not available'
    
    try:
        director_section = soup.find('li', {'data-testid': 'title-pc-principal-credit'}).find('a')
        movie_details['director'] = director_section.text.strip() if director_section else 'Not available'
    except AttributeError:
        movie_details['director'] = 'Not available'
    
    return movie_details

if __name__ == "__main__":
    movie_name = input("Enter the movie name: ")
    details = get_movie_details(movie_name)
    
    if not details:
        print("No movie found!")
    else:
        print(f"\n{details['name']}\n")
        print(f"\tGenres: {', '.join(details['genres'])}\n")
        print(f"\tDirector: {details['director']}\n")
        print(f"Summary: {details['summary']}\n")
        print(f"\tMore info: {details['url']}")