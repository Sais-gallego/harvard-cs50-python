# Harvard University: CS50P (Programming with Python)

![Build Status](https://github.com/Sais-gallego/harvard-cs50-python/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Course](https://img.shields.io/badge/Harvard-CS50P-crimson.svg)

Implementaciones completas de laboratorios, validaciones avanzadas con expresiones regulares, modelado orientado a objetos (OOP), manejo de excepciones y pruebas unitarias del programa oficial de **Harvard University: CS50's Introduction to Programming with Python (CS50P)**, impartido por el profesor **David J. Malan**.

**Autor:** Sergio Andrés Ipuz Saavedra  
**GitHub:** [@Sais-gallego](https://github.com/Sais-gallego)  
**Institución:** Harvard University (CS50)

---

## 🐍 Núcleos del Programa CS50P

### 1. Validaciones con Expresiones Regulares (`src/core_programming.py`)
- **NUMB3RS:** Validación estricta de direcciones IPv4 asegurando el rango $[0, 255]$ por cada octeto mediante grupos de captura regex.
- **Watch on YouTube:** Extracción de enlaces de inserción `<iframe>` y normalización a URLs canónicas compartibles `https://youtu.be/<id>`.
- **Working 9 to 5:** Conversión bidireccional y formateo de horarios de 12 horas a formato estándar militar de 24 horas (`HH:MM to HH:MM`).

### 2. Algoritmos Clásicos: Algoritmo de Luhn (CS50 Credit)
- Validación de sumas de comprobación de tarjetas de crédito y clasificación por emisor bancario (American Express, MasterCard, Visa).

### 3. Programación Orientada a Objetos - OOP (Semana 8)
- Clase `Jar` con encapsulamiento, getters/setters (`@property`), validación estricta de capacidad, excepciones personalizadas (`ValueError`) y sobrecarga de métodos dunder `__str__` (renderizado de galletas `🍪`).

---

## 🧪 Pruebas Automatizadas

```bash
python -m unittest discover tests -v
```

### Resultados de la Suite (5/5 Passed ✅)
```text
test_jar_oop_model ... ok
test_luhn_credit_card_brand_identification ... ok
test_numb3rs_ipv4_validation ... ok
test_working_9_to_5_conversion ... ok
test_youtube_embed_extraction ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```
