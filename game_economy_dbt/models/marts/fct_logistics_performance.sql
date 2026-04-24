
with trade_logs as (
    select * from {{ ref('stg_trade_logs') }}
),
characters as (
    select * from {{ ref('stg_characters') }}
),
routes as (
    select * from {{ ref('stg_routes') }}
),
users as (
    select * from {{ ref('stg_users') }}
)


select
    
    l.log_id,
    l.created_at,
    u.user_id,
    u.vip_level,
    c.char_name,
    c.rarity,
    r.origin,
    r.destination,
    l.status,

    l.actual_profit as gross_revenue,         
    c.base_cost as dispatch_cost,               
    (l.actual_profit - c.base_cost) as net_profit, 

    
    r.time_hours,
    case 
        when l.status = 'Completed' and r.time_hours > 0 
        then cast((l.actual_profit - c.base_cost) as float) / r.time_hours 
        else 0 
    end as profit_per_hour,                    
    

    case when c.rarity = 'Red' then true else false end as is_red_card 

from trade_logs l
left join characters c on l.char_id = c.char_id
left join routes r on l.route_id = r.route_id
left join users u on l.user_id = u.user_id