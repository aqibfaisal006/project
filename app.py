from flask import Flask, jsonify, request

app = Flask(__name__)

students = {}
current_id = 1

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200


@app.route('/students', methods=['POST'])
def add_student():
    global current_id
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    student = {"id": current_id, "name": data['name']}
    students[current_id] = student
    current_id += 1

    return jsonify(student), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)