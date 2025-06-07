from flask import Blueprint, render_template, request, redirect, url_for
from models.comentario import Comentario
from database.db_config import db

comentario_bp = Blueprint('comentario', __name__)
comentario_model = Comentario()

@comentario_bp.route('/encuesta', methods=['GET', 'POST'])
def gestionar_comentarios():
    if request.method == 'POST':
        datos = {
            'Nombre': request.form['nombre'],
            'Correo': request.form['correo'],
            'Informacion': request.form.get('p1'),
            'Satisfecho': request.form.get('p2'),
            'Visuales': request.form.get('p3'),
            'Compra': request.form.get('p4'),
            'Recomendacion': f"{request.form.get('p5')} - {request.fprm.get('comentario1')}",
            'Mejoras': request.form.get('comentario2')
        }
        comentario_model.guardar_comentario(datos)
        return redirect(url_for('comentario.gestionar_comentarios'))

    comentarios = comentario_model.obtener_comentarios()
    return render_template('encuesta.html', comentarios=comentarios)
