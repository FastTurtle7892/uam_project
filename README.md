# 🚁 UAM 실시간 위치 관제 시스템 (UAM Real-time Location Monitoring System)

## 📌 프로젝트 소개
본 프로젝트는 **SDR(Software Defined Radio) 장비와 GNU Radio를 활용한 무선 통신 기반의 드론/UAM(도심항공교통) 실시간 위치 관제 시스템**입니다. 
무선으로 송수신되는 GPS(위도, 경도) 데이터를 디코딩하여 데이터베이스에 적재하고, 이를 WebSocket 기반의 웹 서버를 통해 클라이언트로 전송하여 카카오맵(Kakao Maps API) 상에 실시간 이동 경로를 시각화합니다.

## 🛠 기술 스택 (Tech Stack)
- **Communication / Hardware:** SDR (Software Defined Radio), GNU Radio, USRP
- **Backend:** Python, Flask, Flask-SocketIO, SQLite
- **Frontend:** HTML, JavaScript, Kakao Maps API
- **Data Visualization & Analysis:** MATLAB, Jupyter Notebook (Folium)

## 📂 폴더 구조 (Directory Structure)
```text
uam_project/
│
├── database/                     # 백엔드 서버 및 데이터베이스 관련 파일
│   ├── templates/                
│   │   └── test.html             # [Frontend] 실시간 위치 관제 웹 페이지 (Kakao Maps API 연동)
│   ├── test_07_13.py             # [Backend] Flask 및 Socket.IO 기반 실시간 스트리밍 웹 서버
│   ├── test_07_29.py             # [DB] GPS 데이터 수신 및 SQLite/MySQL 데이터베이스 저장 로직
│   ├── gps.db / test_gps.db      # [DB] 수신된 GPS 좌표(LAT, LON)가 저장되는 SQLite DB 파일
│   ├── mapDatabaseData.m         # [Analysis] MATLAB을 활용한 위치 데이터 정적 시각화 스크립트
│   └── .ipynb_checkpoints/       # Jupyter Notebook 데이터 분석 관련 파일 (Folium 활용 등)
│
├── uam_gnu_file/                 # 무선 통신 및 데이터 송수신 (GNU Radio) 관련 파일
│   ├── pkt_rcv_strip.grc / .py   # [RX] 수신된 무선 패킷 디코딩 및 Base64 변환 로직
│   ├── pkt_rcv_strip_epy_block_0.py # [RX] 패킷 Preamble 분석 및 유효 데이터 추출 커스텀 블록
│   ├── xmt_rcv_switch.grc / .py  # [TX/RX] 송수신 상태 전환 제어 (안테나 스위치 및 LED)
│   ├── xmt_rcv_switch_epy_block_0.py# [TX/RX] 스위치 제어 로직 커스텀 블록
│   └── experiment_result/        # 실험 결과 로그 데이터 (.tmp 파일)
│
└── README.md                     # 프로젝트 설명서 (현재 파일)
```

## 🚀 주요 기능 (Key Features)

1. **SDR 기반 무선 데이터 수신 및 전처리**
   - GNU Radio를 활용하여 하드웨어(USRP)로부터 무선 신호를 수신합니다.
   - Preamble 분석을 통해 유효 패킷을 추출하고, Base64 디코딩을 수행하여 원본 GPS 데이터를 확보합니다.

2. **실시간 데이터베이스 적재 파이프라인**
   - 수신 및 디코딩된 GPS 데이터를 SQLite 데이터베이스에 지속적으로 저장하여 데이터 무결성을 유지합니다.

3. **WebSocket 기반 실시간 스트리밍 서버 구축**
   - Python Flask 및 Socket.IO를 활용하여 서버-클라이언트 간 양방향 통신 환경을 구축했습니다.
   - DB에 저장된 최신 위치 데이터를 1초 주기로 웹 클라이언트에게 브로드캐스트합니다.

4. **웹 기반 실시간 관제 대시보드 (Frontend)**
   - 카카오맵 API(Kakao Maps API)를 연동하여 수신된 좌표에 마커를 생성합니다.
   - 이전 위치와 현재 위치를 Polyline(선)으로 연결하여 드론/UAM의 이동 궤적을 실시간으로 렌더링합니다.

## ⚙️ 실행 방법 (How to Run)

*(※ 해당 프로젝트는 USRP 등 특정 하드웨어 환경 및 데이터베이스 세팅이 필요할 수 있습니다.)*

1. **무선 데이터 수신부 실행 (GNU Radio)**
   - `uam_gnu_file/` 디렉토리 내의 GNU Radio 블록(`pkt_rcv_strip.py`, `xmt_rcv_switch.py`)을 실행하여 데이터 수신 및 디코딩을 시작합니다.

2. **백엔드 서버 및 DB 로직 실행**
   - 데이터베이스 적재 실행: `python database/test_07_29.py`
   - 실시간 스트리밍 웹 서버 실행: `python database/test_07_13.py`

3. **관제 대시보드 확인**
   - 브라우저를 통해 `http://localhost:5000` (또는 설정된 포트)에 접속하여 실시간으로 이동하는 위치(`test.html`)를 확인합니다.
