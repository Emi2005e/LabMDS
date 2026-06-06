# Folosim o imagine oficială și minimalistă de Python
FROM python:3.11-slim

# Setăm directorul de lucru în interiorul containerului
WORKDIR /app

# Copiem fișierul cu pachete în container
COPY requirements.txt .

# Instalăm pachetele necesare (în cazul nostru, librăria 'requests')
RUN pip install --no-cache-dir -r requirements.txt

# Copiem scriptul aplicației meteo
COPY main.py .

# Comanda care se va executa la pornirea containerului
CMD ["python", "main.py"]

