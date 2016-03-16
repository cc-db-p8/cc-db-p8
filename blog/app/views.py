# coding=utf-8
from flask import Flask, url_for, render_template, request, redirect
import models
app = Flask(__name__)

@app.route('/')
@app.route('/<id>')
def hello_world(id=None):
    full = request.args.get('full', False)
    if request.method == 'GET':
        pass
    elif resquest.method == 'POST':
        pass
    user = models.User.get_user('toot')

    posts = models.Post.get_posts(user['username'])
    for post in posts:
        commentaires = models.Commentaire.get_commentaires(post['id'])
        post['commentaires'] = commentaires
        post['nb_com'] = len(commentaires)
    return render_template('index.html',
                           posts = posts,
                           titre='mon titre',
                           full=full)


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    champs = [
        'titre',
        'contenu'
    ]

    if request.method == 'GET':
        return render_template('post.html', champs=champs, form={}, errors={})
    else:
        form = request.form
        result =  validate(form, champs)

        if result['valid']:
            user = models.User.get_user('toot')
            models.Post.insert('toot', result['form']['titre'], result['form']['contenu'])
            return redirect('/')

        else:
            return render_template('post.html',
                                   champs=champs,
                                   form=result['form'],
                                   errors=result['errors'])


def validate(form, champs):
    result = {'valid': True, 'form': form, 'errors': {}}
    for champ in champs:
        result['valid'] = result['valid'] and champ_requis(form, champ, errors=result['errors'])

    return result

def champ_requis(form, champ, errors):
    if form.get(champ, None) == '':
        errors[champ] = 'le champ {} est requis'.format(champ)
        return False
    else:
        return True
