testDIR = Src/tests/
t ?= teste


start:
	@python Src/main.py

tests:
	@python -m unittest discover -s $(testDIR)** -p "*.py"
test:
	@python -m unittest discover -s $(testDIR)** -p "$(t).py"

clear:
	@find . -name "*.pyc" -exec rm -f {} \;

help:
	@echo "start         - Start the program"
	@echo "tests         - Run all tests"
	@echo "test t=<name> - Run a specific test"
	@echo "clear         - Remove all .pyc files"
.PHONY: start tests test
