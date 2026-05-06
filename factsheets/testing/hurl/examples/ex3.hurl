# Step 1: Login and capture token
POST http://localhost:8080/api/login
{
  "username": "admin",
  "password": "password123"
}

HTTP 200
[Captures]
token: jsonpath "$.access_token"

# Step 2: Use captured token for a second request
GET http://localhost:8080/api/profile
Authorization: Bearer {{token}}

HTTP 200
[Asserts]
jsonpath "$.username" == "admin"
