# Osnovna slika - minimalna verzija Pythona
FROM python:3.12-slim

# Radni folder u kontejneru
WORKDIR /app

# Kopiraj requirements i instaliraj zavisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiraj sav kod
COPY app.py .

# Komanda koja pokreće aplikaciju
CMD ["python", "app.py"]
