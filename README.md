# Programming Challenge
This repository contains solutions for **Challenge A**, **Challenge B**, and **Challenge C**, that demonstrates generating, processing, and Dockerizing a Python script that reads and processes randomly generated data from a file. Docker ensures that the solution can be run in any environment with Docker installed.

**1. Challenge A** (challengeA.py):
   - Generate random objects (alphabetical strings, integers, real numbers, alphanumerics) and store them in a file (`output.txt`).
   - The objects are separated by commas and the file is 10MB in size.

**2. Challenge B** (challengeB.py):
   - Process the `output.txt` file from Challenge A.
   - Identify the type of each object (alphabetical string, integer, real number, alphanumeric).
   - Strip spaces from the alphanumeric objects and save the processed results to `output/output_challengeB.txt`.

**3. Challenge C** (Dockerfile):
   - Dockerize the entire project so that it can be easily built and executed in a containerized environment.
   - The input file (`output.txt`) is passed into the container, processed by the script, and the results are saved to an output file on the host machine.

  
## Requirements
- Docker installed on your machine.
- Python 3.9 or later (used within the Docker container).


## Instructions
### 1. Build the Docker Image

```bash
docker build -t challengeb_image .
```
### 2. Run the Docker Container
```bash
docker run --rm -v "$(pwd)/output:/app/output" challengeb_image
```

### 3. View the processed results
```bash
cat output/output_challengeB.txt
```
