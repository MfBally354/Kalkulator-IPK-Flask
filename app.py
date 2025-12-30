from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

# File untuk menyimpan data
DATA_FILE = 'ipk_data.json'

# Fungsi untuk load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Fungsi untuk save data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Fungsi hitung IPK
def hitung_ipk(mata_kuliah):
    """
    mata_kuliah: list of dict dengan format:
    [
        {'nama': 'Matematika', 'sks': 3, 'nilai': 'A'},
        {'nama': 'Fisika', 'sks': 4, 'nilai': 'B'},
    ]
    """
    konversi_nilai = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'D': 1.0,
        'E': 0.0
    }
    
    total_bobot = 0
    total_sks = 0
    
    for mk in mata_kuliah:
        sks = int(mk['sks'])
        nilai = konversi_nilai.get(mk['nilai'].upper(), 0)
        total_bobot += sks * nilai
        total_sks += sks
    
    if total_sks == 0:
        return 0.0
    
    ipk = total_bobot / total_sks
    return round(ipk, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        mata_kuliah = data.get('mata_kuliah', [])
        
        if not mata_kuliah:
            return jsonify({'error': 'Data mata kuliah kosong'}), 400
        
        # Hitung IPK
        ipk = hitung_ipk(mata_kuliah)
        
        # Simpan hasil
        result = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'mata_kuliah': mata_kuliah,
            'ipk': ipk
        }
        
        # Load data lama dan tambahkan data baru
        all_data = load_data()
        all_data.append(result)
        save_data(all_data)
        
        return jsonify({
            'success': True,
            'ipk': ipk,
            'total_matkul': len(mata_kuliah)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def history():
    data = load_data()
    # Reverse agar data terbaru di atas
    data.reverse()
    return render_template('history.html', data=data)

@app.route('/clear-history', methods=['POST'])
def clear_history():
    save_data([])
    return redirect(url_for('history'))

@app.route('/api/history')
def api_history():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
