.PHONY: help prod dev test version flake

VERSION = 0.0.1

help:
	@echo "Smart Vehicle Access cloud"
	@echo "-----------------------"
	@echo ""
	@echo "Run source code check"
	@echo "    make code-check"
	@echo ""
	@echo "See contents of Makefile for more targets."

.DEFAULT_GOAL := help

code-check: ## Syntax check by flake
	flake8 server

version: ## Output the current version
	@echo $(VERSION)