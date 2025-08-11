import requests
import googletrans
import streamlit as st

NASA_KEY = ""


def get_apod(api_key="DEMO_KEY"):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("title"),
            "date": data.get("date"),
            "explanation": data.get("explanation"),
            "url": data.get("url"),
            "hdurl": data.get("hdurl"),
            "media_type": data.get("media_type")
        }
    else:
        return None

def google_trans_eng_ko(text):
    translator = googletrans.Translator()
    translated = translator.translate(text, dest='ko')
    return translated.text

st.title("🚀 NASA 탐험")

if st.button("오늘의 우주 보기"):
    apod_data = get_apod(api_key=NASA_KEY)

    if apod_data is None:
        st.error("NASA API 요청 실패!")
    else:
        explanation_kor = google_trans_eng_ko(apod_data["explanation"])
        title_kor = google_trans_eng_ko(apod_data["title"])

        # 미디어 URL 선택 (hdurl 우선, 없으면 url)
        media_url = apod_data.get("hdurl") or apod_data.get("url")

        # 미디어 타입에 따라 처리
        if apod_data["media_type"] == "image" and media_url:
            st.image(media_url, caption=apod_data["title"], use_container_width=True)
        elif apod_data["media_type"] == "video" and media_url:
            st.video(media_url)
        else:
            st.warning("오늘 자료는 공식 사이트에서 확인해주세요.")
            if media_url:
                st.markdown(f"[🔗 원본 링크 바로가기]({media_url})")
            else:
                # 링크도 없으면 APOD 공식 페이지 링크 안내
                apod_official_url = f"https://apod.nasa.gov/apod/ap{apod_data['date'].replace('-', '')}.html"
                st.markdown(f"[🔗 APOD 공식 페이지 바로가기]({apod_official_url})")

        st.markdown(f"**📅 날짜:** {apod_data['date']}")
        st.markdown(f"**📝 설명 (영어):**\n\n{apod_data['explanation']}")
        st.markdown(f"**📝 설명 (한국어):**\n\n{explanation_kor}")
        st.markdown(f"**제목 (한글):** {title_kor}")
