#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
from flask import Flask, url_for, render_template, redirect, jsonify
from flask import send_from_directory, session, flash


# Globals #####################################################################

app = Flask(__name__)


# helpers #####################################################################

def get_side_nav():
    return {
        'heading 1': {'page name': 'dashboard'},
        'heading 2': {'sub heading': {'page name': 'dashboard'}}, }


def start_response(name) -> dict:
    return {
        'title': name.replace('__', ' ').replace('_', ' ').title(),
        'sidenavs': get_side_nav(), }


# ERRORS ######################################################################

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


# STATIC PAGES ################################################################

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static/img/favicon'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/generated/<path:path>')
def send_generated(path):
    return send_from_directory('generated', path)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'now': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})


@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/dashboard')
def dashboard():
    resp = start_response(sys._getframe().f_code.co_name)
    favorites = {'name': {
        'path_url': 'dashboard',
        'path_hierarchy': 'here',
        'type': 'unknown'}}
    resp = {**resp, **{
        'title': 'Template',
        'favorites': favorites}}
    return render_template('dashboard.html', **resp)


# #############################################################################

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    if os.name == 'nt':
        app.run(host='0.0.0.0', port=5000, use_reloader=True, debug=True)
    else:
        app.run(host='0.0.0.0', port=5000, use_reloader=False)
