import mysql.connector
import datetime


class Database:
    def __init__(self, host_name, user_name, password, db_name):
        self.db = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password,
            database=db_name
        )

    def insert_meas(self, value, id_topic):
        sql = "INSERT INTO measurment (createTime, value, idTopic) VALUES (%s, %s, %s)"
        val = (datetime.datetime.now(), value, id_topic)
        self.db.cursor().execute(sql, val)
        self.db.commit()

    def select_id(self, topic):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT idTopic FROM topic WHERE name=%s", (topic,))
        return mycursor.fetchone()
