if [[ $1 == "build" ]]; then
	 docker run --rm -u $(id -u):$(id -g) -v $PWD:/data latex-machine make
fi

if [[ $1 == "docker" ]]; then
	docker build -t latex-machine .
fi
