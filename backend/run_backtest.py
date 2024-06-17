import json
import sys

def run_backtest(scene_name, params):
    # Simulate running a backtest with the provided parameters
    results = {
        "scene_name": scene_name,
        "params": params,
        "metrics": {
            "return": 0.15,
            "number_of_trades": 50,
            "winning_trades": 30,
            "losing_trades": 20,
            "max_drawdown": 0.10,
            "sharpe_ratio": 1.25,
        }
    }
    return results

def save_results_to_file(results, file_path):
    with open(file_path, 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python run_backtest.py <scene_name> <params_json>")
        sys.exit(1)

    scene_name = sys.argv[1]
    params_json = sys.argv[2]

    try:
        params = json.loads(params_json)
    except json.JSONDecodeError:
        print("Invalid JSON for params")
        sys.exit(1)

    results = run_backtest(scene_name, params)
    save_results_to_file(results, f"{scene_name}_results.json")
    print(f"Backtest results saved to {scene_name}_results.json")

