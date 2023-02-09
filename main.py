import streamlit as st
from PIL import Image
import time


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)


st.title('杉山健のHP')
st.write('よろしくお願いします👍')

option = st.sidebar.text_input('あなたが好きなコトを教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの好きなコトは', option, 
'あなたの今の調子は', condition

if st.checkbox('杉山健を見てみる'):
   img = Image.open('sugiyamaken.jpeg')
   st.image(img, caption='杉山健', use_column_width=True)


toiawase1 = st.expander('杉山健とどこで会えるの？')
toiawase1.write('大体津田沼にいるよ！4月からは本山だね！')
toiawase2 =  st.expander('杉山健の身長は？')
toiawase2.write('174センチだよ！もう少し伸びたい！')
toiawas3 = st.expander('杉山健の生まれは？')
toiawas3.write('大阪府八尾市だよ！住んだことはないみたい')