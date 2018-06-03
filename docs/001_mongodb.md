# Install mongoDB


## Install the packages
Import the public key used by the package mgmt system (to check consistency/ authenticity)
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
```
Create a list file for MDB. Below version for  
```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/testing multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
```
Reload the local package database.
```
sudo apt-get update
```
Install mongoDB.
```
sudo apt-get install -y mongodb-org
```
Pin the installed version of MongoDB, so there will be no unintended upgrades. Issue the following commands
```
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
```

## Run MongoDB
Start `mongod`.
```
sudo service mongod start
```
Check that MDB started successfully.
```
less /var/log/mongodb/mongod.log
cat /var/log/mongodb/mongod.log | grep waiting
```
Expected output:
```
2018-06-02T16:06:43.249+0300 I NETWORK  [initandlisten] waiting for connections on port 27017
```
Stop `mongod`.
```
sudo service mongod stop
```
Restart `mongod`.
```
sudo service mongod restart
```
Check `mongod` status.
```
vl@mfla:~/Downloads$ sudo service mongod status
● mongod.service - MongoDB Database Server
   Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset:
   Active: active (running) since Суб 2018-06-02 16:06:41 +03; 5min ago
   ...

Чэр 02 16:06:41 mfla systemd[1]: Started MongoDB Database Server.
Чэр 02 16:06:41 mfla mongod[9063]: 2018-06-02T16:06:41.815+0300 I CONTROL  [main
lines 1-10/10 (END)
```
NEXT UP:
* [MongoDB 02 - Mistake](002_mongod_trouble.md)
