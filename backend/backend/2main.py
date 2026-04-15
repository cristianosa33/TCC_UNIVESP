from flask import request, redirect
from werkzeug.utils import secure_filename

# Pasta onde as fotos serão salvas
UPLOAD_FOLDER = '../static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/registrar', methods=['POST'])
def registrar_demanda():
    categoria = request.form.get('categoria')
    descricao = request.form.get('descricao')
    lat = request.form.get('latitude')
    lng = request.form.get('longitude')
    
    # Tratamento da Imagem
    file = request.files['foto']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        foto_url = f"uploads/{filename}"
    
    # Aqui entraria a lógica de salvar no banco de dados (SQL INSERT)
    print(f"Nova demanda: {categoria} em {lat}, {lng}")
    
    return redirect('/') # Volta para o mapa após registrar
