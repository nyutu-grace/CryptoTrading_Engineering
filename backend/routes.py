from flask import Blueprint, request, jsonify
from backend.backtesting.run_backtest import run_backtest

bp = Blueprint('backtest', __name__)

@bp.route('/run_backtest', methods=['POST'])
def run_backtest_route():
    datafile = request.json.get('datafile')
    if not datafile:
        return jsonify({'error': 'Datafile not provided'}), 400

    try:
        run_backtest(datafile)
        return jsonify({'status': 'Backtest completed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
