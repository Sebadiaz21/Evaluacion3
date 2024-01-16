from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio= None
    estado= None
    if request.method == 'POST' :
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asis = float(request.form['asis'])
        promedio=(nota1+nota2+nota3)/3
        if promedio>=40 and asis >=75:
            estado = 'Aprobado'
        else:
            estado='Reprobado'

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nomlar= None
    lon= None
    if request.method == 'POST':
        nom1=request.form['nom1']
        nom2=request.form['nom2']
        nom3=request.form['nom3']
        largo1= len(nom1)
        largo2= len(nom2)
        largo3= len(nom3)
        if largo1 > largo2 and largo3:
            nomlar=largo1
            nom=nom1
        elif largo2> largo1 and largo3:
            nomlar=largo2
            nom=nom2
        else:
            nomlar=largo3
            nom=nom3
        lon=nom
    return render_template('ejercicio2.html', nomlar=nomlar, lon=lon)


if __name__ == '__main__':
    app.run(debug=True)