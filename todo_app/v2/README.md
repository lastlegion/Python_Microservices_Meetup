## Accessing REST endpoints through cURL


### List all todo items
```
curl --location --request GET 'http://localhost:5000/todo'
```

### Create a todo
```
curl --location --request POST 'http://localhost:5000/todo' \
--header 'Content-Type: application/json' \
--data-raw '{
	"description": "This is an example",
	"status": "active"
}'
```


### Update a todo item
```
curl --location --request PUT 'http://localhost:5000/todo/3' \
--data-raw '{
	"description": "I have to do the groceries today (Edited)",
	"status": "active"
}'
```

### Delete a todo item
```
curl --location --request DELETE 'http://localhost:5000/todo/3' 
```
