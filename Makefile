docker-build:
	docker build -t back_image .

run-backend :
	docker run --rm back_image

