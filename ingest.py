from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def load_and_split_document(file_path):
	"""
	Load a pdf document and split it into smaller chunks
	"""

	#Load pdf
	loader = PyPDFLoader(file_path)
	documents = loader.load()

	#Create Text splitter
	text_splitter = RecursiveCharacterTextSplitter(
		chunk_size=500,
		chunk_overlap=100
	)

	# Split documents into chucks
	chunks = text_splitter.split_documents(documents)

	return chunks

def create_vector_store(chunks):
	embeddings = HuggingFaceEmbeddings(
		model_name ="sentence-transformers/all-miniLM-L6-v2"
	)

	vector_store = Chroma.from_documents(
		documents=chunks,
		embedding=embeddings,
		persist_directory="vector_store"
	)

	vector_store.persist()

	return vector_store

if __name__ == "__main__":
	file_path="data/sample.pdf"
	chunks = load_and_split_document(file_path)
	print(f"Total chunks created: {len(chunks)}")
	vector_store=create_vector_store(chunks)
	print("\nVector database created successfully:")
	
