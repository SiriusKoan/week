FROM python:3.10-slim
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
