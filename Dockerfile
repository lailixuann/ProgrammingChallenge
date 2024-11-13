FROM python:3.9-slim
WORKDIR /app

COPY challengeB.py /app/challengeB.py
COPY output.txt /app/output.txt

RUN mkdir /app/output

CMD ["python", "challengeB.py", "/app/output.txt", "/app/output/output_challengeB.txt"]
# CMD ["python3", 'challengeB.py']