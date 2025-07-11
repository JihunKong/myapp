# app.py
import streamlit as st
import time
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="네이버 시계",
    page_icon="🕒",
    layout="centered"
)

# 스타일 적용
st.markdown("""
    <style>
    .clock-container {
        font-size: 80px;
        font-weight: bold;
        color: #2DB400;
        text-align: center;
        margin-top: 50px;
    }
    .date-container {
        font-size: 30px;
        color: #444;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 시간 표시
placeholder = st.empty()

while True:
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%Y년 %m월 %d일 %A")

    with placeholder.container():
        st.markdown(f"<div class='date-container'>{date_str}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='clock-container'>{time_str}</div>", unsafe_allow_html=True)

    time.sleep(1)
    # Streamlit reruns script automatically on each change. Loop just for clarity.
