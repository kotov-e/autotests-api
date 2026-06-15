from swagger_coverage_tool import SwaggerCoverageTracker
import httpx

tracker = SwaggerCoverageTracker(service="api-course")


#account_tracker = SwaggerCoverageTracker(service="api-account")

# @tracker.track_coverage_httpx("/api/v1/users/{user_id}")
# def get_user(user_id: str) -> httpx.Response:
#     return httpx.get(f"http://localhost:8000/api/v1/users/{user_id}")

# @account_tracker.track_coverage_httpx("/api/v1/users")
# def create_user() -> httpx.Response:
#     return httpx.post("http://localhost:8000/api/v1/users")
