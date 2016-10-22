from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import EnterChatroom, InitializeChatrooms


@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = EnterChatroom()
    if form.validate_on_submit():
        session['name'] = 'Anonymous'
        print('---------------')
        print(session)
        print(session.__dict__)
        print('---------------')
        return redirect(url_for('.chat'))
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    if name == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name)

@main.route('/volunteer', methods=['GET', 'POST'])
def volunteer_welcome():
    form = InitializeChatrooms()
    if form.validate_on_submit():
        session['name'] = 'Volunteer'
        print('---------------')
        print(session)
        print(session.__dict__)
        print('---------------')
        return redirect(url_for('.chat'))

    return render_template('volunteer.html', form=form)

