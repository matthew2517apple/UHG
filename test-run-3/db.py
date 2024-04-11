# db.py model
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn

def get_branches():
    conn = open_connection()
    with conn.cursor() as cursor:
        #result = 
        cursor.execute('SELECT * FROM branch;')
        branches = cursor.fetchall()
        return branches    

def get_customers():
    conn = open_connection()
    with conn.cursor() as cursor:
        #result = 
        cursor.execute('SELECT * FROM customer;')
        customers = cursor.fetchall()
        return customers  

def get_one_branch(name):
    conn = open_connection()
    with conn.cursor() as cursor:
        #result = 
        cursor.execute("SELECT * FROM branch WHERE branch_name = %s", [name])
        branch = cursor.fetchone()
        return branch        

def create(name, city, assets):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO branch (branch_name, branch_city, assets) VALUES(%s, %s, %s)',
                       (name, city, assets))
    conn.commit()
    conn.close()
