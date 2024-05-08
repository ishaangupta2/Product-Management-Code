import streamlit as st
from openai import OpenAI


# Ensure your API key is set as an environment variable

client = OpenAI(api_key="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")

def main():
    st.title('ICAO Theory Assistant')

    # User input for the question
    question = st.text_area("Enter the question")

    if st.button('Answer Aviation Questions'):
        response = client.chat.completions.create(
            model="gpt-4",
            temperature=0.5,
            messages=[
                {
                    "role": "system",
                    "content": "As an aviation expert, answer questions related to aviation safety, regulations, and procedures."
                },
                {
                    "role": "user",
                    "content": f"Here is the question: {question}"
                }
            ]
        )

        # Display the formatted answer
        answer = response.choices[0].message.content
        st.write(answer)  # Using st.write to display text; st.json is primarily for JSON objects

if __name__ == "__main__":
    main()