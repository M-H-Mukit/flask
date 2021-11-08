from flask import Flask, render_template, send_file
import random
import string
import time
import sys
from dotenv import load_dotenv
from helper import *

load_dotenv()

app = Flask(__name__)

GENERATED_FILE_NAME = "output.txt"
FILE_SIZE = 2097152  # binary byte size of 2mb
ALPHABETICAL_STRING_MIN_LENGTH = 1  # random choice
ALPHABETICAL_STRING_MAX_LENGTH = 50  # random choice
INTEGER_MAX_LENGTH = 500000  # random choice


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/generatefile")
def generate_file():
    is_first_obj = True
    try:
        output_str = ""

        while len(output_str) < FILE_SIZE:
            if is_first_obj == False:
                output_str += ","
            is_first_obj = False

            random_obj = random.choice([
                generate_random_alphabetical_string(
                    ALPHABETICAL_STRING_MIN_LENGTH, ALPHABETICAL_STRING_MAX_LENGTH),
                generate_random_real_number(INTEGER_MAX_LENGTH),
                generate_random_integer(INTEGER_MAX_LENGTH),
                generate_random_alphanumeric(
                    ALPHABETICAL_STRING_MIN_LENGTH, ALPHABETICAL_STRING_MAX_LENGTH)
            ])
            output_str += str(random_obj)

        with open(GENERATED_FILE_NAME, 'w') as file:
            file.write(output_str)

        return {'output_file_name': GENERATED_FILE_NAME}, 200
    except:
        return {'error': 'Something went wrong won server'}, 500


@app.route("/api/downloadfile")
def download_file():
    try:
        return send_file(GENERATED_FILE_NAME, as_attachment=True)
    except:
        return {'error': 'Something went wrong won server'}, 500


@app.route("/api/getreport")
def get_report():
    try:
        total_alphabetical_strings = 0
        total_real_numbers = 0
        total_integers = 0
        total_alphanumerics = 0

        with open(GENERATED_FILE_NAME, 'r') as file:
            file_str = file.read()

        random_objects = file_str.split(',')

        for current_object in random_objects:
            if is_alphabetical_string(current_object):
                total_alphabetical_strings += 1
            elif is_integer(current_object):
                total_integers += 1
            elif is_real_number(current_object):
                total_real_numbers += 1
            else:
                total_alphanumerics += 1

        return {
            'alphabetical_strings': total_alphabetical_strings,
            'real_numbers': total_real_numbers,
            'integers': total_integers,
            'alphanumerics': total_alphanumerics,
        }
    except:
        return {'error': 'Something went wrong won server'}, 500
