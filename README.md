## Install

```
# Build the image
docker build -t django-app:latest .

# Run the container with auto-restart
docker run -d --restart=always --name django-container -p 8000:8000 django-app:latest --env-file ./.env
```
