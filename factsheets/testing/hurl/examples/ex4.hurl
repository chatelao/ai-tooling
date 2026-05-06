# Test redirection handling
GET http://localhost:8080/old-page

HTTP 301
[Asserts]
header "Location" == "http://localhost:8080/new-page"

# Test basic auth
GET http://localhost:8080/basic-auth
[BasicAuth]
user: password

HTTP 200
