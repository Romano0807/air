import streamlit as st
import pandas as pd
import plotly.express as px

st.title("포항시 2024 지역별 대기통합지수 시각화")

uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 컬럼명 자동 매핑 (혹시 다를 경우 대비)
    rename_dict = {
        'region': '지역', '동': '지역', '읍면동': '지역', '위치': '지역',
        'index': '대기통합지수', '통합지수': '대기통합지수', '대기지수': '대기통합지수',
        'lat': '위도', 'latitude': '위도', '위도': '위도',
        'lon': '경도', 'lng': '경도', 'longitude': '경도', '경도': '경도'
    }
    df.rename(columns=rename_dict, inplace=True)

    required_columns = {'지역', '대기통합지수', '위도', '경도'}
    if not required_columns.issubset(df.columns):
        st.error(f"CSV에 {required_columns} 컬럼이 필요합니다. 현재 컬럼: {df.columns.tolist()}")
    else:
        st.dataframe(df)

        fig = px.scatter_mapbox(
            df,
            lat='위도',
            lon='경도',
            color='대기통합지수',
            size='대기통합지수',
            size_max=50,  # ← 원 크기를 크게 (기본 20 → 50)
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

