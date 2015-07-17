METEOR=/home/tclugg/src/meteor/meteor

build: dddppp/frontend/ $(shell find dddppp/frontend/* -type f) ${METEOR}
	cd dddppp/frontend/ && ROOT_URL_PATH_PREFIX=/app ${METEOR} build "../../build" --directory
