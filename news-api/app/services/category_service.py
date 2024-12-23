from app.services.category_service import CategoryService
from flask import request, jsonify

class CategoryController:

    @staticmethod
    def create_category():
        try:
            data = request.get_json()
            category = CategoryService.create_category(data)
            return jsonify(category.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_category(category_id):
        category = CategoryService.get_category_by_id(category_id)
        if category:
            return jsonify(category.to_dict())
        return jsonify({"error": "Category not found"}), 404

    @staticmethod
    def get_all_categories():
        categories = CategoryService.get_all_categories()
        return jsonify([category.to_dict() for category in categories])

    @staticmethod
    def update_category(category_id):
        try:
            data = request.get_json()
            category = CategoryService.update_category(category_id, data)
            return jsonify(category.to_dict())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_category(category_id):
        try:
            category = CategoryService.delete_category(category_id)
            return jsonify({"message": f"Category {category.id} deleted successfully."})
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def assign_categories_to_article(article_id):
        try:
            data = request.get_json()
            category_ids = data.get('category_ids', [])
            article = CategoryService.assign_categories_to_article(article_id, category_ids)
            return jsonify(article.to_dict())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
