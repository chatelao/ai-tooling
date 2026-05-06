POST http://localhost:8080/api/users
Content-Type: application/json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}

HTTP 201
[Asserts]
header "Content-Type" contains "application/json"
jsonpath "$.id" exists
jsonpath "$.name" == "Jane Doe"
jsonpath "$.status" == "active"
duration < 500
