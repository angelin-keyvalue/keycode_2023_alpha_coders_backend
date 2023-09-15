import os
import zipfile

from app import db
from app.routes import bp
from app.models.document import Document
from app.models.elder import Elder

from flask import jsonify, request, send_file, Response
from flask_cors import cross_origin


ALLOWED_FILE_EXTENSIONS = {'pdf'}
DOCUMENT_UPLOAD_FOLDER = 'app/elder_documents'
DOCUMENT_UPLOAD_FOLDER_FOR_SEND_FILE = 'elder_documents'

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXTENSIONS

@bp.route('/doc/<int:id>/upload', methods=['POST'])
@cross_origin(origin='*')
def upload_doc(id):
    if 'file' not in request.files:
        return jsonify({"msg": "No file uploaded"}), 400

    elder = Elder.query.get(id)
    if not elder:
        return jsonify({'error': 'Elder not found'}), 404

    file = request.files['file']
    if file and is_allowed_file(file.filename):
        file_path = os.path.join(DOCUMENT_UPLOAD_FOLDER, str(elder.id))
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        try:
            file.save(os.path.join(file_path, file.filename))
            new_doc = Document(doc_name=file.filename, elder_id=id)
            db.session.add(new_doc)
            db.session.commit()
            return jsonify({"msg":"Upload successful", "id": new_doc.id}), 200
        except Exception:
            return jsonify({"msg":"Upload failed. Something went wrong"}), 200
    return jsonify({"msg":"Upload failed. Allowed formats: PDF"}), 200


@bp.route('/doc/<int:id>/all', methods=['GET'])
@cross_origin(origin='*')
def list_docs(id):
    elder = Elder.query.get(id)
    if not elder:
        return jsonify({'error': 'Elder not found'}), 404

    folder_path = os.path.join(DOCUMENT_UPLOAD_FOLDER, str(id))
    files = os.listdir(folder_path)

    if not files:
        return {"msg": "No files available!"}, 404
    
    try:
        zip_filename = 'uploaded_docs.zip'
        zip_path = os.path.join(folder_path, zip_filename)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                file_path = os.path.join(folder_path, file)
                zipf.write(file_path, file)
        
        with open(zip_path, 'rb') as zip_file:
            response = Response(zip_file.read())
            response.headers['Content-Type'] = 'application/zip'
            response.headers['Content-Disposition'] = 'attachment; filename=uploaded_docs.zip'

        os.remove(zip_path)
        return response
    except Exception:
        return {"msg": "Something went wrong listing files"}, 404


@bp.route('/doc/<int:id>', methods=['GET'])
@cross_origin(origin='*')
def get_doc_by_id(id):
    document = Document.query.get(id)
    if not document:
        return {"msg": "No files available!"}, 404

    file_name = document.doc_name
    file_path = os.path.join(DOCUMENT_UPLOAD_FOLDER_FOR_SEND_FILE,str(id),file_name)
    return send_file(file_path, mimetype='application/pdf')
