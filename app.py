import streamlit as st
import os

from ingest import load_and_split_document, create_vector_store
from retrieval import generate_answer

st.set_page_config(page_title="AI Document Assistant", layout="wide")

st.title("📄 AI Document Assistant")
st.write("Upload a document and ask questions about its content.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Upload document
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:

    file_path = f"data/{uploaded_file.name}"

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Document uploaded successfully!")

    # Process document
    if st.button("Process Document"):

        with st.spinner("Processing document..."):

            chunks = load_and_split_document(file_path)
            create_vector_store(chunks)

        st.success("Document processed and stored in vector database!")

# Ask question
st.subheader("Ask Questions")

question = st.text_input("Enter your question about the document")

if question:

    with st.spinner("Generating answer..."):

        answer, docs = generate_answer(question)

    # Save to chat history
    st.session_state.chat_history.append(("User", question))
    st.session_state.chat_history.append(("AI", answer))

    # Display chat history
    st.subheader("Conversation")

    for role, message in st.session_state.chat_history:
        if role == "User":
            st.markdown(f"**🧑 {role}:** {message}")
        else:
            st.markdown(f"**🤖 {role}:** {message}")

    # Display sources
    st.subheader("Sources")

    for i, doc in enumerate(docs):
        page_number = doc.metadata.get("page", "Unknown")
        st.markdown(f"**Source {i+1} — Page {page_number + 1}**")
        st.write(doc.page_content[:400])
        st.divider()