import duckdb
import pandas as pd
import os


db_path = 'game_economy_dbt/game_db.duckdb'
output_path = 'data/looker_ready_data.csv'

try:
    
    print("connecting...")
    con = duckdb.connect(db_path)
    
   
    print("selecting fct_logistics_performance data...")
    df = con.execute("SELECT * FROM fct_logistics_performance").df()
    
   
    df.to_csv(output_path, index=False)
    
    print(f"🎉 success! {len(df)} rows exported to: {output_path}")
    print("next: open your browser and log in to Looker Studio!")

except Exception as e:
    print(f"❌ error: {e}")
    print("please ensure you are running this script from the looker_game_project root directory!")