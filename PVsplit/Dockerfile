FROM python:3.11

WORKDIR /pv_split

COPY /requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY pv_split /pvsplit

CMD ["python", "main.py"]