# prices

[FireAcademy.io](https://fireacademy.io) prices from catchpole config.

## Format

Since almost everyone can read python:

```python
p = open('prices.json', 'r').read()

p[acessed_route]['base_url']
#	internal url to forward the request to

p[acessed_route]['headers']
#	headers to include in the request

p[acessed_route]['billing_method']
#	billing method per request
#	values: 'none', 'per_request', 'per_result'

p[acessed_route]['endpoints'][acessed_endpoint]
#	object containing per-endpoint configuration
#	keys: 'cost'
```