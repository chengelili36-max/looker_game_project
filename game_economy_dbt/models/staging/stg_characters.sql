with raw_data as (
    select * from read_csv_auto('../data/raw_characters.csv')
)

select
    char_id,
    char_name,
    rarity,
    cast(logistics_bonus as numeric) as logistics_bonus,
    cast(base_cost as integer) as base_cost
from raw_data