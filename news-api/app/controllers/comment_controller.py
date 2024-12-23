from flask import Blueprint, request, jsonify
from app.services.comment_service import CommentService

# Blueprint for comment routes
bp = Blueprint('comments', __name__, url_prefix='/api/comments')

# Get all comments for a specific article
@bp.route('/<int:article_id>', methods=['GET'])
def get_comments_by_article(article_id):
    comments = CommentService.get_comments_by_article(article_id)
    return jsonify([comment.to_dict() for comment in comments])

# Create a new comment for a specific article
@bp.route('/<int:article_id>', methods=['POST'])
def create_comment(article_id):
    data = request.get_json()

    # Ensure that required fields are provided
    if 'content' not in data:
        return jsonify({"error": "Comment content is required"}), 400

    # Create the new comment using the service
    comment = CommentService.create_comment(article_id, data)
    return jsonify(comment.to_dict()), 201

# Update an existing comment
@bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.get_json()

    # Ensure that required fields are provided
    if 'content' not in data:
        return jsonify({"error": "Comment content is required"}), 400

    # Update the comment using the service
    comment = CommentService.update_comment(comment_id, data)
    return jsonify(comment.to_dict())

# Delete a comment
@bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    # Delete the comment using the service
    CommentService.delete_comment(comment_id)
    return jsonify({'message': 'Comment deleted successfully'}), 204
