import streamlit as st
import pandas as pd
import plotly.express as px

st.title("포항시 2024 지역별 대기통합지수 시각화")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 컬럼명 예시: '지역', '대기통합지수', '위도', '경도'
    if not {'지역', '대기통합지수', '위도', '경도'}.issubset(df.columns):
        st.error("CSV에 '지역', '대기통합지수', '위도', '경도' 컬럼이 필요합니다.")
    else:
        st.dataframe(df)

        # Plotly 지도
        fig = px.scatter_mapbox(
            df,
            lat='위도',
            lon='경도',
            color='대기통합지수',
            size='대기통합지수',
            size_max=20,
            color_continuous_scale="YlOrRd",
            hover_name='지역',
            hover_data={'대기통합지수': True, '위도': False, '경도': False},
            zoom=10,
            height=700,
        )

        fig.update_layout(
            mapbox_style="carto-positron",
            margin={"r":0, "t":0, "l":0, "b":0}
        )

        st.plotly_chart(fig, use_container_width=True)

