import random
from IPython.display import display, HTML

# Helper function for colorful output
def colorful_message(message, color="black"):
    display(HTML(f"<p style='color:{color}; font-size:16px;'>{message}</p>"))

# Simple NLP-based chatbot
def chatbot():
    colorful_message("🤖 Hello! I am your AI Chatbot. Ask me anything!", "blue")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # NLP keyword-based responses
        if "hello" in user_input or "hi" in user_input:
            colorful_message("Hello there! How can I help you today?", "green")
        
        elif "how are you" in user_input:
            colorful_message("I'm doing great, thanks for asking! How about you?", "orange")
        
        elif "name" in user_input:
            colorful_message("My name is ChatBot, your friendly AI assistant 🤖", "blue")
        
        elif "weather" in user_input:
            colorful_message("I can't check live weather here, but I hope it's sunny where you are! ☀️", "brown")
        
        elif "joke" in user_input:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the computer go to the doctor? Because it caught a virus!",
                "Why was the math book sad? Because it had too many problems."
            ]
            colorful_message(random.choice(jokes), "red")
        
        else:
            # Fallback: always answer something
            responses = [
                "That's an interesting question! Let me think about it 🤔",
                "I may not know the exact answer, but I love your curiosity!",
                "Good question! Can you tell me more?",
                "I’m still learning, but I’ll try my best to help!"
            ]
            colorful_message(random.choice(responses), "gray")
        
        # Quit option after each response
        choice = input("Do you want to quit? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            colorful_message("👋 Goodbye! Have a great day!", "purple")
            break

# Run the chatbot
chatbot()
