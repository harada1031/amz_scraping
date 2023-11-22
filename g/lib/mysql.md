how to install mysql in ubuntu
================================================================================================================================
To install MySQL on Ubuntu, you can follow these steps:

1. Open a terminal on your Ubuntu machine.

2. Update the package list using the following command:

```bash
sudo apt-get update
```

3. Install the MySQL server package using the following command:

```bash
sudo apt-get install mysql-server
```

4. During the installation process, you will be prompted to set a root password for MySQL. Choose a strong password and remember it as you will need it to log in to MySQL.

5. Once the installation is complete, start the MySQL service using the following command:

```bash
sudo systemctl start mysql
```

6. To ensure that MySQL starts automatically at boot time, run the following command:

```bash
sudo systemctl enable mysql
```

7. Verify that MySQL is running by running the following command:

```bash
sudo systemctl status mysql
```

You should see a message indicating that MySQL is active and running.

You can now connect to MySQL using the root user and the password you set during installation. For example, to connect to MySQL using the command line interface, run the following command:

```bash
mysql -u root -p
```

Enter the root password when prompted and you should be logged in to MySQL.

how to create mysql database on ubuntu server
================================================================
To create a MySQL database on an Ubuntu server, you can follow these steps:

1. Install MySQL server: If you haven't already installed MySQL on your Ubuntu server, you can do so using the following command:

   ```
   sudo apt-get update
   sudo apt-get install mysql-server
   ```

2. Secure the MySQL installation: After installing MySQL, you should secure the installation by running the following command:

   ```
   sudo mysql_secure_installation
   ```

   This command will prompt you to set a root password, remove anonymous users, disallow root login remotely, and remove test databases and access to them.

3. Log in to MySQL: Once you've secured the installation, you can log in to the MySQL server using the following command:

   ```
   sudo mysql -u root -p
   ```

   This command will prompt you to enter the root password you set earlier.

4. Create a new database: After logging in to MySQL, you can create a new database using the following command:

   ```
   CREATE DATABASE mydatabase;
   ```

   Replace `mydatabase` with the name of your desired database.

5. Create a new user and grant privileges: To create a new user and grant privileges to the new database, use the following commands:

   ```
   CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
   GRANT ALL PRIVILEGES ON mydatabase.* TO 'myuser'@'localhost';
   ```

   Replace `myuser` with the username of your desired user and `mypassword` with the password for that user.

6. Exit MySQL: Once you've created the database and user, you can exit the MySQL prompt using the following command:

   ```
   exit;
   ```

That's it! You've now created a new MySQL database on your Ubuntu server and granted privileges to a new user. You can connect to this database using the appropriate credentials from your Python program or other applications.



how to scrape data from website and save the data in mysql table
=
To scrape data from a website and save it in a MySQL table, you can follow these general steps:

1. Install necessary libraries: Install the required libraries for web scraping and MySQL connectivity. For Python, you can use libraries like Beautiful Soup or Scrapy for web scraping, and pymysql or mysql-connector-python for MySQL connectivity. Install them using pip, for example: `pip install beautifulsoup4` and `pip install pymysql`.

2. Import libraries: In your Python script, import the necessary libraries for web scraping and MySQL connectivity. For example:

```python
from bs4 import BeautifulSoup
import requests
import pymysql
```

3. Fetch the webpage: Use the requests library to send an HTTP GET request to the specific URL you want to scrape. For example:

```python
url = "https://www.example.com"
response = requests.get(url)
```

4. Parse the HTML: Use the web scraping library (e.g., BeautifulSoup) to parse the HTML content of the webpage. Extract the desired data using the library's methods. For example:

```python
soup = BeautifulSoup(response.content, "html.parser")
data = soup.find("div", class_="data-class").text
```

5. Connect to MySQL: Establish a connection to your MySQL database using the appropriate credentials. For example:

```python
db = pymysql.connect(host="localhost", user="username", password="password", database="database_name")
cursor = db.cursor()
```

6. Save data to the MySQL table: Use SQL queries to insert the scraped data into the desired table. For example:

```python
sql = "INSERT INTO table_name (column1, column2) VALUES (%s, %s)"
values = (data1, data2)
cursor.execute(sql, values)
db.commit()
```

7. Close the connection: After saving the data, close the MySQL connection. For example:

```python
cursor.close()
db.close()
```

Remember to handle any errors that may occur during the process and ensure that your scraping activities comply with the website's terms of service and legal requirements.


How to connect DB include Port number setting
================================================================
1. using mysql

To set the port when connecting to a MySQL database using Python, you can include the `port` parameter when creating the connection object. Here's an updated example that includes setting the port:

```python
import mysql.connector

# Create a connection object with port
cnx = mysql.connector.connect(user='ihor_user', password='eCZ5xmpfNf6lZ+Ti7N9Eih6D5r8RV9Cm5D+69DkM0VE=',
                              host='91.107.206.223', port='your_port_number', database='ihor_grap')

# Create a cursor object
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM my_table"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection objects
cursor.close()
cnx.close()
```

In this example, replace `'your_port_number'` with the actual port number that your MySQL server is listening on. By including the `port` parameter when creating the connection object, you can specify the desired port for the connection.

Make sure to replace other connection details like the username, password, host, and database name with your own database information.

Remember to keep your database credentials secure and avoid sharing sensitive information like passwords in public spaces.

2. using pymysql

If you are using the `pymysql` module to connect to a MySQL database in Python, you can specify the port number as part of the `connect()` function. Here's an example of how you can connect to a MySQL database using `pymysql` and specify the port number:

```python
import pymysql

# Create a connection object with port
cnx = pymysql.connect(host='91.107.206.223', port=your_port_number, user='ihor_user', password='eCZ5xmpfNf6lZ+Ti7N9Eih6D5r8RV9Cm5D+69DkM0VE=', db='ihor_grap')

# Create a cursor object
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM my_table"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection objects
cursor.close()
cnx.close()
```

In this example, replace `your_port_number` with the actual port number that your MySQL server is listening on. By including the `port` parameter when creating the connection object, you can specify the desired port for the connection.

Make sure to replace other connection details like the username, password, host, and database name with your own database information.

Remember to keep your database credentials secure and avoid sharing sensitive information like passwords in public spaces.


