with raw_data as (
    
    select * from read_csv_auto('../data/raw_trade_logs.csv')
),

renamed_and_casted as (
    select
        log_id,
        user_id,
        char_id,
        route_id,
        status,
        
        cast(actual_profit as integer) as actual_profit,
    
        cast(created_at as timestamp) as created_at
    from raw_data
)

select * from renamed_and_casted