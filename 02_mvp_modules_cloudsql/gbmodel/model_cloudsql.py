"""
A simple guestbook flask app.
Data is stored in a coludsql database that looks something like the following:

+------------+------------------+------------+----------------+
| Name       | Email            | signed_on  | message        |
+============+==================+============+----------------+
| John Doe   | jdoe@example.com | 2012-05-28 | Hello world    |
+------------+------------------+------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table guestbook (name text, email text, signed_on date, message);

"""
import os
import pymysql
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

from datetime import date
from .Model import Model


class model(Model):
    def __init__(self):
        # Make sure our database exists
        '''
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from guestbook")
        except sqlite3.OperationalError:
            cursor.execute("create table guestbook (name text, email text, signed_on date, message)")
        cursor.close()
	'''

    def open_connection(self):
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

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = self.open_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM guestbook")
        return cursor.fetchall()


    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'email':email, 'date':date.today(), 'message':message}
        connection = self.open_connection()
        cursor = connection.cursor()
        cursor.execute("insert into guestbook (name, email, signed_on, message) VALUES (:name, :email, :date, :message)", params)

        connection.commit()
        cursor.close()
        return True
