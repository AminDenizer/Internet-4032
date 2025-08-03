# tcp_server/Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY tcp_server.py .

EXPOSE 23456/tcp

CMD ["python", "tcp_server.py"]
