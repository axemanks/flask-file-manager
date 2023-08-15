# This will be the backend for the app
# It will be a REST API that will be consumed by the frontend
# Display blobs from the database
# Upload pdfs to /data
# Then run prepdocs.ps1

# render_template return files rather than text

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired



app = Flask(__name__)
# Secret Key used for SR form
app.config['SECRET_KEY'] = 'supersecretkey'
# Path to the data folder - was static/files
app.config['UPLOAD_FOLDER'] = '../data/'

# Class for the upload form
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()]) # FileField is a file upload field, InputRequired is a validator that checks if the field is empty or not
    submit = SubmitField('Upload')

# Default route- will display the blobs from the database
@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello from Flask!"

# Route to upload files to the server to be processed
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First get the file
        # path- get os path then add upload folder and secure filename
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))) # Then save the file
        return "File has been uploaded."
    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)