from app.services.article_service import ArticleService
from flask import request, jsonify

class ArticleController:

    @staticmethod
    def create_article():
        try:
            data = request.get_json()
            article = ArticleService.create_article(data)
            return jsonify(article.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def get_article(article_id):
        article = ArticleService.get_article_by_id(article_id)
        if article:
            return jsonify(article.to_dict())
        return jsonify({"error": "Article not found"}), 404

    @staticmethod
    def get_all_articles():
        articles = ArticleService.get_all_articles()
        return jsonify([article.to_dict() for article in articles])

    @staticmethod
    def update_article(article_id):
        try:
            data = request.get_json()
            article = ArticleService.update_article(article_id, data)
            return jsonify(article.to_dict())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def delete_article(article_id):
        try:
            article = ArticleService.delete_article(article_id)
            return jsonify({"message": f"Article {article.id} deleted successfully."})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
