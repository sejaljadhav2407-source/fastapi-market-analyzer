import requests

def get_market_news(sector):

    query = f"{sector} sector India market news"

    try:
        response = requests.get("https://duckduckgo.com/?q=" + query)

        return f"Latest news collected about {sector} sector in India market."

    except:
        return "Market data not available"