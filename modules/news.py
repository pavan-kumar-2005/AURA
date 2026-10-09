import requests
API_KEY="d8b4c5ae29fc4f338cbad4e4f98478c4"
BASE_URL="https://newsapi.org/v2/top-headlines"

def get_news():
    params={
        "country":"us",
        "apiKey":API_KEY
    }
    response=requests.get(BASE_URL,params=params)
    # print(response.status_code)
    # print(response.json())
    if response.status_code==200:
        data=response.json()
        # article=data["articles"][0]["title"]
        headlines=[]
        for article in data["articles"][0:3]:
            title=article.get("title")
            headlines.append(f"Headline{len(headlines)+1}: {title}")
        whole_news="\n".join(headlines)
        return whole_news
    else:
        return "Sorry, I couldn't get the latest news.Please check  your internet connection and try again."

