# Tutorial for running code
____
## For running code
Tips which u **should follow**:
- Connect to your database
```python
connection = pymysql.connect(
      host="localhost",
      port=3306,
      user="root",
      password="nopassword",
      database="sales",
      cursorclass=pymysql.cursors.DictCursor
      )
```
- Run code 
## Improving my project
- :white_check_mark: Make base of program
- :negative_squared_cross_mark: Add login in DB using txt or json file
- :negative_squared_cross_mark: Fix some buges
- :negative_squared_cross_mark: Add endless loop 
