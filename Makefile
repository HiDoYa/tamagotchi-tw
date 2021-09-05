GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
CYAN   := $(shell tput -Txterm setaf 6)
RESET  := $(shell tput -Txterm sgr0)

TEMP_DIR := package
TERRAFORM_DIR := terraform
ZIP_PACKAGE := tweet_lambda.zip

all: terraform clean

zip: requirements.txt tweet.py
	@echo "Downloading necessary packages"
	@pip3 install --target ./$(TEMP_DIR) -r requirements.txt > /dev/null
	@cp tweet.py package

	@echo "Zipping packages"
	@pushd $(TEMP_DIR) > /dev/null; zip -r $(ZIP_PACKAGE) * > /dev/null; popd > /dev/null

	@cp $(TEMP_DIR)/$(ZIP_PACKAGE) terraform
	@echo "${GREEN}\nYou may now run 'terraform apply' in the terraform folder${RESET}"

terraform: zip terraform/*
	@echo "Applying terraform"
	@pushd $(TERRAFORM_DIR) > /dev/null; terraform apply -auto-approve; popd > /dev/null

clean:
	@echo "Cleaning up"
	@rm -rf $(TEMP_DIR) $(ZIP_PACKAGE)
	