# routes/event.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.forms.event_form import EventForm
from app.models.event import Event

event = Blueprint('event', __name__)

@event.route('/events', methods=['GET'])
def list_events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@event.route('/events/new', methods=['GET', 'POST'])
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            location=form.location.data
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('event.list_events'))
    return render_template('new_event.html', form=form)

@event.route('/events/<int:id>/edit', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.get_or_404(id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.date = form.date.data
        event.location = form.location.data
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('event.list_events'))
    return render_template('edit_event.html', form=form, event=event)
