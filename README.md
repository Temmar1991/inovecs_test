Short description of the services:
  1. seeder - this service connects to mysql database seeder and insert one row per second in the table ticks.
     Table ticks consists of two cilumns id, created_at.
     Implemented check connection method to database before inserting entry.
     
  2. backup_service - service which makes backup of database seeder every 5 seconds and archived in zip file backup_seeder.zip to the current
     directory.
     Also implemented web socket mechanizm for succeessful backup and failed backup. Successful backup event contains name of archive, size
     and date of creation. Failed backup event only emit event without messages.
     For reslization of web socker in server used flask extension flask_socketio.
  3. client_service -  web socket client service, which receives messages from backup_service when backup successful or not.
  4. mysql - simple mysql database, which is runnning from official image.
  
  To run solution in docker-compose simply run docker-compose up
  
  First it load all base images, then creates images for every service through Dockerfiles which are located in seeder_files, backup_server_files,]
  seeder_files and than run our stack. Logs of execution of app will be exposed to console.
     
  
