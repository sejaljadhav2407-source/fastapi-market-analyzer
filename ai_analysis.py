from google import genai

client = genai.Client(api_key="AIzaSyC8AKNJHIST5JyNA-abwdz13D869m1yffE")

def analyze_market(sector, market_data):

    prompt = f"""
    Analyze the {sector} sector in India.

    Market Data:
    {market_data}

    Provide trends and opportunities.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    try:
        return response.candidates[0].content.parts[0].text
    except:
        return "Analysis could not be generated."