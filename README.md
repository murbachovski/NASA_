# 프로젝트 제목
```
NASA와 함께하는 우주 대탐험
```

# 프로젝트 설명
```
1. NASA에서 선정한 오늘의 우주 구경
2. 지구 셀카 관찰
3. 뜨거운 태양 관찰
4. 자외선 태양 4종 관찰
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
  <img src="https://github.com/user-attachments/assets/2946622e-d7e3-483a-b673-688b23229f69" width="700">
  
  <img src="https://github.com/user-attachments/assets/ea3e2851-2c8d-4239-94ae-bc3bf38d0f08" width="700">
  
  <img src="https://github.com/user-attachments/assets/0cea65ab-2a7e-4a21-a5af-f02c6c2e78f3" width="700">
  <img src="https://github.com/user-attachments/assets/84aff42c-45ff-4668-8f1e-bf437269b893" width="700">
  
  <img src="https://github.com/user-attachments/assets/52dd8971-08ff-4c3b-86ff-43116d30a761" width="700">
  <img src="https://github.com/user-attachments/assets/684cd8ae-e65c-4d2a-bbcf-9c635c35ffca" width="700">
  <img src="https://github.com/user-attachments/assets/4837a8d7-2617-4752-8821-1d9ef88f3676" width="700">
  <img src="https://github.com/user-attachments/assets/9f8c5bb9-cda8-4d81-82e4-798f2dac351e" width="700">
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
