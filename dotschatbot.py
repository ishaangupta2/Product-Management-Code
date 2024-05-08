import streamlit as st
import random
import datetime

# Improved validation and error handling
def validate_package_number(package_number):
    if len(package_number) == 8 and package_number.isdigit():
        return True
    else:
        return False

# Enhanced tracking function with error handling
def track_package(package_number):
    try:
        statuses = ["Picked Up", "In Transit", "Out for Delivery", "Delivered"]
        status_durations = [2, 3, 1, 0]
        current_status_index = random.randint(0, len(statuses) - 1)
        current_status_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 7))
        status_dates = {}
        for i, status in enumerate(statuses):
            if i < current_status_index:
                status_dates[status] = current_status_date - datetime.timedelta(days=sum(status_durations[i+1:]))
            elif i == current_status_index:
                status_dates[status] = current_status_date
            else:
                status_dates[status] = current_status_date + datetime.timedelta(days=sum(status_durations[:i]))
        for status in statuses:
            status_dates[status] += datetime.timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        status_history = "\n".join([f"{status_dates[status].strftime('%Y-%m-%d %H:%M:%S')}: {status}" for status in statuses if status_dates[status] <= datetime.datetime.now()])
        current_status = statuses[current_status_index]
        return f"Package {package_number} is currently {current_status} \n\n Delivery Status History: \n\n{status_history}"
    except Exception as e:
        return f"Error tracking package: {str(e)}"

# Function to handle general inquiries with improvements
def handle_inquiry(inquiry_option):
    inquiry_responses = {
        "Refund Policy": """
        Our refund policy allows customers to return items within 30 days of purchase. 
        To be eligible for a refund, the item must be unused and in the same condition that 
        you received it. It must also be in the original packaging. 
        Please note that certain items, such as perishable goods, are not eligible for refunds.
        """,
        "FAQs on Delivery": """
        **Q: How long does delivery take?**
        A: Delivery times vary depending on your location and the shipping method chosen. 
        Standard shipping typically takes 3-5 business days, while expedited shipping 
        may arrive within 1-2 business days.
        """,
        "Return Policies": """
        Our return policy allows customers to return items within 30 days of purchase 
        for a full refund. To be eligible for a return, the item must be unused and 
        in the same condition that you received it. It must also be in the original packaging.
        Please contact our customer service team to initiate a return.
        """,
        "Contact Info": "You can contact us at support@example.com or +1 (123) 456-7890."
    }
    return inquiry_responses.get(inquiry_option, "Inquiry option not recognized.")


# Main function with chat-like interaction and visual enhancements
def main():
    st.set_page_config(layout="wide", page_title="Customer Service Chatbot")
    st.title("Customer Service Chatbot")

    st.markdown(
        """
        <style>
        .chat-bubble {
            padding: 10px;
            border-radius: 20px;
            margin: 5px;
            max-width: 70%;
        }
        .user-bubble {
            background-color: #e5e5ea; /* Light gray */
            align-self: flex-end;
            text-align: right;
            color: black;
            border-top-right-radius: 5px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            border-top-left-radius: 20px;
        }
        .bot-bubble {
            background-color: #d7f3f7; /* Light blue */
            align-self: flex-start;
            color: black;
            border-top-left-radius: 5px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            border-top-right-radius: 20px;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

    option = st.radio("How can we help you today?", ["Track Package", "Give Feedback", "General Inquiry", "Request Refund"], key="option")

    if option == "Track Package":
        st.markdown("<div class='chat-bubble bot-bubble'>Enter your package number (8 digits)</div>", unsafe_allow_html=True)
        package_number = st.text_input("", max_chars=8)
        if st.button('Track'):
            if validate_package_number(package_number):
                with st.spinner('Tracking your package...'):
                    result = track_package(package_number)
                    st.markdown(f"<div class='chat-bubble bot-bubble'>{result}</div>", unsafe_allow_html=True)
            else:
                st.error("Invalid package number. Please ensure it is exactly 8 digits.")

    elif option == "Give Feedback":
        feedback_type = st.radio("Select feedback type", ["Supplier", "Daraz", "Delivery Person"])
        st.markdown(f"<div class='chat-bubble user-bubble'>Select feedback type - {feedback_type}</div>", unsafe_allow_html=True)
        feedback = st.text_area("Enter your feedback", height=150)
        if st.button('Submit Feedback'):
            if feedback:
                # Save feedback to a file
                with open("feedback.txt", "a") as file:
                    file.write(f"Feedback Type: {feedback_type}\n")
                    file.write(f"Feedback: {feedback}\n")
                with st.spinner("Submitting your feedback..."):
                    result = f"Thank you for your {feedback_type.lower()} feedback! We have recorded your feedback."
                    st.markdown(f"<div class='chat-bubble bot-bubble'>{result}</div>", unsafe_allow_html=True)
            else:
                st.error("Please enter some feedback before submitting.")


    elif option == "General Inquiry":
        inquiry_option = st.radio("Select an inquiry option:", ["Refund Policy", "FAQs on Delivery", "Return Policies", "Contact Info"])
        st.markdown(f"<div class='chat-bubble user-bubble'>Select an inquiry option - {inquiry_option}</div>", unsafe_allow_html=True)
        if st.button('Get Information'):
            result = handle_inquiry(inquiry_option)
            st.markdown(f"<div class='chat-bubble bot-bubble'>{result}</div>", unsafe_allow_html=True)

    elif option == "Request Refund":
        st.markdown("<div class='chat-bubble bot-bubble'>Select Product</div>", unsafe_allow_html=True)
        products = ["Product A", "Product B", "Product C"]
        selected_product = st.radio("", products)
        st.markdown(f"<div class='chat-bubble user-bubble'>Select Product - {selected_product}</div>", unsafe_allow_html=True)
        st.markdown("<div class='chat-bubble bot-bubble'>Select Reason for Refund</div>", unsafe_allow_html=True)
        reason = st.radio("", ["Product Defect or Damage", "Incorrect Item Received", "Cancellation of Service", "Double Billing", "Unauthorized Transaction"])
        st.markdown(f"<div class='chat-bubble user-bubble'>Select Reason for Refund - {reason}</div>", unsafe_allow_html=True)
        additional_details = st.text_area("Additional Details", height=150)
        if st.button("Submit Refund Request"):
            refund_status = "Refund Processed" if random.choice([True, False]) else "Refund Pending"
            st.markdown(f"<div class='chat-bubble bot-bubble'>Refund request for {selected_product} has been {refund_status.lower()}.</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
