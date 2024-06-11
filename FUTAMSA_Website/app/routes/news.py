# routes/news.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.forms.news_form import NewsForm
from app.models.news import News

news = Blueprint('news', __name__)

@news.route('/news', methods=['GET'])
def list_news():
    news_items = News.query.all()
    return render_template('news.html', news_items=news_items)

@news.route('/news/new', methods=['GET', 'POST'])
def new_news():
    form = NewsForm()
    if form.validate_on_submit():
        new_news = News(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(new_news)
        db.session.commit()
        flash('News article created successfully!', 'success')
        return redirect(url_for('news.list_news'))
    return render_template('new_news.html', form=form)

@news.route('/news/<int:id>/edit', methods=['GET', 'POST'])
def edit_news(id):
    news_item = News.query.get_or_404(id)
    form = NewsForm(obj=news_item)
    if form.validate_on_submit():
        news_item.title = form.title.data
        news_item.content = form.content.data
        db.session.commit()
        flash('News article updated successfully!', 'success')
        return redirect(url_for('news.list_news'))
    return render_template('edit_news.html', form=form, news_item=news_item)
