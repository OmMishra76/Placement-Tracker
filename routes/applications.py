from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db
from models.application import Application
from datetime import datetime

applications = Blueprint('applications', __name__)


@applications.route('/applications/new', methods=['GET', 'POST'])
@login_required
def new_application():
    if request.method == 'POST':
        company = request.form.get('company')
        role = request.form.get('role')
        job_link = request.form.get('job_link')
        apply_date_str = request.form.get('apply_date')
        deadline_str = request.form.get('deadline')     
        apply_date = datetime.strptime(apply_date_str, '%Y-%m-%d').date() if apply_date_str else None
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
        status = request.form.get('status')
        resume_version = request.form.get('resume_version')
        notes = request.form.get('notes')

        new_app = Application(
            user_id=current_user.id,
            company=company,
            role=role,
            job_link=job_link,
            apply_date=apply_date,
            deadline=deadline,
            status=status,
            resume_version=resume_version,
            notes=notes
        )

        db.session.add(new_app)
        db.session.commit()

        flash('Application added successfully!')
        return redirect(url_for('applications.list_applications'))

    return render_template('applications/new.html')


@applications.route('/applications')
@login_required
def list_applications():
    user_applications = Application.query.filter_by(user_id=current_user.id).order_by(Application.created_at.desc()).all()
    return render_template('applications/list.html', applications=user_applications)