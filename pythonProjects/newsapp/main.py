import requests

query = input("Enter the keyword to search: ")
api = "8639741029dd4063b6e9edd19174d30b"
url =f"https://newsapi.org/v2/everything?q={query}&from=2025-04-10&sortBy=publishedAt&apiKey={api}"

print(url)

content = requests.get(url)
data = content.json()
articles = data['articles']
for index,article in enumerate(articles):
    print(index+1,article['title'],article['url'])
    print("\n***********************************")
