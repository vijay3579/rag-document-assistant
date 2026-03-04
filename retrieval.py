from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def load_vector_store():

	embeddings= HuggingFaceEmbeddings(
		model_name="sentence-transformers/all-MiniLM-L6-v2"
	)

	vector_store =Chroma(
		persist_directory="vector_store",
		embedding_function=embeddings
	)

	return vector_store

def retrieve_documents(query,k=3):
	vector_store= load_vector_store()
	results = vector_store.similarity_search(query,k=k)

	return results

def generate_answer(query):
	docs= retrieve_documents(query)

	context ="\n\n".join([doc.page_content for doc in docs])

	prompt = f"""

	Answer the question using the context below.

	context:
	{context}

	Question:
	{query}

	Answer:
	"""

	llm = ChatOpenAI(model="gpt-4o-mini")

	response = llm.invoke(prompt)

	return response.content, docs


if __name__ == "__main__":

	question=input("Ask a question:")

	answer = generate_answer(question)

	print("\n AI Answer:\n")

	print(answer)
