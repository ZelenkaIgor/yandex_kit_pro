from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/index')
def index():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/help.css')}" />
                    <title>Спасение котят^^</title>
                  </head>
                  <body>
                  <h1>"You become responsible, forever, for what you have tamed"</h1>
                  </body>
                </html>"""



@app.route('/')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/help.css')}" />
                    <title>Спасение котят^^</title>
                  </head>
                  <body>
                  </body>
                </html>"""


@app.route('/promotion')
def return_samp():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/help.css')}" />
                    <title>Спасение котят^^</title>
                  </head>
                  <body>
                  <strong>Как помочь приютам ?</strong>
                  <br> 
                  <br> 1. Распространение информации – один из главных способов помочь приютам для животных. 
                  <br> 2. Материальная помощь.
                  <br> 3. В приютах часто не хватает рук и нужна любая помощь волонтеров.
                  <br> 4. Но самая лучшая помощь это, несомненно, взять животное домой.
                  </body>
                </html>"""


@app.route('/grey_kitten')
def return_picture():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                      <h1>Спасем братьев наших меньших!</h1>
                      <img src="/static/img/cat.jpg">
                      </body>
                    </html>"""


@app.route('/anketa_for_work', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Анкета волонтера</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="name">
                                    <br> <input type="password" class="form-control" id="password" placeholder="Введите почту" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Были ли у вас домашние животные?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Нет</option>
                                          <option>Да, одно</option>
                                          <option>Да, два</option>
                                          <option>Да, более трех</option>
                                        </select>
                                     </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Чем вы готовы заниматься в приюте?</label>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Покупать корм
 </label>
 </div>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Убирать клетки
 </label>
 </div>
 <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Строить новые вольеры
 </label>
 </div>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Вычесывать шерсть
 </label>
 </div>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Выгуливать собак
 </label>
 </div>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Заниматься агитационной деятельностью (распространять иинформацию)
 </label>
 </div>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Искать новых хозяев бедным животным
 </label>
 </div>
                                        <div class="form-check">
 <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
 <label class="form-check-label" for="navigator">
 Взять кого-то на попечение 
 </label>
 </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')