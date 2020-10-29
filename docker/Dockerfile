FROM python:3.6-alpine
WORKDIR /app
RUN apk add --update --no-cache \
	libxml2 \
	libxslt \
	g++ \
	gcc \
	libxslt-dev
COPY requirements.txt .
RUN pip install --upgrade pip && \
	pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "-u", "main.py"]
