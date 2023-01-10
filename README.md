# prices

[FireAcademy.io](https://fireacademy.io) prices from catchpole config.

## Format

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