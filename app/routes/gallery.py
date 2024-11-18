# routes/gallery.py

from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from app import db
from app.forms.gallery_form import GalleryForm
from app.models.gallery import Gallery

gallery = Blueprint('gallery', __name__)

UPLOAD_FOLDER = 'app/static/images/gallery'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@gallery.route('/gallery', methods=['GET'])
def list_gallery():
    images = Gallery.query.all()
    return render_template('gallery.html', images=images)

@gallery.route('/gallery/new', methods=['GET', 'POST'])
def new_gallery_image():
    form = GalleryForm()
    if form.validate_on_submit():
        file = form.image.data
        if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            image_url = f'static/images/gallery/{filename}'
            new_image = Gallery(image_url=image_url, description=form.description.data)
            db.session.add(new_image)
            db.session.commit()
            flash('Image uploaded successfully!', 'success')
            return redirect(url_for('gallery.list_gallery'))
    return render_template('new_gallery_image.html', form=form)

