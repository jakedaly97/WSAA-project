# dao/event_dao.py

import mysql.connector
import dbconfig as cfg

class EventDAO:
    connection = ""
    cursor = ""
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM event"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM event WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, event):
        cursor = self.getcursor()
        sql = "INSERT INTO event (title, date, location, description) VALUES (%s, %s, %s, %s)"
        values = (event.get("title"), event.get("date"), event.get("location"), event.get("description"))
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        event["id"] = newid
        self.closeAll()
        return event

    def update(self, id, event):
        cursor = self.getcursor()
        sql = "UPDATE event SET title = %s, date = %s, location = %s, description = %s WHERE id = %s"
        values = (event.get("title"), event.get("date"), event.get("location"), event.get("description"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM event WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, resultLine):
        attkeys = ['id', 'title', 'date', 'location', 'description']
        event = {}
        currentkey = 0
        for attrib in resultLine:
            event[attkeys[currentkey]] = attrib
            currentkey += 1
        return event