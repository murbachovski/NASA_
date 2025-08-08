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
        # print("Title:", data.get("title"))
        title = data.get("title")
        # print("Date:", data.get("date"))
        date = data.get("date")
        # print("Explanation:", data.get("explanation"))
        explanation = data.get("explanation")
        # print("Image URL:", data.get("url"))
        url = data.get("url")
        return title, date, explanation, url
    else:
        # print("Error:", response.status_code)
        return response.status_code

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
    result = result.text
    return result

def fetch_soho_image(wavelength: str) -> bytes:
    """
    SOHO 자외선 이미지 중 특정 파장(wavelength)의 최신 이미지를 반환.
    - wavelength: 'eit_171', 'eit_195', 'eit_284', 'eit_304'
    """
    url = f"https://soho.nascom.nasa.gov/data/realtime/{wavelength}/1024/latest.jpg"
    response = requests.get(url)
    return response.content if response.status_code == 200 else None

if __name__ == "__main__":
    nasa = get_apod(api_key=NASA_KEY)
    if isinstance(nasa, tuple):
        # title, date, explanation, url = nasa
        # explanation_kor = google_trans_eng_ko(explanation)
        # title_kor = google_trans_eng_ko(title)
        # print(f"Title      : {title}")
        # print(f"Title      : {title_kor}")
        # print(f"Date       : {date}")
        # print(f"Explanation:\n{explanation}\n")
        # print(f"Explanation_kor:\n{explanation_kor}\n")
        # print(f"Image URL  : {url}")
        # filename = download_image(url)
        # print(show_image(filename))
        print("SUCCESS")
    else:
        print(f"Error: Status code {nasa}")

################## STREAMLIT ##################
    st.title("🚀 NASA와 함께하는 우주 대탐험")

    st.divider() # 구분선x

    if st.button("NASA에서 선정한 오늘의 우주", icon="✨"):
        ### PROGRESSBAR
        progress = st.progress(0)  # 0%부터 시작
    
        # 10%: API 데이터 요청 시작
        progress.progress(10)
        title, date, explanation, url = get_apod(api_key=NASA_KEY)
        
        # 50%: 번역 중
        progress.progress(50)
        explanation_kor = google_trans_eng_ko(explanation)
        title_kor = google_trans_eng_ko(title)
        
        # 100%: 완료
        progress.progress(100)
        
        time.sleep(0.3)
        
        # 프로그래스바 제거
        progress.empty()

        title, date, explanation, url = get_apod(api_key=NASA_KEY)
        explanation_kor = google_trans_eng_ko(explanation)
        title_kor = google_trans_eng_ko(title)
        st.image(url, caption=title, use_container_width=True)
        # st.image(url, caption=f"{title}\n{title_kor}", use_container_width=True)
        st.markdown(f"**📅 날짜:** {date}")
        st.markdown(f"**📝 설명 (영어):**\n\n{explanation}")
        st.markdown(f"**📝 설명 (한국어):**\n\n{explanation_kor}")
        st.markdown(f"[🔗 원본 링크 바로가기]({url})")
    
    st.divider() # 구분선x

    # --- 2. 최신 지구 사진 (EPIC) ---
    # st.header("🌍 최신 지구 사진")
    if st.button("지구 셀카 보기", icon="🌍"):
        with st.spinner("NASA 서버에서 최신 이미지를 가져오는 중입니다..."):
            # 모듈의 함수를 호출하여 이미지 데이터와 캡션을 받음
            image_bytes, caption_text = get_latest_earth_image_data()

        # 성공적으로 데이터를 받아왔는지 확인
        if image_bytes:
            st.success("짜잔! 최신 지구 사진을 성공적으로 가져왔습니다.")
            # st.image()가 이미지 바이트를 직접 받아 화면에 렌더링
            st.image(
                image_bytes,
                caption=f"캡션: {caption_text}"
            )
            st.info("이 이미지는 계속 업데이트되고 있습니다.")
        else:
            st.error("이미지를 가져오는 데 실패했습니다. 잠시 후 다시 시도해주세요.")
            
    st.divider() # 구분선x
    
    # --- 태양 사진 탭 ---
    if st.button("뜨거운 태양", icon='☀️',key="sun_button"):
        image_bytes = fetch_latest_eit304_image()
        
        if image_bytes:
            st.image(image_bytes, caption="태양 최신 이미지")
        else:
            st.error("이미지를 가져오는 데 실패했습니다.")

    st.divider() # 구분선x
    # --- 태양 이미지 표시 버튼 ---
    if st.button("자외선 태양 4종", icon="🌞"):
        # 4개의 파장
        wavelengths = ['eit_171', 'eit_195', 'eit_284', 'eit_304']
        captions = ['EIT 171', 'EIT 195', 'EIT 284', 'EIT 304']
        
        # 4개 칼럼으로 나눔
        cols = st.columns(4)
        
        for i in range(4):
            image = fetch_soho_image(wavelengths[i])
            if image:
                # cols[i].image(image, caption=captions[i], use_column_width=True)
                cols[i].image(image, caption=captions[i], use_container_width=True)
            else:
                cols[i].error("이미지를 불러오지 못했습니다.")