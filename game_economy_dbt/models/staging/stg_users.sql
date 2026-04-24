with raw_data as (
    select * from read_csv_auto('../data/raw_users.csv')
)

select
    user_id,
    cast(register_date as date) as register_date,
    cast(vip_level as integer) as vip_level
from raw_data