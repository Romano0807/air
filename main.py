import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 기본 설정
st.set_page_config(layout="wide")
st.title("📍 포항시 2024 지역별 대기통합지수 지도 시각화")

# GitHub 원본 CSV URL (파일명은 영문으로 변경한 것)
csv_url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/pohang_air_index_2024.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)

    # 컬럼명 표준화 (자동 매핑)
    rename_dict = {
        'region': '지역', '동': '지역', '읍면동': '지역', '위치': '지역',
        'index': '대기통합지수', '통합지수': '대기통합지수', '대기지수': '대기통합지수',
        'lat': '위도', 'latitude': '위도', '위도': '위도',
        'lon': '경도', 'lng': '경도', 'longitude': '경도', '경도': '경도'
    }
    df.rename(columns=rename_dict, inplace=True)

    # 필수 컬럼만 추출
    return df[['지역', '대기통합지수', '위도', '경도']]

# 데이터 불러오기
df = load_data(csv_url)

# 데이터 확인용 테이블
st.subheader("📊 데이터 미리보기")
st.dataframe(df)

# 지도 시각화
st.subheader("🗺️ 대기통합지수 지도")
fig = px.scatter_mapbox(
    df,
    lat="위도",
    lon="경도",
    color="대기통합지수",
    size="대기통합지수",
    hover_name="지역",
    hover_data={"대기통합지수": True, "위도": False, "경도": False},
    color_continuous_scale="RdYlGn_r",
    size_max=20,
    zoom=11,
    height=700
)

fig.update_layout(
    mapbox_style="carto-positron",
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)

st.plotly_chart(fig, use_container_width=True)

