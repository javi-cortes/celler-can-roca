help:
	@echo "run                                -- Run the script"

run:
	@docker build . -t canroca && docker run -it canroca

.PHONY: run
