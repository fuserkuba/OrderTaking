# Order Taking

1. After cloning this repository, you can use [docker-compose](deployments/docker-compose.yml) or execute:

```sh
make install
```

Then simply visit [Order Taking][App]!

2. Documented requests and response of the API with [swagger3](http://swagger.io/) support according to the [openapi 3.0.0 specification](https://swagger.io/specification/) is available on [Order Taking][App]

3. The API is able to make estimations in two ways:

 * One by one using [POST] /toTake :
 ```sh
 curl -X POST "http://localhost:5000/toTake" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"order_id\":\"24364873\",\"store_id\":\"30000009\",\"to_user_distance\":2.4781006757058885,\"to_user_elevation\":2.71936035156295,\"total_earning\":3500,\"created_at\":\"2017-09-07T10:02:17Z\"}"
 ```
  * In batch using [PUT] /toTake :
  ```sh
curl -X PUT "http://localhost:5000/toTake" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"orders\":[{\"order_id\":\"14364873\",\"store_id\":\"30000009\",\"to_user_distance\":2.4781006757058885,\"to_user_elevation\":-72.71936035156295,\"total_earning\":5200,\"created_at\":\"2017-09-07T20:02:17Z\"},{\"order_id\":\"14369927\",\"store_id\":\"30000094\",\"to_user_distance\":1.168212748531239,\"to_user_elevation\":-12.61474609375,\"total_earning\":3450,\"created_at\":\"2017-09-07T20:24:18Z\"}]}"
```
 
6. A postman collection with examples is also [available](OrderTaking.postman_collection.json) 
 
5. The app stores locally in a mongo DB each estimation to future analysis.

6. The Jupyter Notebook used for analysis and prediction is available on [training](training/TakeOrderTraining.ipynb)


## Requirements

To build this project you will need [Docker][Docker Install] and [Docker Compose][Docker Compose Install].

[Docker Install]:  https://docs.docker.com/install/
[Docker Compose Install]: https://docs.docker.com/compose/install/
[App]: http://127.0.0.1:5000

