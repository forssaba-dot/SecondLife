import streamlit as st
import os
from openai import OpenAI

st.set_page_config(page_title="SecondLife", page_icon="♻️")

st.title("♻️ SecondLife")
st.write("Don't throw it away — give it a second life!")
st.write("Tell us what you have, and we'll show you a creative way to reuse it.")

st.subheader("What item do you want to give a second life?")

with st.form("secondlife_form"):
    item = st.text_input(
        "Enter an unwanted item:",
        placeholder="Example: broken umbrella, old keyboard, milk carton"
    )

    find_button = st.form_submit_button("♻️ Find a Second Life")


if find_button:
    if not item.strip():
        st.warning("Please enter an item first.")
    else:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        with st.spinner("Finding a second life..."):
            response = client.responses.create(
                model="gpt-5.4-mini",
                input=f"""You are the AI inside an app called SecondLife.

A user has an unwanted household item: {item}

Give ONE creative, practical way to reuse or upcycle it.
Keep the answer short and beginner-friendly.

Include:
♻️ Second Life Idea
🛠️ How to make it (3-5 simple steps)
🌱 Environmental benefit
"""
            )

        st.success("Here's a Second Life idea!")
        st.markdown(response.output_text)
        