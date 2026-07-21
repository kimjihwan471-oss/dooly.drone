import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>드론 총정리 대시보드</title>
        <style>
            :root { --bg-color: #f0f2f5; --text-color: #333333; --card-bg: #ffffff; --card-border: #1a73e8; --header-desc: #666666; --input-bg: #ffffff; --input-border: #cbd5e1; }
            [data-theme="dark"] { --bg-color: #121212; --text-color: #e0e0e0; --card-bg: #1e1e1e; --card-border: #8ab4f8; --header-desc: #aaaaaa; --input-bg: #2d2d2d; --input-border: #444444; }
            body { font-family: 'Malgun Gothic', sans-serif; background-color: var(--bg-color); margin: 0; padding: 40px; color: var(--text-color); transition: background-color 0.3s, color 0.3s; }
            .header { text-align: center; margin-bottom: 30px; position: relative; }
            .header h1 { color: #1a73e8; font-size: 32px; margin-bottom: 10px; }
            .theme-toggle-btn { position: absolute; top: 0; right: 20px; background: var(--card-bg); color: var(--text-color); border: 2px solid var(--input-border); padding: 10px 15px; border-radius: 50px; cursor: pointer; font-weight: bold; }
            .dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; max-width: 1100px; margin: 0 auto; }
            .card { background: var(--card-bg); padding: 40px 30px; border-radius: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 5px solid var(--card-border); text-align: center; text-decoration: none; display: block; transition: transform 0.2s; }
            .card:hover { transform: translateY(-5px); }
            .card h2 { color: var(--text-color); font-size: 22px; margin: 0; }
            .card p { color: var(--header-desc); font-size: 14px; margin-top: 10px; }
        </style>
    </head>
    <body data-theme="light">
        <div class="header">
            <button class="theme-toggle-btn" onclick="toggleTheme()">🌙 다크모드</button>
            <h1>🚁 드론 총정리 대시보드</h1>
            <p>아래 카드를 클릭하여 드론의 정의와 역사를 확인하세요!</p>
        </div>

        <div class="dashboard-grid">
            <a href="/detail/1" class="card">
                <h2>📌 1. 정의와 역사</h2>
                <p>무인항공기의 개념과 상세한 발전 연혁 확인하기</p>
            </a>
        </div>

        <script>
            function toggleTheme() {
                const body = document.body;
                const btn = document.querySelector('.theme-toggle-btn');
                if (body.getAttribute('data-theme') === 'light') {
                    body.setAttribute('data-theme', 'dark');
                    btn.innerHTML = '☀️ 라이트모드';
                } else {
                    body.setAttribute('data-theme', 'light');
                    btn.innerHTML = '🌙 다크모드';
                }
            }
        </script>
    </body>
    </html>
    '''

@app.route('/detail/1')
def detail_1():
    return '''
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>1. 정의와 역사</title>
        <style>
            body { font-family: 'Malgun Gothic', sans-serif; background-color: #f0f2f5; margin: 0; padding: 40px; color: #333; }
            .container { max-width: 900px; margin: 0 auto; background: #fff; padding: 40px; border-radius: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
            .back-btn { display: inline-block; margin-bottom: 25px; background-color: #e2e8f0; color: #333; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: bold; }
            .back-btn:hover { background-color: #cbd5e1; }
            h1 { color: #1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom: 15px; }
            h2 { color: #333; margin-top: 30px; border-left: 4px solid #1a73e8; padding-left: 10px; }
            p, li { line-height: 1.8; font-size: 15px; }
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-btn">← 메인으로 돌아가기</a>
            <h1>📌 1. 정의와 역사</h1>
            
            <h2>드론의 정의</h2>
            <p>조종사가 탑승하지 않고 무선전파의 유도에 의해서 자율 또는 원격으로 비행할 수 있는 무인항공기(UAV, Unmanned Aerial Vehicle)를 통칭합니다.</p>
            
            <h2>드론의 상세 발전 연혁</h2>
            <ul>
                <li><strong>기원 및 군사적 도입 (1910년대 ~ 1940년대):</strong> 1차 세계대전 시기 영국과 미국에서 무인 표적기를 개발하면서 처음 시작되었습니다.</li>
                <li><strong>군사 기술의 고도화 (1950년대 ~ 1990년대):</strong> 위성항법시스템(GPS)과 통신 기술이 접목되면서 정밀 정찰용 무인기로 발전했습니다.</li>
                <li><strong>민수용 및 상업용 개방 (2000년대 ~ 2010년대 초):</strong> 스마트폰 부품 기술의 발전으로 초소형 센서와 고효율 배터리가 상용화되면서 일반 촬영용 드론 시장이 열렸습니다.</li>
                <li><strong>4차 산업혁명과 자율주행 시대 (2015년대 ~ 현재):</strong> 인공지능(AI), 5G 통신과 결합하여 물류 배송, 스마트팜, 재난 구조 등 핵심 산업 인프라로 자리 잡았습니다.</li>
            </ul>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)