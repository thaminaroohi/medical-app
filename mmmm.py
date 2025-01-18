import streamlit as st
import openai
import random

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'  # Replace with your actual OpenAI API key

# Sample medicine data (same as before)
medicines = {
    "headache": {
        "medicine": "Paracetamol",
        "benefits": "Relieves pain and reduces fever.",
        "when_to_take": "Take one tablet every 4-6 hours as needed.",
        "foods_to_eat": "Drink plenty of water, eat light foods like fruits.",
        "foods_to_avoid": "Avoid caffeinated drinks and spicy foods.",
        "natural_remedies": "Rest in a quiet, dark room. Drink ginger tea."
    },
    "cold": {
        "medicine": "Diphenhydramine",
        "benefits": "Helps relieve runny nose and sneezing.",
        "when_to_take": "Take one tablet before bed.",
        "foods_to_eat": "Hot soups, citrus fruits, herbal teas.",
        "foods_to_avoid": "Avoid cold drinks and dairy.",
        "natural_remedies": "Steam inhalation, honey and ginger tea."
    },
    "fever": {
        "medicine": "Ibuprofen",
        "benefits": "Reduces fever and relieves pain.",
        "when_to_take": "Take one tablet every 6-8 hours, not exceeding 3 doses a day.",
        "foods_to_eat": "Hydrate well, consume light meals like soup or fruits.",
        "foods_to_avoid": "Avoid spicy, greasy foods and alcohol.",
        "natural_remedies": "Stay hydrated, take a lukewarm bath to lower temperature."
    },
    "cough": {
        "medicine": "Cough Syrup (Dextromethorphan)",
        "benefits": "Suppresses cough and eases throat irritation.",
        "when_to_take": "Take one dose every 4-6 hours as needed.",
        "foods_to_eat": "Warm liquids like herbal teas and broths.",
        "foods_to_avoid": "Avoid acidic drinks like orange juice.",
        "natural_remedies": "Honey and lemon tea, steam inhalation."
    }
}

