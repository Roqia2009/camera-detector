FROM python:3.11-slim

# التعديل هنا: استخدمنا المكتبات المتوافقة مع التوزيعة الجديدة لـ OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY video.mp4 .

CMD ["python", "main.py"]