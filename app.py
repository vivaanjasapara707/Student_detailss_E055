from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return send_file("app.html")


@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.json

    student = {
        "name": data.get("name"),
        "sapid": data.get("sapid"),
        "marks": data.get("marks"),
        "age": data.get("age")
    }

    students.append(student)

    return jsonify({"message": "Student added successfully"})


@app.route("/search_student")
def search_student():
    query = request.args.get("query")

    for student in students:
        if student["name"] == query or student["sapid"] == query:
            return jsonify(student)

    return jsonify({"message": "Student not found"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)