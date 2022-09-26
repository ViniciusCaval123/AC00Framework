import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'ac02'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  preco = request.form['preco']
  categoria_produto = request.form['categoria_produto']
  if nome and preco and categoria_produto:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_produto (nome, preco, produto) VALUES (%s, %s, %s)', (nome, preco, categoria_produto))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome, preco, produto from tbl_produto')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
