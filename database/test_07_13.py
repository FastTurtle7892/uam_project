from flask import Flask, render_template
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app)

def get_lat_lon(index):
    con = sqlite3.connect('C:/Users/user/database/gps.db')
    cur = con.cursor()
    cur.execute('SELECT LAT, LON FROM Signal')
    rows = cur.fetchall()
    con.close()
    if index < len(rows):
        return rows[index]  # 특정 인덱스의 위치 반환
    return None

locations_index = 0  # 위치 인덱스 초기화

@app.route('/')
def main():
    return render_template('test.html')

@socketio.on('request_location')
def handle_request_location():
    global locations_index
    location = get_lat_lon(locations_index)
    if location:
        socketio.emit('update_location', {'lat': location[0], 'lon': location[1]})
        locations_index += 1  # 다음 위치로 인덱스 증가
    else:
        locations_index = 0  # 인덱스 초기화

if __name__ == '__main__':
    socketio.run(app, port=8000, debug=True)
