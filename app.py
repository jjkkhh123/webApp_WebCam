from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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

    # 파일 업로드 처리
    photo = request.files.get('photo')
    photo_filename = ''
    if photo and photo.filename:
        photo_filename = 이름 + '_' + photo.filename
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo_filename)
        photo.save(photo_path)

    # addbook.txt 파일에 CSV 형식으로 저장 (사진 파일명도 저장)
    with open('addbook.txt', 'a', newline='', encoding='utf-8') as 파일:
        작성자 = csv.writer(파일)
        작성자.writerow([이름, 전화번호, 생일, photo_filename])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)