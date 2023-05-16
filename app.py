# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.h7shnou.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


#더미데이터 초기화------
db.project_1.delete_many({})
keylist = ['id', 'title','image','day','price','reason','description','recommandCount','password']
dummy = [ 
                { keylist[0] : '1', keylist[1] : '최고급 자전거', keylist[2] : 'https://cdn.imweb.me/thumbnail/20210405/0886946ac6042.jpg', keylist[3] : '20240401', keylist[4]: '1000000', keylist[5] : '저는 빠른 속도를 즐깁니다', keylist[6] : '저는 라이딩을 즐겨합니다. 하지만 한번에 큰 돈을 쓸 수는 없는 상황이라 이렇게 조금씩 저금하면서 구매욕구를 불태우고 있습니다. 이 자전거는 저에게 특별합니다. 짜릿한 경험을 선사해줄꺼라고 기대합니다!', keylist[7] : 6, keylist[8] : '1' },
                { keylist[0] : '2', keylist[1] : '포르쉐 자동차', keylist[2] : 'https://files.porsche.com/filestore/news/korea/ko/2022-06-23/headimage1/86736c08-f2f4-11ec-80f3-005056bbdc38/porsche-%ED%8F%AC%EB%A5%B4%EC%89%90%EC%BD%94%EB%A6%AC%EC%95%84%2C-%EC%8B%A0%ED%98%95-%ED%8C%8C%EB%82%98%EB%A9%94%EB%9D%BC-%ED%84%B0%EB%B3%B4-S-E-%ED%95%98%EC%9D%B4%EB%B8%8C%EB%A6%AC%EB%93%9C-%EA%B5%AD%EB%82%B4-%EA%B3%B5%EC%8B%9D-%EC%B6%9C%EC%8B%9C.jpg', keylist[3] : '20300601', keylist[4]: '200000000', keylist[5] : '나의 로망 자동차', keylist[6] : '자동차한테 관심을 가지지 않았었는데 이 자동차를 도심에서 한번 보고 빠져들었어요, 꼭 구매해서 타고 다니고 싶어요', keylist[7] : 17, keylist[8] : '1' },                                            
                { keylist[0] : '3', keylist[1] : '컴퓨터', keylist[2] : 'https://mblogthumb-phinf.pstatic.net/MjAxODAzMzBfNjgg/MDAxNTIyMzgzMTU2MDg4.VgjVkfdLMsBvUpuwZzD4yikSN5zynPfoEnCDer2nZR4g.8slx5ptzdPMxt7YoPs2bwJGxq9IR-ezpx0xiUqI53KUg.JPEG.mypcstory/04.jpg?type=w800', keylist[3] : '20250401', keylist[4]: '1000000', keylist[5] : '게임하고싶어요', keylist[6] : '저는 게임을 좋아해요 하지만 집에는 10년된 컴퓨터밖에 없어요.. 알바를 하면서 꾸준히 저금하고있어요! 목표 기한까지는 반드시 구매할꺼에요', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '4', keylist[1] : '샤넬 가방', keylist[2] : 'https://image-cdn.trenbe.com/productmain/1662021697983-e517aa2d-38d0-4bec-a303-1bd604db1344.jpeg', keylist[3] : '20250401', keylist[4]: '5000000', keylist[5] : '한정판이라서', keylist[6] : '한정판 가방이라서 꼭 구하고싶네요', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '5', keylist[1] : '조던 신발', keylist[2] : 'https://visla.kr/wp/wp-content/uploads/2017/11/20171125_1.png', keylist[3] : '20990701', keylist[4]: '70000000', keylist[5] : '구매한다면 이것만 신고다닐겁니다.', keylist[6] : '조던의 팬입니다. 이 신발만 구할 수 있다면 뭐든지 하겠습니다.', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '6', keylist[1] : 'LP판', keylist[2] : 'https://www.mediapia.co.kr/news/photo/202007/44493_72799_5715.jpg', keylist[3] : '20400401', keylist[4]: '500000', keylist[5] : '감성적으로 음악듣기', keylist[6] : '요즘 LP판이 끌리네요 구매해서 테이블 위에 두고 사용하고싶네요', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '7', keylist[1] : '방송용 카메라', keylist[2] : 'https://mblogthumb-phinf.pstatic.net/20150619_200/dlek513_14346755524401Q9Hs_JPEG/3216_3847_1635.jpg?type=w2', keylist[3] : '20300401', keylist[4]: '1000000', keylist[5] : '영화감독이 꿈입니다.', keylist[6] : '카메라를 구매해서 저예산영화부터 만들어보고 싶어요 성공해서 좋은 카메라도 사고 싶어요 ', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '8', keylist[1] : '비행기 일등석', keylist[2] : 'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202103/12/4b490c08-bf93-4b8d-8805-0c6f110d269f.jpg', keylist[3] : '20300401', keylist[4]: '1000000', keylist[5] : '유튜브롤 보고', keylist[6] : '유튜브에서 일등석 체험하는 영상을 봤어요, 비행기에서 샤워하는 건 어떨까 생각이드네요 꼭 이루고싶어요', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '9', keylist[1] : '드럼 세트', keylist[2] : 'https://www.hanbit.co.kr/data/editor/20181212154715_lzgcmunr.jpg', keylist[3] : '20231001', keylist[4]: '1500000', keylist[5] : '둠칫둠둠칫', keylist[6] : '유명 메이커의 드럼은 소리가 어떻게 다를까?', keylist[7] : 0, keylist[8] : '1' },
                { keylist[0] : '10', keylist[1] : '아이폰', keylist[2] : 'https://sitem.ssgcdn.com/63/62/50/item/1000508506263_i1_1100.jpg', keylist[3] : '20240401', keylist[4]: '1000000', keylist[5] : '아이폰 신제품마다 구매합니다.', keylist[6] : '이번엔 더 비싸질 꺼 같아 목표로 글 올렸어요', keylist[7] : 3, keylist[8] : '1' }
]
db.project_1.insert_many(dummy)
# ----------------------

