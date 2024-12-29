from app.configs.constant import BASE_API_URL , LANGFLOW_ID, FLOW_ID, APPLICATION_TOKEN, ENDPOINT
import json
import streamlit as st
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings
from app.logging.logs import log_decorator
def run_flow(message: str,) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message
    }
    if APPLICATION_TOKEN:
        headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
@log_decorator
def main(message: str):
    response = run_flow(
        message=message    )

    response = response['outputs'][0]["outputs"][0]["outputs"]["message"]['message']['text']
    print(json.dumps(response, indent=2))
    return response
if __name__ == "__main__":
    st.title("Multi-Agent Chatbot for Customer Support")
    query = st.text_area("This is a multi-agent chatbot for customer support.")
    if st.button("Submit"):
        if not query.strip():
            st.warning("Please enter a query.")
        try:
            with st.spinner("Running flow..."):
                ans = main(message=query)
                st.markdown(f"Response: {ans}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


