GET http://localhost:8080/api/secure-data
Authorization: Bearer my-secret-token
X-Custom-Header: Hurl-Test

HTTP 200
[Asserts]
cookie "session_id" exists
header "Cache-Control" == "no-cache"
body contains "Authorized access granted"