# Streamlit app
def main():
    # Sidebar setup with options for games
    menu = ["Welcome", "Nearest Hospital", "Nearest Medical Shop", "Natural Remedies", "Mind Games"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Welcome":
        display_welcome_page()

    elif choice == "Nearest Hospital":
        display_nearest_hospital()

    elif choice == "Nearest Medical Shop":
        display_nearest_medical_shop()

    elif choice == "Natural Remedies":
        display_natural_remedies()

    elif choice == "Mind Games":
        display_game_options()

    # Right Sidebar for Symptom Selection and Query
    with st.sidebar:
        st.header("Select Your Symptom")
        symptom = st.selectbox("Select your symptom", ["headache", "cold", "fever", "cough"])

        # Fetch the corresponding medicine details
        medicine_info = medicines.get(symptom)

        if medicine_info:
            st.subheader(f"Suggested Medicine: {medicine_info['medicine']}")
            st.write(f"**Benefits**: {medicine_info['benefits']}")
            st.write(f"**When to Take**: {medicine_info['when_to_take']}")
            st.write(f"**Foods to Eat**: {medicine_info['foods_to_eat']}")
            st.write(f"**Foods to Avoid**: {medicine_info['foods_to_avoid']}")
            st.write(f"**Natural Remedies**: {medicine_info['natural_remedies']}")

        # Query section for additional questions
        query = st.text_input("Have any other questions? Ask here:")

        if query:
            # Generate response using OpenAI GPT-3/4 API
            response = get_gpt3_response(query)
            st.write(f"Response: {response}")

# Function to fetch nearest hospital (No API, only mock data)
def display_nearest_hospital():
    st.write("Since Google Maps API is disabled, here's a list of hospitals in your area:")
    st.write("1. City Hospital - Address: 123 Main St, City, Country")
    st.write("2. Central Health Center - Address: 456 Health Ave, City, Country")
    st.write("3. General Medical Hospital - Address: 789 General Blvd, City, Country")

# Function to fetch nearest medical shop (No API, only mock data)
def display_nearest_medical_shop():
    st.write("Since Google Maps API is disabled, here's a list of medical shops in your area:")
    st.write("1. Pharma Meds - Address: 123 Med St, City, Country")
    st.write("2. Healthy Pharmacy - Address: 456 Health Ave, City, Country")
    st.write("3. Medicine Corner - Address: 789 Pharma Blvd, City, Country")

# Display Natural Remedies
def display_natural_remedies():
    st.subheader("Natural Remedies")
    st.write("Explore natural remedies for common symptoms:")
    st.write("- **Headache**: Rest in a quiet, dark room. Drink ginger tea.")
    st.write("- **Cold**: Honey and ginger tea, steam inhalation.")
    st.write("- **Fever**: Stay hydrated, lukewarm bath to lower temperature.")
    st.write("- **Cough**: Honey and lemon tea, steam inhalation.")

# Display Welcome Page
def display_welcome_page():
    st.title("Welcome to the Medicinal Suggestions App")
    st.write("This app helps you find the right medicines based on your symptoms and provides "
             "information about nearby hospitals, medical shops, and natural remedies.")
    st.write("Find medicinal suggestions, hospital and medical shop locations, and even "
             "natural ways to treat common ailments.")
    
    st.image("https://via.placeholder.com/800x300.png?text=Welcome+to+Medicinal+App", use_column_width=True)
    
    # Display inspirational quotes
    st.write("**Inspirational Health Quote**:")
    st.write('"The greatest wealth is health." – Virgil')

# Display available games in the "Mind Games" section
def display_game_options():
    games = ["Math Quiz", "Word Guessing Game", "Number Guessing Game", "Trivia Quiz", "Rock Paper Scissors"]
    game_choice = st.selectbox("Choose a game to play", games)

    if game_choice == "Math Quiz":
        math_quiz()
    elif game_choice == "Word Guessing Game":
        word_guessing_game()
    elif game_choice == "Number Guessing Game":
        number_guessing_game()
    elif game_choice == "Trivia Quiz":
        trivia_quiz()
    elif game_choice == "Rock Paper Scissors":
        rock_paper_scissors()

# Math Quiz Game
def math_quiz():
    st.header("Math Quiz")
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = st.number_input(f"What is {num1} + {num2}?", min_value=0, step=1)
    
    if answer == num1 + num2:
        st.success("Correct!")
    elif answer != 0:
        st.error(f"Oops! The correct answer was {num1 + num2}. Try again!")

# Word Guessing Game
def word_guessing_game():
    st.header("Word Guessing Game")
    word_to_guess = random.choice(["apple", "banana", "cherry", "grape", "orange"])
    guess = st.text_input("Guess the fruit name:")

    if guess.lower() == word_to_guess:
        st.success("Correct! Well done.")
    elif guess:
        st.error("Oops! Try again.")

# Number Guessing Game
def number_guessing_game():
    st.header("Number Guessing Game")
    number = random.randint(1, 100)
    guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100)
    
    if guess == number:
        st.success("Correct! Well done.")
    elif guess < number:
        st.warning("Too low! Try again.")
    elif guess > number:
        st.warning("Too high! Try again.")

# Trivia Quiz Game
def trivia_quiz():
    st.header("Trivia Quiz")
    questions = {
        "What is the capital of France?": ["Paris", "London", "Berlin", "Rome"],
        "Which planet is known as the Red Planet?": ["Mars", "Earth", "Venus", "Jupiter"],
        "Who wrote 'Romeo and Juliet'?": ["Shakespeare", "Dickens", "Austen", "Hemingway"]
    }
    
    question, options = random.choice(list(questions.items()))
    answer = st.radio(question, options)
    
    if answer == options[0]:
        st.success("Correct!")
    else:
        st.error("Oops! That's not correct.")

# Rock Paper Scissors Game
def rock_paper_scissors():
    st.header("Rock Paper Scissors")
    user_choice = st.selectbox("Choose your option", ["Rock", "Paper", "Scissors"])
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        st.write(f"You chose {user_choice}, Computer chose {computer_choice}. It's a draw!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.write(f"You chose {user_choice}, Computer chose {computer_choice}. You win!")
    else:
        st.write(f"You chose {user_choice}, Computer chose {computer_choice}. You lose!")

def get_gpt3_response(query):
    """
    Function to generate a response using OpenAI GPT-3 (or GPT-4).
    """
    try:
        # OpenAI API call to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use other engines like "gpt-4" if you have access
            prompt=query,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()
