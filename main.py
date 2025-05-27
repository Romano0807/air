import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 설정
st.set_page_config(layout="wide")
st.title("포항시 2024 지역별 대기통합지수 지도 시각화")

# GitHub에 있는 CSV 데이터 불러오기
csv_url = "https://raw.githubusercontent.com/사용자명/저장소명/브랜치명/포항시_2024_지역별_대기통합지수_가상_예시.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    rename_dict = {
        'region': '지역', '동': '지역', '읍면동': '지역', '위치': '지역',
        'index': '대기통합지수', '통합지수': '대기통합지수', '대기지수': '대기통합지수',
        'lat': '위도', 'latitude': '위도', '위도': '위도',
        'lon': '경도', 'lng': '경도', 'longitude': '경도', '경도': '경도'
    }
    df.rename(columns=rename_dict, inplace=True)
    return df[['지역', '대기통합지수', '위도', '경도']]

# 데이터 불러오기
df = load_data(csv_url)

# 데이터 확인
st.dataframe(df)

# 지도 시각화
fig = px.scatter_mapbox(
    df,
    lat="위도",
    lon="경도",
    color="대기통합지수",
    size="대기통합지수",
    hover_name="지역",
    hover_data={"위도": False, "경도": False, "대기통합지수": True},
    color_continuous_scale="RdYlGn_r",
    size_max=15,
    zoom=11,
    height=700
)

fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)
