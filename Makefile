# =============================================================================

# Setup the initial environment by pulling the llama model
setup:
	ollama pull llama3.2:1b

# Install necessary Python packages
requirements.install:
	pip install -U pip
	pip install -r requirements.txt

# Initialize the project setup and install requirements
init: setup requirements.install

# =============================================================================

# Run pre-commit checks on all files
pre-commit.run:
	pre-commit run --all-files
	pre-commit run --all-files

# Update pre-commit hooks
pre-commit.update:
	pre-commit autoupdate

# =============================================================================

# Run all tests with detailed output
test:
	python -m pytest \
		-vv \
		-s \
		--log-cli-level=DEBUG \

# Run specific tests with detailed output for the TTS module
test.tts:
	python -m pytest \
		-s \
		--log-cli-level=DEBUG \
		-vv \
		tests/test_tts.py

# Run specific tests with detailed output for the Martian module
test.martian:
	python -m pytest \
		-s \
		--log-cli-level=DEBUG \
		-vv \
		tests/test_martian.py

# Run specific tests with detailed output for the Translator module
test.translator:
	python -m pytest \
		-s \
		--log-cli-level=DEBUG \
		-vv \
		tests/test_translator.py

# =============================================================================

# Execute the main program
run:
	@python main.py

# Run the main program and redirect output to a log file
run_with_log:
	$(MAKE) run > /tmp/output.log 2>&1

# =============================================================================

# Run jupyter notebook
notebooks.run:
	jupyter lab \
		--ip=0.0.0.0 \
		--port=9088 \
		--allow-root \
		--NotebookApp.token='' \
		--NotebookApp.password=''

# =============================================================================

# Run in docker
docker.up:
	docker-compose up --build

docker.down:
	docker-compose down --volumes --remove-orphans
