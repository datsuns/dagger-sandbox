default:

init:
	mkdir -p lib/common module/build
	cd lib/common   && go mod init multi-module/lib/common && cd -
	cd module/build && dagger init --sdk=go --name multi-module/module/build
	go work init ./lib/common ./module/build


.PHONY: default init
