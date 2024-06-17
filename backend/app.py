from flask import Flask, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)

@app.route('/run_backtest', methods=['POST'])
def run_backtest():
    data = request.get_json()
    scene_name = data.get('scene_name')
    params = data.get('params')

    # Serialize params to JSON string
    params_json = json.dumps(params)

    # Call the run_backtest.py script
    result_file = f"{scene_name}_results.json"
    process = subprocess.run(
        ['python', 'run_backtest.py', scene_name, params_json],
        capture_output=True,
        text=True
    )

    if process.returncode != 0:
        return jsonify({"error": process.stderr}), 500

    # Read the results from the file
    if os.path.exists(result_file):
        with open(result_file, 'r') as f:
            results = json.load(f)
        return jsonify(results), 200
    else:
        return jsonify({"error": "Results file not found"}), 500

if __name__ == '__main__':
    app.run(debug=True)

