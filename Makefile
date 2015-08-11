METEOR=$(shell which meteor)

build: dddppp/frontend/ $(shell find dddppp/frontend/* -type f) ${METEOR}
	cd dddppp/frontend/ && ${METEOR} build "../../build" --directory
