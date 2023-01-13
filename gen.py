from markdownTable import markdownTable
import json

prices = json.loads(open("prices.json", "r").read().strip())

data = []
for service, serviceInfo in prices.items():
	if serviceInfo['billing_method'] == 'none':
		continue

	billing_method = 'Per-Request'
	if serviceInfo['billing_method'] == "per_result":
		billing_method = 'Per-Result'

	for endpointMethodAndName, endpointCost in serviceInfo['endpoints'].items():
		arr = endpointMethodAndName.split('.')
		endpointMethod = arr[0]
		endpointName = arr[-1]
		data.append({
			'Method': endpointMethod,
			'Service': service,
			'Endpoint': endpointName,
			'Cost': endpointCost,
			'Billing Method': billing_method
		})


table = markdownTable(data).setParams(row_sep = 'markdown', quote = False)

readme = open("README.md.template", "r").read()
readme = readme.replace('|PRICES_JSON_HERE_PLS_SER|', json.dumps(prices, indent=4))
readme = readme.replace('|PRICE_TABLE_HERE_PLS_SER|', table.getMarkdown())

open("README.md", "w").write(readme)