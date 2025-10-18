import time
import mysql.connector
from mysql.connector import Error

def insert_data(connection, cursor, latitude, longitude):
    try:
        insert_query = """INSERT INTO gps_data (received, latitude, longitude)
                          VALUES (NOW(), %s, %s)"""
        cursor.execute(insert_query, (latitude, longitude))
        connection.commit()
        print(f"Data inserted: Latitude = {latitude}, Longitude = {longitude}")
    except Error as e:
        print(f"Error while inserting data: {e}")

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='210.123.42.48',
            port=3306,
            database='mysql',
            user='uam',
            password='qwer1234',
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            print("Connection established")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def main():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        # 초기 위도와 경도 설정
        latitude = 37.6108600168484
        longitude = 126.995701407384
        try:
            while True:
                insert_data(connection, cursor, latitude, longitude)
                # 마지막 소수점 자리에서 1씩 증가
                latitude = round(latitude + 0.00000000001, 13)
                longitude = round(longitude + 0.00000000001, 13)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program interrupted by user")
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    main()
