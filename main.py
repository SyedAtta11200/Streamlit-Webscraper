import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

st.title('Ai Web Scraper')
url = st.text_input('Enter the Website URL')

if st.button('Scrape Site'):
    st.write('Scraping the website:', url)
    
    dom_content = scrape_website(url)
    body_content = extract_body_content(dom_content)
    cleaned_content = clean_body_content(body_content)

        # Store the DOM content in Streamlit session state
    st.session_state.dom_content = cleaned_content

        # Display the DOM content in an expandable text box
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
   

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)