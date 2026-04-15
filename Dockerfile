From python:3.10-slim
    
WORKDIR /mon-app

COPY mon-app/ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"] 