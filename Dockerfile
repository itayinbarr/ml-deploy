FROM python:3.9-slim AS builder
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY src/ src/
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
CMD ["python", "src/app.py"]
