# EXIF 복사기

## 설치 환경 및 방법

- 설치 환경

  - Windows and Linux

  - Python 3

- 설치 방법

  - [Python 3](https://www.python.org/downloads/)

    - (Windows) 설치 중간에 나오는 `Add to PATH` 체크 필수!

  - [ExifTool by Phil Harvey](https://exiftool.org/)

    - (Windows) Windows Executable: exiftool-xx.xx.zip 을 다운로드!

- 실행 준비

  1. exiftool 디렉터리 생성

  2. `exiftool` or (`exiftool.exe`) exiftool 디렉터리 안에 옮겨두기

    - (Windows) 다운로드 받으면 `exiftool(-k).exe` 일텐데, 파일 이름을 `exiftool.exe` 로 변경해야 함!

## 입출력

- 입력: `input.csv`

  - Fieldnames: `ImagePath,GPSAltitude,GPSLatitude,GPSLongitude,FlightRollDegree,FlightYawDegree,FlightPitchD
egree`

  - Rows 개수 원하는 만큼 적어도 됨

  - `ImagePath`는 프로그램 위치를 기준으로 상대 경로 가능

- 실행

  - (Windows) 쉬프트 + 오른쪽 클릭 => 여기에 PowerShell 창 열기

  - `python3 main.py` or (Windows: `python main.py`)

- 출력: output 디렉터리

## Created by

- Hyunsu Mun (munhyunsu@cs-cnu.org)

