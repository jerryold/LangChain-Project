#Import os to set API key
import os
#Import OpenAI as main LLM Service
from langchain.llms import OpenAI

#Bring streamlit as st
import streamlit as st

# Import PDF Document loaders
from langchain.document_loaders import PyPDFLoader

# Import chroma as the vector store 
from langchain.vectorstores import Chroma

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set APIkey for OpenAI Service
# Can sub this out for other LLM providers
os.environ['OPENAI_API_KEY'] = 'your own openai key'

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)

# Create and load PDF Loader
loader = PyPDFLoader('NVM1.4a_Spec.pdf')
# Split pages from pdf 
pages = loader.load_and_split()
# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(pages, collection_name='nvmespec')

# Create vectorstore info object - metadata repo?
vectorstore_info = VectorStoreInfo(
    name="NVMe Specification Assisant",
    description="a NVMe Specification as a pdf",
    vectorstore=store
)
# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
st.title('🔗 💾NVMe Specification Assisant')
# Create a text input box for the user
prompt = st.text_input('Input your question here')

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(prompt)
    # write it out to the screen
    st.write(response)

    # With a streamlit expander  
    with st.expander('Document Similarity Search'):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Write out the first 
        st.write(search[0][0].page_content) 