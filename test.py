import streamlit as st
import pandas as pd

st.title("포항시 2024 지역별 대기통합지수 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
