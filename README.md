# django-test
## Installation 
To build docker images, run following command in terminal:
``` sh
docker-compose build
```
After docker images installed successfully, run cmd following:

``` sh
docker-compose up
```

## Way to generate and get API key
```
from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="my-remote-service")
key
```