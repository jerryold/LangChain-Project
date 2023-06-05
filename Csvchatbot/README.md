# CSVChatbot📕
This project highlights how to create chatbot to analyze with the csv file . You can load in a csv based document and use it alongside an LLM without the need for fine tuning. In our case, we utilitize it on the NBA report of the Player Salay from 2022 to 2025. The dataset is from kaggle<a href="[https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html](https://www.kaggle.com/datasets/omarsobhy14/nba-players-salaries)">


# Introduction 🚀
1. Create a virtual environment `python -m venv csvchatbot`
2. Activate it: 
   - Windows:`.\csvchatbot\Scripts\activate`
   - Mac: `source langchain/bin/activate`
3. Clone this repo `git clone https://github.com/jerryold/LangChain-Project/Csvchatbot`
4. Go into the directory `cd Csvchatbot`
5. Install the required dependencies `pip install -r requirements.txt`
6. Add your own OpenAI APIKey to line 24 of `csvchatbot.py`
#### OpenAI APIKEY-The most import thing is that you need apply your own key in offical website🔑
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/ee344176-8784-4b45-8936-53fa734d8e56)

7. Start the app `streamlit run app.py`  

# Package Summary📙
*  PyPDF2 is a free and open source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files
*  Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.
*  Streamlit-chat is a Streamlit Component, for a Chat-bot UI

# The demo screenshot of the app🪧
* Initial Screen
 ![image](https://github.com/jerryold/LangChain-Project/assets/12774427/04af6cf2-f3f5-4565-b197-edf82e82d8a5)
   
 # Demo💻
 [CSVChatbot Demo.webm](https://github.com/jerryold/LangChain-Project/assets/12774427/180114d4-d6d3-45b7-9675-7435d861d25a)


* ChatScreen
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/dbdf3697-4d31-4e24-b3bc-101e957a36dc)



# Other References 🔗
<p>The main LG Agent used:<a href="https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html">Langchain VectorStore Agents
</a></p>



