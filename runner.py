from agent import InterviewAgent

def main():
    api_key = "your-openai-api-key"
    audio_path = "interview_audio.mp3"

    with open("job_description.txt", "r") as f:
        job_desc = f.read()

    agent = InterviewAgent(api_key, job_desc)

    print("🔍 Transcribing audio...")
    transcript = agent.transcribe_audio(audio_path)

    print("\n📝 Summary:")
    print(agent.summarize_transcript(transcript))

    print("\n📌 Matched Keywords:")
    print(agent.match_keywords(transcript))

    print("\n📊 Sentiment Analysis:")
    print(agent.evaluate_sentiment(transcript))

if __name__ == "__main__":
    main()
