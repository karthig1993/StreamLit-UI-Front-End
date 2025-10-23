import streamlit as st
import requests

st.set_page_config(page_title="Prompt Squad Uploader", page_icon="🚀")

# Check login
"""
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please login first from the Login page.")
    st.stop()
"""
    

st.title("🚀 Prompt Squad Document Uploader")
st.subheader("Secure upload to S3 via AWS Lambda")

LAMBDA_ENDPOINT = "https://your-lambda-url.amazonaws.com/upload"

uploaded_file = st.file_uploader("Upload PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    st.info(f"📁 Selected: {uploaded_file.name}")
    if st.button("Upload to S3"):
        try:
            headers = {"Authorization": f"Bearer {st.session_state['access_token']}"}
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(LAMBDA_ENDPOINT, headers=headers, files=files)

            if response.status_code == 200:
                st.success("✅ File uploaded successfully to S3!")
            else:
                st.error(f"❌ Upload failed. {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
