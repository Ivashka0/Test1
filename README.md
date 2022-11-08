# Tutorial for running code
____
Tips which u should **follow**:
- Connect to your database
```
`connection` = pymysql.connect(
      `host`="localhost",
      `port`=3306,
      `user`="root",
      `password`="nopassword",
      `database`="sales",
      `cursorclass`=pymysql.cursors.DictCursor
      )
```
