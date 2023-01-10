# prices

[FireAcademy.io](https://fireacademy.io) prices from catchpole config.

## Format

```
p = read('prices.json')
p[acessed_route]['base_url'] = internal url to forward the request to
p[acessed_route]['headers'] = headers to include in the request
p[acessed_route]['billing_method'] = billing method per request -> 'none', 'per_request', and 'per_result'
p[acessed_route]['endpoints'][acessed_endpoint] = object containing per-endpoint configuration (cost, do_post_instead)
```