from flask import Blueprint, request, jsonify
from app.services.article_service import ArticleService

# Blueprint setup for article routes
bp = Blueprint('articles', __name__, url_prefix='/api/articles')

# Get all articles
@bp.route('/', methods=['GET'])
def get_all_articles():
    articles = ArticleService.get_all_articles()
    return jsonify([article.to_dict() for article in articles])

# Get a single article by ID
@bp.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = ArticleService.get_article_by_id(article_id)
    if article:
        return jsonify(article.to_dict())
    return jsonify({'error': 'Article not found'}), 404

# Create a new article
@bp.route('/', methods=['POST'])
def create_article():
    data = request.get_json()

    # Basic validation of required fields
    if 'title' not in data or 'content' not in data or 'author_id' not in data:
        return jsonify({'error': 'Title, content, and author ID are required'}), 400

    article = ArticleService.create_article(data)
    return jsonify(article.to_dict()), 201

# Update an existing article
@bp.route('/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    data = request.get_json()

    # Find the article
    article = ArticleService.get_article_by_id(article_id)
    if not article:
        return jsonify({'error': 'Article not found'}), 404

    # Update article information
    updated_article = ArticleService.update_article(article_id, data)
    return jsonify(updated_article.to_dict())

# Delete an article
@bp.route('/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = ArticleService.get_article_by_id(article_id)
    if not article:
        return jsonify({'error': 'Article not found'}), 404

    ArticleService.delete_article(article_id)
    return jsonify({'message': 'Article deleted successfully'}), 204
