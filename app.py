import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers




def get_llama_response(input_text,no_words,blog_style):
    llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q4_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.1})



    # PromptTemplate
    template = """
    Write a blog post targeting {} professionals, focusing on the topic of "{}". 
    Ensure the content is engaging, informative, and tailored to the interests and needs of the target audience. 
    The blog post should be concise yet comprehensive, spanning approximately {} words.
    """.format(blog_style, input_text, no_words)


    prompt_template= PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                                    template=template)
    
    ## generate response

    response=llm((prompt_template.format(blog_style=blog_style,input_text=input_text,no_words=no_words)))
    return response


st.set_page_config(page_title = 'Blog Generation Application',layout='centered',page_icon='🤖',initial_sidebar_state='collapsed')

st.header('Generate Blog 🤖')


input_text=st.text_input("Enter the Blog Topic")


## creating to more columns for additonal 2 fields

col1, col2 = st.columns([5, 5])


with col1:
    no_words = col1.number_input('No of Words', min_value=0, step=1)
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People', 'Tech Enthusiasts', 
                               'Business Professionals', 'Critics', 'Hobbyists', 'Enthusiasts', 
                               'Academic Community', 'Industry Professionals'),
                              index=0)
    
submit = st.button('Generate')


## Final response 

if submit:
    response = get_llama_response(input_text, no_words, blog_style)
    st.write(response)