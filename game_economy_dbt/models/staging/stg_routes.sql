with raw_data as (
    select * from read_csv_auto('../data/raw_routes.csv')
)

select
    route_id,
    origin,
    destination,
    cast(base_profit as integer) as base_profit,
    cast(time_hours as integer) as time_hours
from raw_data