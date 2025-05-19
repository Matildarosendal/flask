from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        message="Flask API by Matilda"
    ), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

@app.route("/nums")
def num_numbers():
    numbers_param = request.args.get("numbers")
    if not numbers_param:
        return jsonify(error="Missing 'numbers' parameter"), 400
    numbers = numbers_param.split(",")
    return jsonify(num=len(numbers)), 200

@app.route("/sum")
def sum_numbers():
    numbers_param = request.args.get("numbers")
    mysum = 0
    if numbers_param:
        numbers = numbers_param.split(",")
        for num in numbers:
            mysum += int(num)
    return jsonify(sum=mysum), 200

@app.route("/max")
def max_numbers():
    numbers_param = request.args.get("numbers")
    if not numbers_param:
        return jsonify(error="Missing 'numbers' parameter"), 400
    numbers = numbers_param.split(",")
    max_num = max(numbers)
    return jsonify(max=max_num), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)