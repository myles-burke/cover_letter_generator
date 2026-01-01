import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("TOKEN"), base_url="https://openrouter.ai/api/v1")

def sendMessage(resume, job):
    prompt_text = (
        f"You are a professional career assistant."
        f"Resume: {resume} Job Description {job}"
        f"TASK: Generate a tailored cover letter that:"
        f"-Highlights relevant experience"
        f"-Aligns skills with job requirements"
        f"-Sounds natural and human-written"
        f"-Make it 3 paragraphs with the last paragraph summing things up and thanking for the employers time"
        f"-Don't include a header just go straight into it with Dear Hiring Manager,..."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_text}],
        temperature=0.7, # How creative the language gets
        max_tokens=700
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(sendMessage("Describe a cat in three words"))
