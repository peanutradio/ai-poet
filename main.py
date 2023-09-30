# from dotenv import load_dotenv
# load_dotenv()
from langchain.chat_models import ChatOpenAI
import streamlit as st

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("나는 강아지를 미워..")
# print(result)

chat_model = ChatOpenAI()

st.title('Artificial Intelligence Poet ')

content = st.text_input('시의 주제를 제시해 주세요.' ) 

if st.button('시 작성 요청하기'):
    with st.spinner('In the process of writing a poem...'):
        result = chat_model.predict(content  + "에 대한 시를 써줘")
        st.write(result)

# #  st.write('시의 주제는', title)