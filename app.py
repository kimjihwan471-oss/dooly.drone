from flask import Flask, render_template

app = Flask(__name__)

# 카드에 들어갈 드론 정보 데이터 (나중에 이 내용을 풍성하게 채우면 됩니다!)
drone_cards = [
    {
        "id": 1,
        "title": "드론 자격증, 꼭 있어야 할까?",
        "front_desc": "250g이 넘는 드론을 날리려면 무엇이 필요할까요?",
        "back_desc": "250g 초과 기체는 완구용이라도 무게와 용도에 따라 '무인동력비행장치 4종(온라인 교육)' 이상 취득이 필수입니다!"
    },
    {
        "id": 2,
        "title": "비행금지구역 확인하기",
        "front_desc": "아무 곳에서나 드론을 날리면 큰일 납니다!",
        "back_desc": "원스탑(One-Stop) 민원서비스나 드론 플라이 앱을 통해 비행 허가 구역인지 반드시 사전 확인해야 합니다."
    },
    {
        "id": 3,
        "title": "멋진 항공 샷 찍는 꿀팁",
        "front_desc": "영화 같은 풍경을 담고 싶다면?",
        "back_desc": "수평을 맞추는 짐벌 조작과 일몰 1시간 전인 '골든 아워'를 노려보세요. 감탄이 나오는 결과물을 얻을 수 있습니다."
    }
]

@app.route('/')
def index():
    return render_template('index.html', cards=drone_cards)

if __name__ == '__main__':
    app.run(debug=True)