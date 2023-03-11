# prices

[FireAcademy.io](https://fireacademy.io) prices from catchpole config.

## Price Table

|Method|     Service     |             Endpoint            |Cost|Billing Method|
|------|-----------------|---------------------------------|----|--------------|
|  GET |     leaflet     |         get_network_info        | 10 |  Per-Request |
| POST |     leaflet     |         get_network_info        | 10 |  Per-Request |
|  GET |     leaflet     |       get_blockchain_state      | 10 |  Per-Request |
| POST |     leaflet     |       get_blockchain_state      | 10 |  Per-Request |
| POST |     leaflet     |            get_block            | 25 |  Per-Request |
| POST |     leaflet     |            get_blocks           | 25 |  Per-Request |
|  GET |     leaflet     |     get_block_count_metrics     | 10 |  Per-Request |
| POST |     leaflet     |     get_block_count_metrics     | 10 |  Per-Request |
| POST |     leaflet     |    get_block_record_by_height   | 50 |  Per-Request |
| POST |     leaflet     |         get_block_record        | 25 |  Per-Request |
| POST |     leaflet     |        get_block_records        | 25 |  Per-Request |
| POST |     leaflet     |         get_block_spends        | 100|  Per-Request |
|  GET |     leaflet     |   get_unfinished_block_headers  | 20 |  Per-Request |
| POST |     leaflet     |   get_unfinished_block_headers  | 20 |  Per-Request |
|  GET |     leaflet     |        get_network_space        | 100|  Per-Request |
| POST |     leaflet     |        get_network_space        | 100|  Per-Request |
| POST |     leaflet     |    get_additions_and_removals   | 100|  Per-Request |
| POST |     leaflet     | get_recent_signage_point_or_eos | 20 |  Per-Request |
| POST |     leaflet     | get_coin_records_by_puzzle_hash | 100|  Per-Request |
| POST |     leaflet     |get_coin_records_by_puzzle_hashes| 100|  Per-Request |
| POST |     leaflet     |     get_coin_record_by_name     | 25 |  Per-Request |
| POST |     leaflet     |    get_coin_records_by_names    | 25 |  Per-Request |
| POST |     leaflet     |  get_coin_records_by_parent_ids |5000|  Per-Request |
| POST |     leaflet     |     get_coin_records_by_hint    | 500|  Per-Request |
| POST |     leaflet     |             push_tx             |1000|  Per-Request |
| POST |     leaflet     |     get_puzzle_and_solution     | 25 |  Per-Request |
|  GET |     leaflet     |      get_all_mempool_tx_ids     | 10 |  Per-Request |
| POST |     leaflet     |      get_all_mempool_tx_ids     | 10 |  Per-Request |
|  GET |     leaflet     |      get_all_mempool_items      | 10 |  Per-Request |
| POST |     leaflet     |      get_all_mempool_items      | 10 |  Per-Request |
| POST |     leaflet     |    get_mempool_item_by_tx_id    | 10 |  Per-Request |
| POST |     leaflet     |         get_fee_estimate        | 10 |  Per-Request |
|  GET |     leaflet     |            get_routes           | 10 |  Per-Request |
| POST |     leaflet     |            get_routes           | 10 |  Per-Request |
|  GET |     leaflet     |             healthz             | 10 |  Per-Request |
| POST |     leaflet     |             healthz             | 10 |  Per-Request |
|  GET |leaflet-testnet10|         get_network_info        | 10 |  Per-Request |
| POST |leaflet-testnet10|         get_network_info        | 10 |  Per-Request |
|  GET |leaflet-testnet10|       get_blockchain_state      | 10 |  Per-Request |
| POST |leaflet-testnet10|       get_blockchain_state      | 10 |  Per-Request |
| POST |leaflet-testnet10|            get_block            | 25 |  Per-Request |
| POST |leaflet-testnet10|            get_blocks           | 25 |  Per-Request |
|  GET |leaflet-testnet10|     get_block_count_metrics     | 10 |  Per-Request |
| POST |leaflet-testnet10|     get_block_count_metrics     | 10 |  Per-Request |
| POST |leaflet-testnet10|    get_block_record_by_height   | 50 |  Per-Request |
| POST |leaflet-testnet10|         get_block_record        | 25 |  Per-Request |
| POST |leaflet-testnet10|        get_block_records        | 25 |  Per-Request |
| POST |leaflet-testnet10|         get_block_spends        | 100|  Per-Request |
|  GET |leaflet-testnet10|   get_unfinished_block_headers  | 20 |  Per-Request |
| POST |leaflet-testnet10|   get_unfinished_block_headers  | 20 |  Per-Request |
|  GET |leaflet-testnet10|        get_network_space        | 100|  Per-Request |
| POST |leaflet-testnet10|        get_network_space        | 100|  Per-Request |
| POST |leaflet-testnet10|    get_additions_and_removals   | 100|  Per-Request |
| POST |leaflet-testnet10| get_recent_signage_point_or_eos | 20 |  Per-Request |
| POST |leaflet-testnet10| get_coin_records_by_puzzle_hash | 100|  Per-Request |
| POST |leaflet-testnet10|get_coin_records_by_puzzle_hashes| 100|  Per-Request |
| POST |leaflet-testnet10|     get_coin_record_by_name     | 25 |  Per-Request |
| POST |leaflet-testnet10|    get_coin_records_by_names    | 25 |  Per-Request |
| POST |leaflet-testnet10|  get_coin_records_by_parent_ids |5000|  Per-Request |
| POST |leaflet-testnet10|     get_coin_records_by_hint    | 500|  Per-Request |
| POST |leaflet-testnet10|             push_tx             |1000|  Per-Request |
| POST |leaflet-testnet10|     get_puzzle_and_solution     | 25 |  Per-Request |
|  GET |leaflet-testnet10|      get_all_mempool_tx_ids     | 10 |  Per-Request |
| POST |leaflet-testnet10|      get_all_mempool_tx_ids     | 10 |  Per-Request |
|  GET |leaflet-testnet10|      get_all_mempool_items      | 10 |  Per-Request |
| POST |leaflet-testnet10|      get_all_mempool_items      | 10 |  Per-Request |
| POST |leaflet-testnet10|    get_mempool_item_by_tx_id    | 10 |  Per-Request |
| POST |leaflet-testnet10|         get_fee_estimate        | 10 |  Per-Request |
|  GET |leaflet-testnet10|            get_routes           | 10 |  Per-Request |
| POST |leaflet-testnet10|            get_routes           | 10 |  Per-Request |
|  GET |leaflet-testnet10|             healthz             | 10 |  Per-Request |
| POST |leaflet-testnet10|             healthz             | 10 |  Per-Request |

## prices.json Format

Since almost everyone can read python:

```python
p = open('prices.json', 'r').read()

# internal url to forward the request to
# string
p[acessed_route]['base_url']

# headers to include in the request
# list of strings
p[acessed_route]['headers']

# billing method per request
# string
# values: 'none', 'per_request', 'per_result'
p[acessed_route]['billing_method']

# leaflet only responds to POST requests
# set to true for compatibility
# (= change GET requests to POST)
# if true, acess_method is set to POST
# bool
p[acessed_route]['force_request_method_to_post']

# cost (either for the whole request or for one result)
# integer
p[acessed_route]['endpoints'][acess_method + acessed_endpoint]
```

## prices.json

```json
{
    "admin": {
        "base_url": "http://data-dude:5000/management/",
        "headers": [
            "X-Management-Token"
        ],
        "billing_method": "none",
        "endpoints": {
            "GET.unresolved-tickets": 0,
            "POST.generate-gift-codes": 0,
            "POST.resolve-ticket": 0,
            "POST.verify-email": 0,
            "POST.api-key-info": 0
        }
    },
    "stripe": {
        "base_url": "http://data-dude:5000/stripe/",
        "headers": [
            "Stripe-Signature"
        ],
        "billing_method": "none",
        "endpoints": {
            "POST.webhook": 0
        }
    },
    "api": {
        "base_url": "http://data-dude:5000/api/",
        "headers": [
            "Authorization"
        ],
        "billing_method": "none",
        "endpoints": {
            "GET.stripe-dashboard-url": 0,
            "POST.subscribe-url": 0,
            "POST.user-plan": 0,
            "GET.dashboard-data": 0,
            "POST.api-key": 0,
            "PUT.api-key": 0,
            "POST.gift-code": 0,
            "POST.ticket": 0,
            "GET.updates": 0,
            "POST.updates": 0,
            "GET.plans": 0
        }
    },
    "leaflet": {
        "base_url": "http://leaflet:18444/rpc/",
        "headers": [],
        "billing_method": "per_request",
        "endpoints": {
            "GET.get_network_info": 10,
            "POST.get_network_info": 10,
            "GET.get_blockchain_state": 10,
            "POST.get_blockchain_state": 10,
            "POST.get_block": 25,
            "POST.get_blocks": 25,
            "GET.get_block_count_metrics": 10,
            "POST.get_block_count_metrics": 10,
            "POST.get_block_record_by_height": 50,
            "POST.get_block_record": 25,
            "POST.get_block_records": 25,
            "POST.get_block_spends": 100,
            "GET.get_unfinished_block_headers": 20,
            "POST.get_unfinished_block_headers": 20,
            "GET.get_network_space": 100,
            "POST.get_network_space": 100,
            "POST.get_additions_and_removals": 100,
            "POST.get_recent_signage_point_or_eos": 20,
            "POST.get_coin_records_by_puzzle_hash": 100,
            "POST.get_coin_records_by_puzzle_hashes": 100,
            "POST.get_coin_record_by_name": 25,
            "POST.get_coin_records_by_names": 25,
            "POST.get_coin_records_by_parent_ids": 5000,
            "POST.get_coin_records_by_hint": 500,
            "POST.push_tx": 1000,
            "POST.get_puzzle_and_solution": 25,
            "GET.get_all_mempool_tx_ids": 10,
            "POST.get_all_mempool_tx_ids": 10,
            "GET.get_all_mempool_items": 10,
            "POST.get_all_mempool_items": 10,
            "POST.get_mempool_item_by_tx_id": 10,
            "POST.get_fee_estimate": 10,
            "GET.get_routes": 10,
            "POST.get_routes": 10,
            "GET.healthz": 10,
            "POST.healthz": 10
        }
    },
    "leaflet-testnet10": {
        "base_url": "http://leaflet-testnet10:18444/rpc/",
        "headers": [],
        "billing_method": "per_request",
        "endpoints": {
            "GET.get_network_info": 10,
            "POST.get_network_info": 10,
            "GET.get_blockchain_state": 10,
            "POST.get_blockchain_state": 10,
            "POST.get_block": 25,
            "POST.get_blocks": 25,
            "GET.get_block_count_metrics": 10,
            "POST.get_block_count_metrics": 10,
            "POST.get_block_record_by_height": 50,
            "POST.get_block_record": 25,
            "POST.get_block_records": 25,
            "POST.get_block_spends": 100,
            "GET.get_unfinished_block_headers": 20,
            "POST.get_unfinished_block_headers": 20,
            "GET.get_network_space": 100,
            "POST.get_network_space": 100,
            "POST.get_additions_and_removals": 100,
            "POST.get_recent_signage_point_or_eos": 20,
            "POST.get_coin_records_by_puzzle_hash": 100,
            "POST.get_coin_records_by_puzzle_hashes": 100,
            "POST.get_coin_record_by_name": 25,
            "POST.get_coin_records_by_names": 25,
            "POST.get_coin_records_by_parent_ids": 5000,
            "POST.get_coin_records_by_hint": 500,
            "POST.push_tx": 1000,
            "POST.get_puzzle_and_solution": 25,
            "GET.get_all_mempool_tx_ids": 10,
            "POST.get_all_mempool_tx_ids": 10,
            "GET.get_all_mempool_items": 10,
            "POST.get_all_mempool_items": 10,
            "POST.get_mempool_item_by_tx_id": 10,
            "POST.get_fee_estimate": 10,
            "GET.get_routes": 10,
            "POST.get_routes": 10,
            "GET.healthz": 10,
            "POST.healthz": 10
        }
    }
}
```