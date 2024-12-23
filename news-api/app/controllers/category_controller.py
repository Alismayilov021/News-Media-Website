from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService

# Blueprint for category routes
bp = Blueprint('categories', __name__, url_prefix='/api/categories')

# Get all categories
@bp.route('/', methods=['GET'])
def get_all_categories():
    categories = CategoryService.get_all_categories()
    return jsonify([category.to_dict() for category in categories])

# Get category by ID
@bp.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = CategoryService.get_category_by_id(category_id)
    return jsonify(category.to_dict())

# Create a new category
@bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()

    # Ensure that required fields are provided
    if 'name' not in data:
        return jsonify({"error": "Category name is required"}), 400

    # Create the new category using the service
    category = CategoryService.create_category(data)
    return jsonify(category.to_dict()), 201

# Update a category
@bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()

    # Ensure that required fields are provided
    if 'name' not in data:
        return jsonify({"error": "Category name is required"}), 400

    # Update the category using the service
