from flask import Flask, url_for, request
import datetime

from flask import Flask, render_template, request, abort
from data import db_session
from data.users import User
from data.news import News
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from app.forms.login import LoginForm
from werkzeug.utils import redirect

from app.forms.news import NewsForm
from app.forms.user import RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


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
                  <br><a> 1. Распространение информации – один из главных способов помочь приютам для животных. </a>
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
                      <img src="/static/img/cat_1.jpg">
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


@app.route('/carousel')
def carousel_ka():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                        <title>Карусель</title>
                    <title>Карусель?</title>
                      </head>
                      <body>
                      <h1>Грустные фото приютов :(</h1>
                      <div class="container">
                          <div id="carousel-basic" class="carousel slide" data-ride="carousel">
                          <ol class="carousel-indicators">
                <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                <li data-target="carousel-basic" data-slide-to="1"></li>
                <li data-target="carousel-basic" data-slide-to="2"></li>
                <li data-target="carousel-basic" data-slide-to="3"></li>
            </ol>
            <div class="carousel-inner" role="listbox">
                <div class="carousel-item active">
                    <img src="{url_for('static', filename='img/imgpreview.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/dogs.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/kitten.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
                <div class="carousel-item">
                    <img src="{url_for('static', filename='img/priyut.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                </div>
            </div>
            <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Назад</span>
            </a>
            <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Вперед</span>
            </a>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

                      </body>
                    </html>"""


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private is not True)
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/checkes',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление чека',
                           form=form)


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html',
                           title='Редактирование чека',
                           form=form
                           )


@app.route('/check_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')