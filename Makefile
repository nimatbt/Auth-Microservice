IMAGE_NAME=authz
IMAGE_TAG=latest
GIT_COMMIT=`git rev-parse HEAD`
GIT_TAG=`git tag --points-at HEAD`

.PHONY: all
all: install dev

.PHONY: install
install:
	apt update && apt install -y python3 python3-pip 
	
.PHONY: dev
dev:
	apt update && apt install -y python3-venv
	
.PHONY: build # 24-1 34'
build:
	docker build -t ${IMAGE_NAME}:${IMAGE_TAG} --build-arg GIT_COMMIT=${GIT_COMMIT} --build-arg GIT_TAG=${GIT_TAG} .
