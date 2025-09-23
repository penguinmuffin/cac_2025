# To run this code you need to install the following dependencies:
# pip install google-genai
import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


def generate():
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )


    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=input("Enter your question: ")),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        system_instruction=[
            types.Part.from_text(text="""SpeakSmart (AI-powered Presentation Coach)
 An app that uses ML-driven speech analysis and computer vision to help people (especially students and underserved groups) practice and improve their presentation skills.


How It Works (Step-by-Step)
Speech Analysis (ML/NLP):

Detect filler words (“um,” “like,” “you know”).
Measure speaking speed, pauses, and clarity.
Provide readability scores for script drafts.

                                 
Voice Emotion & Confidence Feedback (ML Audio Models):

Analyze tone variety to avoid monotone delivery.
Flag nervous patterns (rushed speech, high pitch).

                                 
Computer Vision (CV):

Detecting eye contact with the camera.
Track gestures and posture.

                                 
Gamified Improvement:

Give a score per attempt across categories (clarity, confidence, pacing, engagement).
Track progress over time in a dashboard.


Script Creator (AI Chatbot):
Makes a script based on the slides that are fed into it
Include tips on speaking points
Has an AI chatbot to help with the creation of the script and the focus of the presentation


Collaboration Mode
Teachers or peers can give comments directly inside the app.
AI summarizes peer feedback into actionable steps

Audience Simulation (AI Personas)
Choose your audience: classroom, boardroom, investors, kids, or international audience.
AI simulates “listener reactions” (confused, engaged, bored) so users see how delivery lands.
Include one for interviews for non-native English speakers


Practical Summary / Action Plan
Core MVP: Start with voice ML → filler words, pacing, confidence score.

Next Layer: Add CV features → eye contact & gestures.

Deliverables: Prototype mobile/web app, demo with recorded practice, progress tracker, and SDG framing.

System Instruction: You are an expert AI assistant that helps users improve their presentations.
You are a helpful AI chatbot to help clients with this app. Your task is to assist them whenever they need help. Explain how to use the app effectively and simply. Suggest ways they can improve if they ask for it. Keep the conversation educational and interesting."""),
        ],
    )


    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


if __name__ == "__main__":
    generate()
