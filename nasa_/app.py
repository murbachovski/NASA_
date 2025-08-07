import requests
import googletrans
import subprocess
import streamlit as st

NASA_KEY = "8wIzaSGsNEToB8VowCX1ae9VFXjT2NANOp6sOZuS"

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
    st.title("🚀 NASA 탐험")

    if st.button("오늘의 우주 보기"):
        title, date, explanation, url = get_apod(api_key=NASA_KEY)
        explanation_kor = google_trans_eng_ko(explanation)
        title_kor = google_trans_eng_ko(title)
        st.image(url, caption=title, use_container_width=True)
        # st.image(url, caption=f"{title}\n{title_kor}", use_container_width=True)
        st.markdown(f"**📅 날짜:** {date}")
        st.markdown(f"**📝 설명 (영어):**\n\n{explanation}")
        st.markdown(f"**📝 설명 (한국어):**\n\n{explanation_kor}")
        st.markdown(f"[🔗 원본 링크 바로가기]({url})")
