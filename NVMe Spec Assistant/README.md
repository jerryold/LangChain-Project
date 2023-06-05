# Read NVMe Spec in a Langchain Pipeline📕
This project highlights how to leverage a ChromaDB vectorstore in a Langchain pipeline to create NVMe Specification Assisant to help developer who can search SSD related work with the Assistant answer . You can load in a pdf based document and use it alongside an LLM without the need for fine tuning. 


# Introduction 🚀
1. Create a virtual environment `python -m venv langchainenv`
2. Activate it: 
   - Windows:`.\langchainenv\Scripts\activate`
   - Mac: `source langchain/bin/activate`
3. Clone this repo `git clone https://github.com/jerryold/LangChain-Project/NVMe Specification Assisant`
4. Go into the directory `cd LangchainDocuments`
5. Install the required dependencies `pip install -r requirements.txt`
6. Add your own OpenAI APIKey to line 22 of `app.py`
#### OpenAI APIKEY-The most import thing is that you need apply your own key in offical website🔑
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/ee344176-8784-4b45-8936-53fa734d8e56)

7. Start the app `streamlit run app.py`  

# LangChain Application Theory
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/083f5b81-6d4f-4c94-acc9-50e992235fa4)
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/3595da66-89cc-4d11-9eaf-49010d056cbb)


# Package Summary📙
*  PyPDF2 is a free and open source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files
*  Chroma is a database for building AI applications with embeddings.
*  Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.




# Other References 🔗
<p>The main LG Agent used:<a href="https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html">Langchain VectorStore Agents
</a></p>



