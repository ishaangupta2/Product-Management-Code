import streamlit as st
from openai import OpenAI

# Ensure your API key is set as an environment variable
api_key = "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"
client = OpenAI(api_key=api_key)

def main():
    st.title('AI-driven Aviation Q&A Assistant')

    # User input for the question
    question = st.text_area("Enter the aviation-related question")

    if st.button('Get Aviation Answer') and question:
        response = client.chat.completions.create(
            model="text-davinci-003",
            prompt=f"As an aviation expert, answer questions related to aviation safety, regulations, and procedures.\nQ: {question}\nA:",
            max_tokens=100,
            stop=None,
            n=3,
            temperature=0.7
        )

        # Display the formatted answers
        answers = [choice.text.strip() for choice in response.choices]
        for i, answer in enumerate(answers):
            st.write(f"Answer {i+1}: {answer}")

if __name__ == "__main__":
    main()
