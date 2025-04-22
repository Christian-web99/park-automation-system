# 🧠 PARK 자동화 시스템 – 주식·암호화폐 시장 완전 자동 감시

> KOSPI / KOSDAQ / Crypto / Macro / ETF / 인물 발언 / 위기 감지  
> 실시간 + 오전 7시 요약 알림 기반 / 총 27가지 자동화 항목 운영

---

## 🚀 시스템 개요

본 시스템은 시장 전반의 기술적 지표, 수급 흐름, ETF, 경제 이벤트, 거시지표, 위기 요인까지 자동 감지합니다.  
설정된 조건을 만족할 경우 실시간 또는 오전 7시에 **텔레그램 메시지**로 자동 알림을 전송합니다.

---

## 🗂️ 프로젝트 구조

```
park-automation-system/
├── main.py                    # 전체 실행 메인 (실시간/요약 통합)
├── main_7am.py                # 오전 7시 요약 알림 전용
├── main_realtime.py           # 5분/1시간 실시간 감시 전용
├── main_critical_realtime.py  # 1분 간격 초실시간 감시 (전쟁/발언 등)
├── telegram_handler.py        # 텔레그램 메시지 전송 함수
├── park_alerts.py             # 27개 알림 항목 실행 트리거
├── config.py                  # API 키, 경로, 설정 정보
├── requirements.txt           # Python 패키지 목록
├── env_sample                 # API 키 템플릿 (.env)
├── README.md                  # 설명 파일
│
├── services/
│   ├── fetch_market_data.py     # 외부 API 데이터 수집
│   ├── fetch_ipo_dart.py        # DART 신규상장주 크롤링
│   ├── fetch_ipo_list.py        # IPO 마스터 파일 업데이트
│   ├── schedule/                # (예약 기능 확장 가능)
│   └── __init__.py
│
└── modules/
    ├── alerts/                  # 환율, 기술지표 등
    ├── ema/
    ├── ipo/
    ├── flows/
    ├── weekly/
    ├── holdings/
    ├── etf/
    ├── people/
    ├── calendar/
    ├── crisis/
    ├── macro/
    ├── economy/
    └── sentiment/
```

---

## 🔑 API 설정 방법

1. `config.py` 또는 `.env.sample` 파일을 참고하여 아래 키를 등록하세요.

| 이름 | 사용 목적 | 필요 여부 |
|------|-----------|------------|
| `FRED_API_KEY` | 미국 금리, 경기지표 | ✅ |
| `ALPHA_VANTAGE_API_KEY` | 환율 | ✅ |
| `COINMARKETCAP_API_KEY` | 비트코인 ETF | ✅ |
| `NEWS_API_KEY` | 위기 뉴스 | ✅ |
| `TWITTER_BEARER_TOKEN` | 인물 발언 수집 | ✅ |
| `INVESTING_API_KEY` | VIX, 글로벌 지수 | ✅ |
| `OKX_API_KEY`, `OKX_SECRET_KEY`, `OKX_PASSPHRASE` | BTC 실시간 시세 | ✅ |
| `OPENWEATHER_API_KEY` | 이상기후 감지 | ✅ |
| `DART_API_KEY` | 신규상장 종목 자동 업데이트 | ✅ |

---

## 📌 주요 실행 방법

```bash
# 1. 오전 7시 요약 알림 실행 (크론에 등록 권장)
python main_7am.py

# 2. 실시간 감시 (5분, 1시간)
python main_realtime.py

# 3. 초실시간 감시 (1분 간격 전쟁/발언 등)
python main_critical_realtime.py
```

---

## 🧭 자동화 항목 요약 (총 27개)

| 번호 | 항목 | 주기 |
|------|------|------|
| 1~4 | 기술적 분석 (환율/보조지표/EMA/신규상장주) | 실시간 + 요약 |
| 5~11 | 수급 요약 (기관, 공매도, 야간선물, ETF, 블랙록 등) | 종가 후 or 실시간 |
| 12~14 | 발언 / 일정 / 위기 감지 | 1분 실시간 + 요약 |
| 15~19 | 거시지표 확장 (원자재, VIX, 실적 등) | 실시간 + 요약 |
| 20~26 | 전문가형 분석 (CDS, 정책발표 등) | 실시간 + 요약 |
| 27 | 시장 체온 요약 (CNN F&G, 버핏지수 등) | 오전 7시 요약 |

---

## 📬 텔레그램 설정

- `TELEGRAM_BOT_TOKEN`: 텔레그램 봇 생성 후 토큰 입력
- `TELEGRAM_CHAT_IDS`: 알림 수신할 대상자 ID 리스트

---

## ✅ 향후 확장 가능 항목

- 자동 매매 연동 (트레이딩뷰 Webhook)
- Slack, 이메일 등 다중 알림 채널
- 종목 선택 학습형 모델 탑재 (ex. ChatGPT API 연동)

---

> 함께 만들어가는 자동화 시스템 –  
> 실패를 반복하지 않도록, 시장을 **먼저 감지하고 먼저 움직인다.**