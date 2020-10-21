import sys
import os
import random

from tqdm import tqdm

from flask import Blueprint, request, jsonify, Flask
import torch
import torch.nn.functional as F
import wget

import db
import config
from ml.model import CharacterLevelCNN
from ml.utils import predict_sentiment

app = Flask(__name__)
api = Blueprint('api', __name__)

# Load pytorch model for inference
model_name = 'model_en.pth'
model_path = f'./ml/models/{model_name}'
model = CharacterLevelCNN()


if model_name not in os.listdir('./ml/models/'):
    print(f'downloading the trained model {model_name}')
    wget.download(
        "https://github.com/simon831110/Semantic-analysis-Pytorch/tree/main/src/api/ml/models/model_en.pth",
        out=model_path
    )
else:
    print('model already saved to api/ml/models')

if torch.cuda.is_available():
    trained_weights = torch.load(model_path)
else:
    trained_weights = torch.load(model_path, map_location='cpu')
#載入
model.load_state_dict(trained_weights)
model.eval()
print('PyTorch model loaded !')

#告訴flask到哪個網址執行函數  methods路由只接收POST的命令
@api.route('/predict', methods=['POST'])
def predict_rating():
    '''
    對於評論進行分數預測
    '''
    if request.method == 'POST':
        #若評論沒東西
        if 'review' not in request.form:
            return jsonify({'error': 'no review in body'}), 400
        else:
            parameters = model.get_model_parameters()
            #評論
            review = request.form['review']
            output = predict_sentiment(model, review, **parameters)
            return jsonify(float(output))


@api.route('/review', methods=['POST'])
def post_review():
    '''
    Save review to database.
    '''
    if request.method == 'POST':
        expected_fields = [
            'review',
            'rating',
            'suggested_rating',
            'sentiment_score',
            'brand',
            'user_agent',
            'ip_address'
        ]
        if any(field not in request.form for field in expected_fields):
            return jsonify({'error': 'Missing field in body'}), 400

        query = db.Review.create(**request.form)

        return jsonify(query.serialize())


@api.route('/reviews', methods=['GET'])
def get_reviews():
    '''
    Get all reviews.
    '''
    if request.method == 'GET':
        query = db.Review.select().order_by(db.Review.created_date.desc())

        return jsonify([r.serialize() for r in query])


app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST)
