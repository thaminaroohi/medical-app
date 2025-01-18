import streamlit as st
import openai
import os
from googleapiclient.discovery import build

# Set OpenAI API Key
openai.api_key = "your-openai-api-key"

# Set YouTube API Key
YOUTUBE_API_KEY = "your-youtube-api-key"

# Function to get a recipe from OpenAI
def get_recipe(vegetables):
    prompt = f"Suggest a dish using {', '.join(vegetables)} and provide step-by-step cooking instructions."
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

# Function to fetch a YouTube cooking video
def get_youtube_video(query):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    search_response = youtube.search().list(
        q=query + " recipe",
        part="snippet",
        maxResults=1
    ).execute()

    if "items" in search_response:
        video_id = search_response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    return None

# Streamlit UI
st.title("🍲 AI Cooking Assistant")

# List of vegetables
vegetables = st.multiselect("Select available vegetables:", 
                            ["Tomato", "Onion", "Garlic", "Potato", "Carrot", 
                             "Cabbage", "Spinach", "Broccoli", "Pepper", "Mushroom"])

if st.button("Get Recipe"):
    if vegetables:
        with st.spinner("Generating recipe..."):
            recipe = get_recipe(vegetables)
            st.subheader("🍽 Suggested Dish")
            st.write(recipe)

            # Get a video
            video_url = get_youtube_video(f"{vegetables[0]} recipe")
            if video_url:
                st.subheader("🎥 Cooking Video")
                st.video(video_url)
    else:
        st.error("Please select at least one vegetable!")

