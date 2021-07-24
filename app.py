from flask import Flask

app = Flask(__name__)
app.secret_key = "ddgtvzgtvovpkm53zgvsai5t75hsbmmj3ooaacqtewxbg43cdkca"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
