# Martians Attack

This is a simple project to demostrate the interaction
between LLM agents.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/000paradox000/martians-attack.git
   cd martians-attack
   ```

2. Setup the environment:
   Create a virtualenv and pull the necessary model and install required
   packages using the commands:
   ```bash
   make init
   ```

## Usage

- Run the main program:
  ```bash
  make run
  ```

- Run with logging:
  ```bash
  make run_with_log
  ```

## Testing

- Run all tests:
  ```bash
  make test
  ```

- Run specific tests for some modules:
  ```bash
  make test.martian
  make test.tts
  make test.translator
  ```

## Run in jupyter notebook

  ```bash
  make notebooks.run
  ```

## Run in docker

  ```bash
  make docker.up
  ```

  ```bash
  make docker.down
  ```
