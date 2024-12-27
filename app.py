from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Inserisci la tua chiave API di Hugging Face
HUGGINGFACE_API_KEY = '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'  # Sostituisci con la tua chiave API

headers = {
    'Authorization': f'Bearer {HUGGINGFACE_API_KEY}'
}

# Verifica se il server è in esecuzione
@app.route('/')
def index():
    return "Server Flask in funzione!"

# Endpoint per la generazione
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()  # Ottieni i dati dalla richiesta

    if 'prompt' not in data:
        return jsonify({'error': 'Prompt mancante'}), 400  # Se il prompt non è presente

    prompt = data['prompt']

    # URL dell'API Hugging Face (ad esempio per un modello GPT-2)
    api_url = 'https://api-inference.huggingface.co/models/gpt2'  # Sostituisci con il tuo modello

    # Invio della richiesta al modello Hugging Face
    response = requests.post(api_url, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        # Se la richiesta è andata a buon fine, ritorna la risposta
        return jsonify({'response': response.json()[0]['generated_text']})
    else:
        # Se c'è stato un errore, ritorna l'errore
        return jsonify({'error': 'Errore nell\'API di Hugging Face', 'details': response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)



    






 