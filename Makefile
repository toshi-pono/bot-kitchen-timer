.PHONY: generate
generate:
	@echo "Generating requirements.txt"
	rm -f requirements.txt
	cat requirements.lock | sed '/-e/d' > requirements.txt