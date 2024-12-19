import streamlit as st
with st.sidebar:
    password=st.text_input('輸入OpenAI API密碼',type='password')
    st.markdown('''<a href="https://platform.openai.com/docs/overview">點擊獲取API密碼</a>''',unsafe_allow_html=True)
st.markdown('AI智能PDF問答程式')
data=st.file_uploader('上傳PDF檔案',type='PDF')
if data:
    with open(data.name,'wb') as file:
        file.write(data.getbuffer())
        print('文檔已下載')
if data:
    print(data.name)
    print(data)
    question=st.text_input('請輸入您的問題')
submit=st.button('提交')
if submit:
    with st.spinner('AI思考中....'):
        from model import pdf_parser
        st.write(pdf_parser(data.name,question,password))
