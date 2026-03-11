import requests
import bs4

url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
# print(response.text)

# headers = {
#     'Content-Type' : 'application/json'
# }

# data = {
#     'name': 'Qasim',
#     'age': 24,
#     'height': 174
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)

url = 'https://whoisfreaks.com'
r = requests.get(url)

soup = bs4.BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

for heading in soup.find_all('h1'):
    print(heading.text)


# run with 
# python /home/leo/RESOURCES/Python/requests/script.py