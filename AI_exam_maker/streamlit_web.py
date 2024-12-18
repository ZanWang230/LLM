from langchain_file import generate_test
import streamlit as st

st.markdown("<h1 style='font-size: 50px;'>AI出題老師</h1>", unsafe_allow_html=True)
subject=st.text_input('科目?')
number=st.number_input('幾題?',value=1,step=1)
submit=st.button('submit')
with st.sidebar:
    password=st.text_input('輸入OpenAi API密碼',type="password")
    st.markdown('''<a href="https://platform.openai.com/docs/overview">點擊獲取API密碼</a>''',unsafe_allow_html=True)
if submit:
    loading='AI出題中...'
    if number>=30:
        loading='AI出題中...\n題目較多~請耐心等待'
    with st.spinner(loading):
        res=generate_test(number,subject,password)
        show=st.write(res.split('#')[0])
        with st.sidebar:
            ans=st.write(res.split('#')[1])