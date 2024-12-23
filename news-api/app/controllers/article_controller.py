from app.services.article_service import ArticleService
from flask import request, jsonify, Blueprint

bp = Blueprint('articles', __name__, url_prefix='/api/articles')

@bp.route('/', methods=['GET'])
def get_all_articles():
    articles = ArticleService.get_all_articles()
    return jsonify([article.to_dict() for article in articles])

@bp.route('/<int:article_id>', methods=['GET'])
def get_article_by_id(article_id):
    article = ArticleService.get_article_by_id(article_id)
    return jsonify(article.to_dict())

@bp.route('/', methods=['POST'])
def create_article():
    data = request.get_json()
    article = ArticleService.create_article(data)
    return jsonify(article.to_dict()), 201

@bp.route('/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    data = request.get_json()
    article = ArticleService.update_article(article_id, data)
    return jsonify(article.to_dict())

@bp.route('/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = ArticleService.delete_article(article_id)
    return jsonify({'message': 'Article deleted successfully'}), 204
