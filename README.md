# 🎙️ InterviewInsightAI

An agentic AI system that analyzes interview recordings and maps them to job descriptions using OpenAI APIs.

## 🚀 Overview

InterviewInsightAI is designed to help recruiters and hiring managers quickly assess candidate interviews by:
- Transcribing audio files using OpenAI Whisper
- Summarizing the interview content
- Matching key skills and concepts with a provided job description
- Analyzing the sentiment of the candidate’s responses

## 🧠 Features

- 🎧 Audio transcription via Whisper
- 📝 Summary generation using GPT
- 📌 Keyword matching with job description
- 📊 Sentiment analysis of candidate tone and confidence

## 📦 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/InterviewInsightAI.git
   cd InterviewInsightAI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key:
   - Set it as an environment variable: `export OPENAI_API_KEY=your-key`
   - Or replace `"your-openai-api-key"` in `runner.py`

4. Add your files:
   - Interview audio: `interview_audio.mp3`
   - Job description: `job_description.txt`

5. Run the agent:
   ```bash
   python runner.py
   ```

## 📥 Sample Input

### 🎧 Interview Audio
A recorded interview session with a candidate discussing their experience in software development, cloud infrastructure, and team leadership. (File: `interview_audio.mp3`)

### 📄 Job Description
```text
We are seeking a Senior DevOps Engineer with expertise in Kubernetes, CI/CD pipelines, cloud architecture (AWS/GCP), and infrastructure as code (Terraform). Strong communication and leadership skills are essential.
```

## 📤 Sample Output

### 📝 Transcript (excerpt)
> "I've led multiple DevOps initiatives, including migrating legacy systems to Kubernetes clusters on AWS. I also designed CI/CD pipelines using GitHub Actions and Terraform for infrastructure provisioning..."

### 📌 Matched Keywords
```
['Kubernetes', 'CI/CD', 'AWS', 'Terraform', 'leadership']
```

### 📊 Sentiment Analysis
> The candidate expresses confidence and enthusiasm. Tone is positive, with emphasis on leadership and technical ownership.

### 🧠 Summary
> The candidate demonstrates strong alignment with the job description, particularly in Kubernetes deployment, CI/CD automation, and cloud infrastructure. Their leadership experience and communication skills are evident throughout the interview.

## 🛠️ File Structure

```
InterviewInsightAI/
│
├── agent.py               # Core agent logic and tools
├── runner.py              # Orchestrates the workflow
├── utils.py               # Helper functions (e.g., keyword extraction)
├── job_description.txt    # Sample job description
├── interview_audio.mp3    # Sample interview audio
├── requirements.txt       # Dependencies
└── README.md              # Project overview and setup
```

## 💡 Future Enhancements

- Add Streamlit UI for interactive analysis
- Support multiple interview files
- Visualize keyword matches and sentiment trends

---

Feel free to fork, contribute, or reach out with ideas!
```

---

Let me know if you'd like help writing a GitHub project description, adding badges, or turning this into a portfolio-ready app. This project has serious showcase potential!
