# 프로젝트 제목
```
AladinGemini — Aladin API를 이용한 Gemini 책 추천 서비스
```

# 프로젝트 설명
```
AladinGemini는 읽고 싶은 책에 대한 키워드를 입력하면,
Aladin API를 통해서 책을 검색한 후 Google Gemini AI로 분석해 책을 추천
```

# 가상환경 설정
```
conda create -n aladin_reco python=3.9
```

# API_KEY 설정
```
export ALADIN_TTBKEY=""
export GENAI_API_KEY=""
```

# 라이브러리 설치
```
pip install -r requirements.txt
```

# 앱 실행
```
./run.sh
```

# 웹 구성
<p align="center">
  <img src="" width="700">
</p>

# Ngrok
(로컬 서버 => 공개 서버로 전환)
```
<Mac M1 설치 기준>
https://ngrok.com/downloads/mac-os
brew install ngrok
ngrok config add-authtoken <token>
ngrok http 80
```

# Ngrok log
<p align="center">
  <img src="https://github.com/user-attachments/assets/5ca755c3-d8f8-4088-b3b4-1b735945d351" width="700">
</p>

# Ngrok(공개 서버 접속)
[Ngrok 공개 서버 접속](https://c83c0967a9dd.ngrok-free.app/)<br>

# Ngrok 참고 문서
[위키독스](https://cordcat.tistory.com/105)<br>

# Make requirements.txt
```
pip install pipreqs
```

# pipreqs 참고 문서
[PyPI pipreqs](https://pypi.org/project/pipreqs/)<br>

# Gemini 참고 문서
[위키독스](https://wikidocs.net/254713)<br>

# NASA OpenAPI 참고 문서
[NASA](https://api.nasa.gov/)<br>
[NASA OpenAPI 안내](https://ssd-api.jpl.nasa.gov/doc/index.php)<br>
