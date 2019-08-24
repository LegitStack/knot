from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
# BooleanField incompatible with Materialize
from wtforms.validators import DataRequired


class NewRoleForm(FlaskForm):
    role_name = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField('Save')


class EditRoleForm(FlaskForm):
    role_name = StringField('Role Name', validators=[DataRequired()])
    submit = SubmitField(
        'Save',
        # suboptimal solution - see materialize.css "#submit"
        # render_kw={'class': 'waves-effect waves-light btn'}
    )
