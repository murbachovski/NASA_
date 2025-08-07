# 프로젝트 제목
```
NASA 대탐험
```

# 프로젝트 설명
```
NASA API를 활용하여 오늘 우주 관찰
```

# 가상환경 설정
```
conda create -n nasa_gem python=3.9
```

# API_KEY 설정
```
export NASA_KEY=""
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
  <img src="https://github.com/user-attachments/assets/dceafa25-c230-4f13-8e58-8a468ac0acb8" width="700">
  ---
  <img src="https://github.com/user-attachments/assets/ae5755ea-8b1a-4d1d-82a5-23c13f373e8d" width="700">
  ---
  <img src="https://github.com/user-attachments/assets/eb7636e4-e40a-4737-b46f-45710ea81a1a" width="700">
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
