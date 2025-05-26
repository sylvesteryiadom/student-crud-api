from flask import Blueprint, request, jsonify, abort
from .models import Student
from . import db
import logging

students_bp = Blueprint('students', __name__, url_prefix='/api/v1/students')
health_bp = Blueprint('health', __name__)
logger = logging.getLogger(__name__)


@students_bp.route('', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        abort(400, description="Missing required fields: name and email")
    student = Student(
        name=data['name'],
        email=data['email'],
        age=data.get('age')
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name, "email": student.email, "age": student.age}), 201

@students_bp.route('', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([
        {"id": s.id, "name": s.name, "email": s.email, "age": s.age}
        for s in students
    ])

@students_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify({"id": student.id, "name": student.name, "email": student.email, "age": student.age})

@students_bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()
    if 'name' in data: student.name = data['name']
    if 'email' in data: student.email = data['email']
    if 'age' in data: student.age = data['age']
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name, "email": student.email, "age": student.age})

@students_bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"})

#health check endpoint
@health_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200
