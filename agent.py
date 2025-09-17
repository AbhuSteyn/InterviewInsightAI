import openai
from utils import extract_keywords, analyze_sentiment

class InterviewAgent:
    def __init__(self, api_key, job_description):
        openai.api_key = api_key
        self.job_keywords = extract_keywords(job_description)

    def transcribe_audio(self, audio_path):
        with open(audio_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        return response["text"]

    def summarize_transcript(self, transcript):
        prompt = f"Summarize this interview transcript:\n{transcript}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

    def match_keywords(self, transcript):
        matched = [kw for kw in self.job_keywords if kw.lower() in transcript.lower()]
        return matched

    def evaluate_sentiment(self, transcript):
        return analyze_sentiment(transcript)
