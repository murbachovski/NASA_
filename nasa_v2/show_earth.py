# show_earth_module.py

import requests

def get_latest_earth_image_data():
    """
    DSCOVR: EPIC API에서 최신 '자연색' 지구 이미지 데이터와 캡션을 가져와 반환합니다.
    파일로 저장하지 않고, 데이터를 직접 return합니다.
    
    Returns:
        tuple: (이미지 데이터(bytes), 캡션(str)) 또는 에러 시 (None, None)
    """
    try:
        # 1단계: 메타데이터 요청
        api_url = "https://epic.gsfc.nasa.gov/api/natural"
        response = requests.get(api_url)
        response.raise_for_status()
        
        image_data = response.json()
        if not image_data:
            return None, None

        # 2단계: 정보 파싱
        latest_image_meta = image_data[0]
        image_name = latest_image_meta['image']
        caption = latest_image_meta['caption'] # 캡션 정보 추가
        date_str = latest_image_meta['date']
        
        year, month, day = date_str.split(' ')[0].split('-')
        
        # 3단계: 이미지 다운로드 URL 구성 및 데이터 요청
        archive_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
        
        image_response = requests.get(archive_url)
        image_response.raise_for_status()
        
        # 4단계: 이미지 데이터(bytes)와 캡션을 반환
        return image_response.content, caption

    except requests.exceptions.RequestException as e:
        print(f"[모듈 오류] 요청 중 오류가 발생했습니다: {e}")
        return None, None
    except (KeyError, IndexError) as e:
        print(f"[모듈 오류] 수신된 데이터의 형식이 예상과 다릅니다: {e}")
        return None, None

if __name__ == "__main__":
    print(get_latest_earth_image_data())