# webApp_WebCam

## 📌 목차
- [1. 소개](#1-소개)
- [2. 설치 방법 및 주요 코드 설명](#2-설치-방법-및-주요-코드-설명)
- [3. 사용법 및 실행 장면](#3-사용법-및-실행-장면)
- [4. 추가된 기능](#4-추가된-기능)

---

## 1. 소개
가상환경을 만들고 Flask를 이용해 이름과 전화번호와 생일을 입력받아 addbook.txt 파일에 CSV 형식으로 저장하는 간단한 웹 애플리케이션 코드입니다. HTML 템플릿도 함께 포함되어 있습니다. 추가로 사진을 선택하면 미리보기로 보여준 후 업로드를 하면 서버에 사진이 저장되며 addbook.txt에 이름 전화번호 생일 사진이름 이 저장하도록 구현하였습니다.    
이전의 webApp_base와 대부분 비슷합니다. (따라서 추가된 기능만 보고자 하시는 분들은 위의 4번 메뉴를 클릭하여 주세요.)

## 2. 설치 방법 및 주요 코드 설명 
이전의 webApp_base와 대부분 비슷합니다.
2.1 Flask 프레임워크 설치 
```
pip install flask
```
<br><br><br>
2.2 주요 코드 설명 
app.py
아래의 코드를 위에서 부터 하나씩 살펴보자면 
주소에 /로 끝나면 template에 있는 index.html을 불러옵니다. 
버튼을 누르면 /add를 주소 끝에 반환하게 되는데 그러면 이름 전화번호 생일을 request.form을 통해서 받아옵니다. 받아온 데이터를 addbook.txt에 저장을 합니다. 이 행동들을 마치면 주소를 /로 끝내게 하여 처음의 화면인 index.html이 화면에 보이게 됩니다.
```
# 홈 페이지 라우트
@app.route('/')
def index():
    return render_template('index.html')

# 폼 제출을 처리하는 라우트
@app.route('/add', methods=['POST'])
def add_contact():
    이름 = request.form['pyname']
    전화번호 = request.form['pyphone']
    생일 = request.form['pybirth']

    # addbook.txt 파일에 CSV 형식으로 저장
    with open('addbook.txt', 'a', newline='', encoding='utf-8') as 파일:
        작성자 = csv.writer(파일)
        작성자.writerow([이름, 전화번호,생일])

    return redirect('/')
```

index.html
index.html에 대해 살펴보겠습니다.    
먼저 html을 꾸미기 위하여 <head> 사이에 
```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```
<br> 위 코드를 넣었습니다. 위 코드는 static에 있는 style.css를 불러오는 코드입니다.

## 3. 사용법 및 실행 장면
cmd 창에 아래의 코드를 입력해줍니다. 코드를 실행할 때 현재 위치가 app.py가 있는 위치와 동일한지 확인해야 합니다. 
```
python app.py
```
<img src="https://github.com/jjkkhh123/webApp_base/blob/main/images/img1.png" alt="html 장면" width="500" height="500">
<img src="https://github.com/jjkkhh123/webApp_base/blob/main/images/img2.png" alt="html 장면" width="300" height="200">

## 4. 추가된 기능
webApp_base 와 비교하여 추가된 기능들
### 4.1 사진을 선택하면 미리보기로 보여준 후 업로드를 하면 서버에 사진이 저장되며 addbook.txt에 이름 전화번호 생일 사진이름이 저장.
### 4.2 웹캠을 클릭하여 사진을 업로드하는 대신에 웹캠으로 사진을 찍어서 서버에 저장.
<img src="https://github.com/jjkkhh123/webApp_WebCam/blob/main/static/images/img1.png" alt="html 장면1" width="500" height="500">
<img src="https://github.com/jjkkhh123/webApp_WebCam/blob/main/static/images/img2.png" alt="html 장면2" width="500" height="500">
<img src="https://github.com/jjkkhh123/webApp_WebCam/blob/main/static/images/img3.png" alt="html 장면3" width="500" height="500">
<img src="https://github.com/jjkkhh123/webApp_WebCam/blob/main/static/images/img4.png" alt="html 장면4" width="300" height="300">
