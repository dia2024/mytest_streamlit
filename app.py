import streamlit as st
import streamlit as st
st.title('문자열')
st.header('header : 헤더')
st.subheader('subheader : 서브헤더')
st.text('text')
st.code('code')
code = '''
def hello():
    print('streamlit!')
    '''
st.code(code)
st.markdown('스트림릿에서 **마크다운**을 사용할수 있다. :sunglasses:')
