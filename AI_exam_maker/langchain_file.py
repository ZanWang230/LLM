def generate_test(number,subject,password):
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    with open('openAI_secret_key.txt') as file:
        password=file.read()
    model=ChatOpenAI(model='gpt-4',
                  openai_api_key=password)
    prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '''你是一個國小出題老師，請根據指示出選擇體，除了題目之外不要有其他文本，全部的題目跟每一題的答案用#隔開，範例如下:
        1.請問6+3是多少? A)1, B)2, C)3, D)9 \n
        2.請問6*9是多少? A)55, B)65, C)54, D)90 \n
        3.請問9*3是多少? A)22, B)27, C)26, D)25 \n
         #
         1. D \n
         2. C \n
         3. B \n'''),
        ('human', '幫我出{number}題，科目為{subject}的題目')
    ]
)
    model_chain=(prompt|model).invoke({'number':number,'subject':subject})
    return model_chain.content
