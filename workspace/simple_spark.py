import pandas as pd
import random
from datetime import datetime, timedelta
import importlib.util

def generate_synthetic_logs(num_entries=1000):
    log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
    current_time = datetime.now()
    logs = []
    for _ in range(num_entries):
        timestamp = current_time - timedelta(seconds=random.randint(0, 100000))
        log_level = random.choice(log_levels)
        message = f"This is a {log_level} message."
        logs.append({'timestamp': timestamp, 'log_level': log_level, 'message': message})
    return pd.DataFrame(logs)

# Generate logs and save to CSV
df_logs = generate_synthetic_logs()
df_logs.to_csv('synthetic_system_logs.csv', index=False)

# Import simple_map_reduce module
spec = importlib.util.spec_from_file_location("simple_map_reduce", "/opt/workspace/simple_map_reduce.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Use the map_reduce function
log_file = 'synthetic_system_logs.csv'
log_level_counts = module.map_reduce(log_file)

print(log_level_counts)
