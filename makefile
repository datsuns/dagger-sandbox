VERSION=$(shell dagger version | cut -d' ' -f2)

default:

init:
	dagger init --sdk go --name hello

run:
	cd cmd && go mod tidy && dagger run -i go run main.go

call:
	dagger call container-echo --string-arg hello

init_py:
	dagger init --sdk python --name hello --source src

run_py:
	cd src && python main.py

install_py:
	python -m venv .venv
	source .venv/bin/activate
	pip install dagger-io

enable_gpu:
	# https://docs.dagger.io/configuration/custom-runner
	echo $(VERSION)
	docker rm -f dagger-engine-$(VERSION) 2>/dev/null && docker run --gpus all -d --privileged -e _EXPERIMENTAL_DAGGER_GPU_SUPPORT=true --name dagger-engine-$(VERSION) registry.dagger.io/engine:$(VERSION)-gpu -- --debug

check_gpu:
	dagger -m github.com/samalba/dagger-modules/nvidia-gpu call has-gpu

export_docker_image:
	dagger call export-docker-image --string-arg hell2 export --path=./image.tgz

load_exported_image:
	bash ../load_image.sh image.tgz


.PHONY: default int run init_py run_py install_py enable_gpu check_gpu export_docker_image
