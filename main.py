from src.tools.tools import web_search, scrape_url

# output = web_search("Latest news on AI research")
# print(output)

# results = scrape_url("https://ai.google/research")
# print(results)

p = web_search.invoke("Latest news on AI research")
print(p)
# scrape_url.invoke("https://ai.google/research")