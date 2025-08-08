import requests
import os
from datetime import datetime

def fetch_latest_eit304_image():
    """
    SOHO 위성이 촬영한 EIT_304 타입의 가장 최신 이미지를 다운로드하고, 이미지 바이트를 반환합니다.
    """
    image_name = "EIT_304"
    image_url = "https://soho.nascom.nasa.gov/data/realtime/eit_304/1024/latest.jpg"

    try:
        response = requests.get(image_url)
        response.raise_for_status()  # 예외 발생 (상태 코드가 200이 아닐 경우)

        # 바이트 데이터를 반환
        return response.content

    except requests.exceptions.RequestException as e:
        print(f"[오류] 이미지 다운로드 실패: {e}")
        return None
