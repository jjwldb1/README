import streamlit as st
import pandas as pd
from analyzer import classify, analyze

st.title("경쟁자 분석기")

keyword = st.text_input("검색 키워드 입력")

if st.button("분석 실행"):
    if keyword == "":
        st.warning("키워드를 입력하세요")
    else:
        # 현재는 테스트용 데이터
        sample_data = [
            {"title": "AI 얼굴 분석 서비스", "desc": "AI로 얼굴 분석 후 추천"},
            {"title": "성형 상담 컨설팅", "desc": "전문의 상담 기반 추천"},
            {"title": "크몽 얼굴 분석", "desc": "얼굴형 분석 리포트 제공"}
        ]

        results = []

        for item in sample_data:
            t = classify(item["desc"])
            s = analyze(item["desc"])

            results.append({
                "제목": item["title"],
                "유형": t,
                "전략": s
            })

        df = pd.DataFrame(results)
        st.write(df)

        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("CSV 다운로드", csv, "result.csv")
