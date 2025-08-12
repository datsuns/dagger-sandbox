default:

init_mod:
	mkdir -p ci services/api/cmd/api services/worker/cmd/worker libs/common
	go work init ./ci ./services/api ./services/worker ./libs/common
	cd services/api    && go mod init hello.com/multi-module/services/api    && cd -
	cd services/worker && go mod init hello.com/multi-module/services/worker && cd -
	cd libs/common     && go mod init hello.com/multi-module/libs/common     && cd -

init_dagger:
	cd ci              && dagger init --name ci && dagger develop --sdk=go && cd -
	cd services/api    && dagger init --name ci && dagger develop --sdk=go && cd -
	cd services/worker && dagger init --name ci && dagger develop --sdk=go && cd -

resolve:
	cd services/api    && echo "require example.com/monorepo/libs/common v0.0.0" && go mod tidy && cd -
	cd services/worker && echo "require example.com/monorepo/libs/common v0.0.0" && go mod tidy && cd -

.PHONY: default init_mod
