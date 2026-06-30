import streamlit as sm
sm.write("Madhusudan's webpage")
# Inject custom CSS to make the GitHub fork button invisible
sm.markdown(
    """
    <style>
    #GithubIcon {
        visibility: hidden !important;
    }
    footer {
        visibility: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)