default:

init:
	mkdir -p ci services/api/cmd/api services/worker/cmd/worker libs/common
	cd services/api    && go mod init hello.com/multi-module/services/api    && go mod tidy && cd -
	cd services/worker && go mod init hello.com/multi-module/services/worker && go mod tidy && cd -
	cd libs/common     && go mod init hello.com/multi-module/libs/common     && go mod tidy && cd -
	go work init ./ci ./services/api ./services/worker ./libs/common

.PHONY: default init
