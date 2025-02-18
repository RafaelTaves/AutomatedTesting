import requests
import json
from difflib import SequenceMatcher

test_files = [
    ("documento1.pdf", {"nome": "João Silva", "cpf": "123.456.789-00"}),
    ("documento2.jpg", {"data": "10/02/2024", "valor": "R$ 500,00"})
]

API_URL = "http://127.0.0.1:8000/extract" 

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def test_api():
    for file_path, expected_output in test_files:
        with open(file_path, "rb") as file:
            response = requests.post(API_URL, files={"file": file})
            extracted_data = response.json()
            
        sim_score = similarity(extracted_data["nome"], expected_output["nome"])
        
        print(f"Testando {file_path}...")
        print("Extraído:", extracted_data)
        print("Esperado:", expected_output)
        
        if extracted_data == expected_output:
            print("✅ Teste passou!\n")
        else:
            print("❌ Teste falhou!\n")
        
        print(f"Similaridade: {sim_score:.2%}")

test_api()
