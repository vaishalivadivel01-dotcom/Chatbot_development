
import pandas as pd
import os
from datetime import datetime

questions = pd.read_csv("dataset/sample_questions.csv")

print("Welcome to My Chatbot!")

while True:
    user_input = input("You: ").strip().lower()

    result = questions[
        questions["question"].str.strip().str.lower() == user_input
    ]

    if not result.empty:
        response = result.iloc[0]["expected_response"]
    else:
        response = "Sorry, I don't understand."

    print("Bot:", response)

    chat = pd.DataFrame([{
        "Date": datetime.now(),
        "User": user_input,
        "Bot": response
    }])

    file_path = "dataset/chat_history.csv"
    chat.to_csv(
        file_path,
        mode="a",
        header=not os.path.exists(file_path) or os.path.getsize(file_path) == 0,
        index=False
    )

    if user_input == "bye":
        break
