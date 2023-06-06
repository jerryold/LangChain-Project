# Youtube Summary in a Langchain Pipeline📕
This project highlights how to summary the youtube content to help listener who can understand the video in a short time . You can type the youtube link and use it alongside an LLM without the need for fine tuning. 


# Introduction 🚀
1. Create a virtual environment `python -m venv youtubegpt`
2. Activate it: 
   - Windows:`.\youtubegpt\Scripts\activate`
   - Mac: `source youtubegpt/bin/activate`
3. Clone this repo `git clone https://github.com/jerryold/LangChain-Project/YoutubeSummary`
4. Go into the directory `cd LangChain-Project`
5. Install the required dependencies `pip install -r requirements.txt`
6. Add your own OpenAI API Key to first placeholder of streamlit application
#### OpenAI APIKEY-The most import thing is that you need apply your own key in offical website🔑
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/ee344176-8784-4b45-8936-53fa734d8e56)

7. Start the app `streamlit run app.py`  


# Package Summary📙
*  youtube-transcript-api is a python library that allows you to get the transcripts of YouTube videos. It also comes with a downloader and a CLI.
*  Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.
*  pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.

# The demo screenshot of the app🪧
* Initial Screen
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/2a3d592f-3ec6-461d-8329-1f3a703f2535)  
* Get Insigh tScreen
![image](https://github.com/jerryold/LangChain-Project/assets/12774427/28d8e823-b4f9-42fd-83e8-d9adf9b2de7e)
  

# Demo💻
[youtubegpt.webm](https://github.com/jerryold/LangChain-Project/assets/12774427/a6771a43-eac1-4924-a3b9-3ab517120ab9)



# Other References 🔗
<p>The main LG Agent used:<a href="https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html">Langchain VectorStore Agents
</a></p>




