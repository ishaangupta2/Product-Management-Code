import streamlit as st

def main():
    st.title('Simple Streamlit App')

    # User input
    user_input = st.text_input("Enter your name:")

    # Button to display greetings
    if st.button('Greet'):
        st.write(f'Hello {user_input}, welcome to Streamlit!')

if __name__ == "__main__":
    main()