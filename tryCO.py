from askCO import Search
import os

# Register for an API key at https://data.tepapa.govt.nz/docs/register.html
# Save it to the environment variable "TE-PAPA-KEY"
api_key = os.environ.get("TE-PAPA-KEY")

# Set functional parameters
quiet = False
sleep = 0.1
timeout = 5
attempts = 3

# Set the search request parameters
endpoint = "object"
query = "Myosotis"
filters = [{"field": "type", "keyword":"Specimen"},{"field": "collection", "keyword": "Plants"}]
fields = None
size = 100
start = 0

# Create the query object
request = Search(api_key=api_key, endpoint=endpoint, query=query, filters=filters, fields=fields, size=size, start=start, timeout=timeout, attempts=attempts, quiet=quiet, sleep=sleep)

# Run the query
request.send_query()

# See what you got
print("Search returned {} results".format(request.record_count))
if request.record_count > 0:
	print("First result:")
	print(next(iter(request.records)))