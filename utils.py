import openai

def extract_keywords(text):
    prompt = f"Extract key skills and concepts from this job description:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    keywords = response["choices"][0]["message"]["content"]
    return [kw.strip() for kw in keywords.split(",")]

def analyze_sentiment(text):
    prompt = f"Analyze the sentiment of this interview transcript:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