# 팀 소개 메인
@app.route('/')
def home():
    return render_template('main.html')

# 위시리스트 메인
@app.route("/wishlist", methods=["GET"])
def wishlist_get():
    
    return render_template('wishlist.html')

#위시리스트 작성
@app.route("/wishlist/create", methods=["GET"])
def wishlist_create_get():
    return render_template('wishlist_create.html')


    
# 데이타 가져오기 reverse
@app.route('/item', methods=['GET'])
def getItems():
    all_list = list(db.project_1.find({},{'_id':False}))
    all_list.reverse()
    return jsonify({'result':all_list})

# 데이타 가져오기
@app.route('/item_', methods=['GET'])
def getItems_():
    all_list = list(db.project_1.find({},{'_id':False}))
    print(all_list)
    return jsonify({'result':all_list})

# 게시글 등록
@app.route('/item', methods=['POST'])
def addItems():
    id_receive = request.form['id_give']
    title_receive = request.form['title_give']
    image_receive = request.form['image_give']
    day_receive = request.form['day_give']
    price_receive = request.form['price_give']
    reason_receive = request.form['reason_give']
    description_receive = request.form['description_give']
    password_receive = request.form['password_give']
    
    doc = {
        'id' : id_receive,
        'title' : title_receive,
        'image' : image_receive,
        'day' : day_receive,
        'price' : price_receive,
        'reason' : reason_receive,
        'description' : description_receive,
        'password' : password_receive,
        'recommandCount' : 0
    }
    
    db.project_1.insert_one(doc)
    
    return jsonify({'result': '작성이 완료되었습니다!'})

#위시리스트 상세 페이지
@app.route("/wishlistDetail", methods=["GET"])
def wishlistDetailPage():
    idx = request.args.get('id')
    all_list = list(db.project_1.find({},{'_id':False}))
    
    for lt in all_list:
        if lt['id'] == idx:
            return render_template('wishlistDetail.html', data=lt)
        


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)