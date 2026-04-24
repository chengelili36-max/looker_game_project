import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os


os.makedirs('data', exist_ok=True)


characters = [
    {'char_id': 'C001', 'char_name': 'Aria', 'rarity': 'Red', 'logistics_bonus': 1.50, 'base_cost': 500},
    {'char_id': 'C002', 'char_name': 'Nyx', 'rarity': 'Gold', 'logistics_bonus': 1.25, 'base_cost': 300},
    {'char_id': 'C003', 'char_name': 'Blacksmith', 'rarity': 'Blue', 'logistics_bonus': 1.05, 'base_cost': 100},
    {'char_id': 'C004', 'char_name': 'Trader', 'rarity': 'Purple', 'logistics_bonus': 1.15, 'base_cost': 200}
]
pd.DataFrame(characters).to_csv('data/raw_characters.csv', index=False)


routes = [
    {'route_id': 'R01', 'origin': 'Capital', 'destination': 'Black Market', 'base_profit': 1500, 'time_hours': 8},
    {'route_id': 'R02', 'origin': 'Capital', 'destination': 'Mines', 'base_profit': 800, 'time_hours': 4},
    {'route_id': 'R03', 'origin': 'Fishing Village', 'destination': 'Capital', 'base_profit': 500, 'time_hours': 2}
]
pd.DataFrame(routes).to_csv('data/raw_routes.csv', index=False)


users = [{'user_id': f'U{str(i).zfill(4)}', 'register_date': '2026-01-01', 'vip_level': random.randint(0, 5)} for i in range(1, 101)]
pd.DataFrame(users).to_csv('data/raw_users.csv', index=False)


logs = []
start_date = datetime(2026, 4, 1)

for i in range(5000):
    user = random.choice(users)['user_id']
    char = random.choice(characters)
    route = random.choice(routes)
    

    is_success = random.random() > 0.1 
    actual_profit = int(route['base_profit'] * char['logistics_bonus']) if is_success else 0
    

    created_at = start_date + timedelta(days=random.randint(0, 29), hours=random.randint(0, 23))
    
    logs.append({
        'log_id': f'L{str(i).zfill(5)}',
        'user_id': user,
        'char_id': char['char_id'],
        'route_id': route['route_id'],
        'status': 'Completed' if is_success else 'Failed',
        'actual_profit': actual_profit,
        'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S')
    })

pd.DataFrame(logs).to_csv('data/raw_trade_logs.csv', index=False)
print("🎉 Successfully generated 4 mock game data files with English names in the /data directory!")