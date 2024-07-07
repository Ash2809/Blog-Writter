import streamlit as st
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate


def get_response(blog_topic,words):
    model_path=r"C:\Projects\Blog-Writter\model\llama-2-7b-chat.ggmlv3.q4_0.bin"
    llm=CTransformers(model=model_path,
                    model_type="llama",
                    config={"max_new_tokens":512,"temperature":0.8})

    prompt_template="""You are a Helpfull Professional Assistant. Write a comprehensive blog on {blog_topic} within {no_of_words} words.
    .Write it in a Professional way. """

    prompt=PromptTemplate(template=prompt_template,input_variables=["blog_topic","no_of_words"])

    prompt=prompt.format(blog_topic=blog_topic,no_of_words=words)

    response=llm(prompt)
    print(response)

    return response


st.set_page_config(page_title="BLOG GENERATION",
                   page_icon=":book:",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("GENERATE BLOGS :book:")

blog_topic=st.text_input("Enter topic of Blog")

words = st.slider(
    "Select a range of values",
    0, 500)
st.write("Words:", words)

submit=st.button("Generate")

if submit:
    st.balloons()
    st.write(get_response(blog_topic,words))