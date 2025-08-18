This file explains what the project does, who it's for, and how to set it up and run it.

You can copy the content below and save it as a file named README.md in your project's main directory.

📊 Advanced YouTube Channel Insights with Gemini
This project is a web application built with Streamlit that leverages the power of Google's Gemini Pro AI model to provide in-depth analysis of any public YouTube channel.

Simply provide a channel's URL, and the application will generate a human-readable report covering key metrics like channel overview, video performance, audience demographics, growth trends, and top content.

Features
Simple Web Interface: Clean and intuitive UI built with Streamlit.

AI-Powered Analysis: Uses the advanced reasoning capabilities of the Gemini Pro model.

Comprehensive Reports: Generates detailed insights on multiple facets of a channel.

No Technical Skills Needed: Designed for marketers, creators, and analysts to use without writing code.

Dynamic Prompting: The user's input is dynamically inserted into a sophisticated prompt for the AI.

 How It Works
The application follows a simple but powerful workflow:

User Input: The user enters a YouTube channel URL into the text input field in the Streamlit web interface.

Prompt Construction: When the "Analyze" button is clicked, the application takes the URL and embeds it into a pre-defined, detailed prompt. This prompt instructs the Gemini model to act as a YouTube analytics expert.

API Call: The prompt is sent to the Google Gemini API using the google-generativeai Python library.

AI Generation: The Gemini model processes the request. Based on its vast training data, which includes a wide range of public information about YouTube trends and channels, it generates a detailed analysis.

Display Results: The generated text response, formatted in markdown, is sent back to the Streamlit app and displayed to the user in a clean, report-style format.

Getting Started
Follow these instructions to set up and run the project on your local machine.

Prerequisites
Python 3.8 or newer

A Google Gemini API Key. You can get one from Google AI Studio.

1. Clone the Repository
Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Create a Virtual Environment
It's highly recommended to use a virtual environment to keep project dependencies isolated.

On macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
Create a file named requirements.txt in the project root and add the following lines:

streamlit
google-generativeai
python-dotenv
Then, install them using pip:

Bash

pip install -r requirements.txt
4. Set Up Your API Key
Important: Never hardcode your API keys directly in the script. It's a security risk. We'll use an environment file.

Create a file named .env in the root of your project directory.

Add your Gemini API key to this file:

GEMINI_API_KEY="AIzaSy...Your...Key...Here"
5. Update Your Python Script
Modify your main Python script (e.g., app.py) to load the API key securely from the .env file.

Replace this line:

Python

API_KEY = "" #REPLACE WITH YOUR API
With these lines at the top of your script:

Python

import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from .env

API_KEY = os.getenv("GEMINI_API_KEY")
Make sure to import os and from dotenv import load_dotenv.

6. Run the Application
Now you're ready to launch the Streamlit app!

Bash

streamlit run app.py
Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

🔧 The Core Prompt
The effectiveness of this tool comes from the detailed prompt sent to the Gemini model. This prompt guides the AI to generate a structured and relevant report. You can modify it to change the structure or content of the analysis.

<details>
<summary><strong>Click to view the prompt template</strong></summary>

You are an advanced YouTube analytics expert.
Analyze the YouTube channel at {channel_url} and provide detailed insights in a **well-structured, user-friendly report**.
DO NOT return JSON or code. Write as a human-readable report with headings and bullet points.

Include:
1.Channel Overview – name, description, niche, estimated popularity and subscriber count and owner name is known
2.Video Performance – estimated average views, engagement level, and possible earnings range.
3.Audience Insights – probable age group, location trends, and interests.
4.Growth Trends – subscriber and view count growth pattern (historical trend if possible).
5.Top Content – list 5 most popular videos or playlists with short descriptions.

Use publicly available assumptions and general trends if exact data is unavailable.
Make it visually appealing with markdown styling.
</details>

