# MongoDB - Troubles

## Data directory not found
I checked the status of `mongod`, and it displayed the error you mentioned.
I STORAGE  [initandlisten] exception in initAndListen: NonExistentPath: Data directory /data/db not found., terminating
I CONTROL  [initandlisten] now exiting
I CONTROL  [initandlisten] shutting down with code:100

Okay, i created the folder, chowned it and restarted the service.
$ sudo mkdir -p /data/db
$ sudo chown `whoami` /data/db
$ sudo service mongod restart

Checking the status again with `mongod`.
New error:
E STORAGE  [initandlisten] Failed to set up listener: SocketException: Address already in use
I CONTROL  [initandlisten] now exiting
I CONTROL  [initandlisten] shutting down with code:48

So what are the steps you can recommend?
sudo killall -15 mongod
