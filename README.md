# Order Taking

1. After cloning this repository, you can use [docker-compose](deployments/docker-compose.yml) or execute:

```sh
make install
```

Then simply visit [Order Taking][App]!

2. Documented requests and response of the API with [swagger3](http://swagger.io/) support according to the [openapi 3.0.0 specification](https://swagger.io/specification/) is available on [Order Taking][App]

3. The API is able to make an estimation [one by one](http://localhost:5000/#/List%20%5B%20%22predict%22%20%5D/post_toTake) or in [batch](http://localhost:5000/#/List%20%5B%20%22predict%22%20%5D/put_toTake)

4. The app stores locally in a mongo DB each estimation to future analysis.


## Requirements

To build this project you will need [Docker][Docker Install] and [Docker Compose][Docker Compose Install].

[Docker Install]:  https://docs.docker.com/install/
[Docker Compose Install]: https://docs.docker.com/compose/install/
[App]: http://127.0.0.1:5000

