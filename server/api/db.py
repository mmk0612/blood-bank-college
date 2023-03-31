import mariadb


conn = mariadb.connect(host="localhost", user="kevqn", password="high", database="bloodbank")
cursor = conn.cursor()

