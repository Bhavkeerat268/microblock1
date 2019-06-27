from app import app
@app.route('/index')
def index():
    a='Divyam'
    b='Singh'
    return str(a + b)


    
    
