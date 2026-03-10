from fastapi import FastAPI
from google import genai

app = FastAPI()

client = genai.Client(api_key="AIzaSyC8AKNJHIST5JyNA-abwdz13D869m1yffE")

@app.get("/")
def home():
    return {"message": "AI Market Analyzer API running"}

@app.get("/analyze/{sector}")
def analyze_market(sector: str):

    prompt = f"Analyze {sector} sector in India and give trends and opportunities."

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        result = response.candidates[0].content.parts[0].text

        return {
            "sector": sector,
            "analysis": result
        }

    except Exception as e:
        return {
            "error": "Gemini API quota exceeded. Try again later."
        }