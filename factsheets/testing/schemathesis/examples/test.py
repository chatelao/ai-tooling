import schemathesis
from hypothesis import settings, HealthCheck

# Load schema from a local file for testing
schema = schemathesis.from_path("api.yaml", base_url="http://localhost:8080")

@schema.parametrize()
@settings(max_examples=10, suppress_health_check=[HealthCheck.filter_too_much])
def test_api(case):
    # This would normally call the actual API
    # case.call_and_validate()
    print(f"Testing endpoint: {case.endpoint.path} with method: {case.method}")
