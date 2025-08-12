default:

init:
	mkdir -p libs/common
	mkdir -p modules/build
	mkdir -p modules/release
	go work init ./libs/common ./modules/build ./modules/release
	go work sync

first:
	cd libs/common     && go mod init libs/common && cd -
	cd modules/build   && dagger init --sdk=go && cd -
	cd modules/release && dagger init --sdk=go && cd -
