# Sử dụng Python chính thức
FROM theodorescsa/ezpdf-lib-requirements:latest

# Đặt biến môi trường để ngăn pip tạo cache
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Cài đặt các gói hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    && apt-get clean

# Sao chép file requirements.txt và cài đặt dependencies Python
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn mysqlclient

# Sao chép toàn bộ mã nguồn
WORKDIR /app
COPY . .

# Expose port
EXPOSE 8000

# Chạy Gunicorn server
CMD ["gunicorn", "EzPDF.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
