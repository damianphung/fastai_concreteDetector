# fastai_concreteDetector
fastAI with fastAPI

## Build
```
docker build --tag concretetest .
```

## Run
```
docker run --rm --name test -e PORT="8000" -e APP_MODULE="app:application" -p 8000:8000 concretetest
```
