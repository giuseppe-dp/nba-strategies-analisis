import kagglehub
import sqlite3 as sql
import pandas as pd
import dtale as dt
import os

# # Download latest version
base_path = os.path.dirname(os.path.abspath(__file__))

target_path = os.path.join(base_path, "dataset")

path = kagglehub.dataset_download(
  "wyattowalsh/basketball", 
  output_dir=target_path
)

print(f"Dataset scaricato con successo in:\n{path}")

# connect al SQL database
db_path = os.path.join(target_path,'nba.sqlite')
connection = sql.connect(db_path)
print("SQL database connected")
table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", connection)
print(table)

query = """
  SELECT 
    SUBSTR(season_id, 2, 4) AS season,
    team_id_home AS team_id,
    team_name_home AS team_name,
    CASE WHEN wl_home = 'W' THEN 1 ELSE 0 END AS win,
    fgm_home AS fgm,
    fga_home AS fga,
    fg3m_home AS fg3m,
    fg3a_home AS fg3a,
    "home" AS location
  FROM game
  WHERE season_id LIKE '2%'

  UNION ALL

  -- Dati squadra in TRASFERTA
  SELECT 
    SUBSTR(season_id, 2, 4) AS season,
    team_id_away AS team_id,
    team_name_away AS team_name,
    CASE WHEN wl_away = 'W' THEN 1 ELSE 0 END AS win,
    fgm_away AS fgm,
    fga_away AS fga,
    fg3m_away AS fg3m,
    fg3a_away AS fg3a,
    "away" AS location
  FROM game
  WHERE season_id LIKE '2%'
"""
# creating the pandas object from the query
df_game = pd.read_sql(query, connection).astype({"season": int})
d = dt.show(df_game, host='localhost')

input("..")
