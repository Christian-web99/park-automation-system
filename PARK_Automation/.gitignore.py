# ▒▒▒ Python 기본 무시 항목 ▒▒▒
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so

# ▒▒▒ Jupyter/IPython 체크포인트 ▒▒▒
.ipynb_checkpoints/

# ▒▒▒ macOS 시스템 파일 ▒▒▒
.DS_Store

# ▒▒▒ Visual Studio Code 설정 ▒▒▒
.vscode/

# ▒▒▒ 환경 변수 파일 (.env는 절대 업로드 금지) ▒▒▒
.env
.env.*

# ▒▒▒ 민감정보 및 로컬 키 파일 (config 키 정보) ▒▒▒
config/config_secret.py
config/keys.json

# ▒▒▒ 로그, 에러 기록 등 ▒▒▒
*.log
*.err
*.out

# ▒▒▒ 결과 저장용 / 분석결과 엑셀파일 등 ▒▒▒
*.xlsx
*.xls
*.csv
data/*.csv   # IPO CSV 등 실전 데이터는 깃허브에 직접 올릴 경우 삭제

# ▒▒▒ 모델 파일, 백테스트 결과 등 (미사용 시 무시) ▒▒▒
*.h5
*.pkl
*.joblib
*.pt

# ▒▒▒ 크롤링 캐시 등 ▒▒▒
.cache/
*.db
*.sqlite

# ▒▒▒ __init__ 보조용 빈 디렉토리 무시 ▒▒▒
*/__init__.pyc
*/__init__.pyo
*/__init__.pyd

# ▒▒▒ 테스트 전용 임시 파일 무시 ▒▒▒
test_*.py
*.test.py
tests/

# ▒▒▒ 사용자 설정 (API Key, Telegram 등 민감 정보) ▒▒▒
secret.json
tokens.json
telegram_config.yaml

# ▒▒▒ 기타 확장 자동화 시스템 연동 대비 ▒▒▒
*.env.local
settings.yaml
config.yaml
.envrc