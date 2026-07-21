from flask import Flask, render_template, abort

app = Flask(__name__)

# 드론 카드 데이터
drone_cards = [
    {
        "id": 1,
        "title": "드론 자격증, 꼭 있어야 할까?",
        "summary": "250g이 넘는 드론을 날리려면 무엇이 필요할까요?",
        "content": "250g을 초과하는 드론은 완구용이라도 무게와 용도에 따라 반드시 '무인동력비행장치 4종(온라인 교육)' 이상을 취득해야 합니다. 무면허 비행 시 과태료가 부과될 수 있으니 야외로 나가기 전에 꼭 확인하세요!"
    },
    {
        "id": 2,
        "title": "비행금지구역 확인하기",
        "summary": "아무 곳에서나 드론을 날리면 큰일 납니다!",
        "content": "우리나라 상공은 안보와 안전을 위해 원자력발전소 주변, 휴전선 인근, 서울 도심 일부 등 수많은 곳이 비행금지구역으로 지정되어 있습니다. '드론플라이' 또는 '원스탑 민원서비스' 앱을 통해 비행 전 반드시 허가지역인지 확인하는 습관이 중요합니다."
    },
    {
        "id": 3,
        "title": "멋진 항공 샷 찍는 꿀팁",
        "summary": "영화 같은 풍경을 담고 싶다면?",
        "content": "항공 촬영의 핵심은 '빛'과 '수평'입니다. 해가 지기 직전 1시간인 '골든 아워'를 노리면 그림자가 부드러워져 훨씬 감성적인 결과물을 얻을 수 있습니다. 또한 짐벌 틸트각을 살짝 낮추어 지평선과 풍경이 조화롭게 담기도록 구도를 잡아보세요."
    }
]

@app.route('/')
def index():
    return render_template('index.html', cards=drone_cards)

@app.route('/card/<int:card_id>')
def card_detail(card_id):
    selected_card = next((card for card in drone_cards if card["id"] == card_id), None)
    if selected_card is None:
        abort(404)
    return render_template('detail.html', card=selected_card)

if __name__ == '__main__':
    app.run(debug=True)