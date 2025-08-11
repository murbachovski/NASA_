import requests
import googletrans
import subprocess
import streamlit as st
import time
import os
from show_earth import get_latest_earth_image_data
from show_sun import fetch_latest_eit304_image

# 환경변수에서 API 키 불러오기
NASA_KEY = os.getenv("NASA_API_KEY")

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

def download_image(url, filename="show.jpg"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image save as {filename}")
    else:
        print("Failed to download image")
    return filename

def show_image_imgcat(filename):
    try:
        subprocess.run(["imgcat", filename], check=True)
    except FileNotFoundError:
        print("imgcat 명령어를 찾을 수 없습니다. iTerm2에서 실행 중인지 확인하세요.")
    except subprocess.CalledProcessError as e:
        print(f"imgcat 실행 중 오류 발생: {e}")

def google_trans_eng_ko(sentence_kor):
    translator = googletrans.Translator()
    result = translator.translate(sentence_kor, dest='ko')
    return result.text

def fetch_soho_image(wavelength: str) -> bytes:
    """
    SOHO 자외선 이미지 중 특정 파장(wavelength)의 최신 이미지를 반환.
    - wavelength: 'eit_171', 'eit_195', 'eit_284', 'eit_304'
    """
    url = f"https://soho.nascom.nasa.gov/data/realtime/{wavelength}/1024/latest.jpg"
    response = requests.get(url)
    return response.content if response.status_code == 200 else None

st.title("🚀 NASA와 함께하는 우주 대탐험")

st.divider()

if st.button("NASA에서 선정한 오늘의 우주", icon="✨"):
    progress = st.progress(0)  # 0%부터 시작

    progress.progress(10)
    apod_data = get_apod(api_key=NASA_KEY)

    if apod_data is None:
        progress.empty()
        st.error("NASA API 요청 실패!")
    else:
        progress.progress(50)
        explanation_kor = google_trans_eng_ko(apod_data["explanation"])
        title_kor = google_trans_eng_ko(apod_data["title"])
        progress.progress(100)
        time.sleep(0.3)
        progress.empty()

        media_url = apod_data.get("hdurl") or apod_data.get("url")

        if apod_data["media_type"] == "image" and media_url:
            st.image(media_url, caption=apod_data["title"], use_container_width=True)
        elif apod_data["media_type"] == "video" and media_url:
            st.video(media_url)
        else:
            st.warning("오늘 자료에는 표시 가능한 이미지나 영상이 없습니다.")
            if media_url:
                st.markdown(f"[🔗 원본 링크 바로가기]({media_url})")
            else:
                apod_official_url = f"https://apod.nasa.gov/apod/ap{apod_data['date'].replace('-', '')}.html"
                st.markdown(f"[🔗 APOD 공식 페이지 바로가기]({apod_official_url})")

        st.markdown(f"**📅 날짜:** {apod_data['date']}")
        st.markdown(f"**📝 설명 (영어):**\n\n{apod_data['explanation']}")
        st.markdown(f"**📝 설명 (한국어):**\n\n{explanation_kor}")
        st.markdown(f"**제목 (한글):** {title_kor}")

st.divider()

if st.button("지구 셀카 보기", icon="🌍"):
    with st.spinner("NASA 서버에서 최신 이미지를 가져오는 중입니다..."):
        image_bytes, caption_text = get_latest_earth_image_data()

    if image_bytes:
        st.success("짜잔! 최신 지구 사진을 성공적으로 가져왔습니다.")
        st.image(image_bytes, caption=f"캡션: {caption_text}")
        st.info("이 이미지는 계속 업데이트되고 있습니다.")
    else:
        st.error("이미지를 가져오는 데 실패했습니다. 잠시 후 다시 시도해주세요.")

st.divider()

if st.button("뜨거운 태양", icon='☀️', key="sun_button"):
    image_bytes = fetch_latest_eit304_image()

    if image_bytes:
        st.image(image_bytes, caption="태양 최신 이미지")
    else:
        st.error("이미지를 가져오는 데 실패했습니다.")

st.divider()

if st.button("자외선 태양 4종", icon="🌞"):
    wavelengths = ['eit_171', 'eit_195', 'eit_284', 'eit_304']
    captions = ['EIT 171', 'EIT 195', 'EIT 284', 'EIT 304']

    cols = st.columns(4)

    for i in range(4):
        image = fetch_soho_image(wavelengths[i])
        if image:
            cols[i].image(image, caption=captions[i], use_container_width=True)
        else:
            cols[i].error("이미지를 불러오지 못했습니다.")
