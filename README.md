# Initial setup 

## Pre-requisites

In order to build and run locally, you will need the following utilities:

* node v14
* bash
* make
* pip3
* yarn
* docker
* docker-compose

# Running

On the first run, you'll need to install the dependencies for the web app:

```shell
pushd ./app && yarn install && popd
```

When running locally, you need a correctly figured .env file.

Start by copying the .env.local.example file and make any adjustments you need.

Of particular importance is the SOFI_HOSTNAME and SOFI_PORT, as well as the
 TLS_CERT_PATH and TLS_KEY_PATH.
 
Regarding the TLS_CERT and TLS_KEY, it is important that the certificate be a
 ‘real’ certificate signed by a trusted CA. You can use Let’s Encrypt for this purpose.

The SOFI_HOSTNAME must match your certificate.

To run locally using `docker-compose`, execute:

```shell
make run
```

This will launch all containers with locally mounted files, enabling automatic code reload, 
as well as hot-module-reload (HMR) in the browser.

By default, services will be available on `http://sofi.localhost`.
This can be changed by modifying the generated `.env` file.
The relevant env variables are `SOFI_SCHEME`, `SOFI_HOSTNAME`, and `SOFI_PORT`.

Make sure to edit your `/etc/hosts` file (`c:\windows\system32\drivers\etc\hosts` on Windows) and include the line:

```
127.0.0.1	dev.sofi-platform.dk
```

Setting `SOFI_HOSTNAME` to `localhost` or `127.0.0.1` is not currently supported.

When running in the dev environment, a default user account is created,
 which you can use for signing into the application.

Username: `admin@fvst.dk`
Password: `Delegate21!`

## Local dev running
Create virtual env, install dependencies
```shell
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
```
Have a mongodb instance running on localhost:27017

```shell
$ sh start_local.sh
```

On windows, in venv with dependencies installed
```shell
set FLASK_APP=wsgi.py
set FLASK_DEBUG=1
set APP_CONFIG_FILE=config.py
set FLASK_RUN_HOST=127.0.0.1
set FLASK_RUN_PORT=8080
flask run
```

Default user 
username: test
password: test
from seed_data project

# Generating simulated data
When running locally, the bifrost db gets pre-seeded with the contents of the `.jsonl` files inside `initdb.d`.

These `.jsonl` files can be regenerated based on the latest specification running:

```shell
rm bifrost/bifrost_db/initdb.d/generated.jsonl
./generate_dummy_data.sh
```

The seeding only occurs when the database is first created, so to force the change to take effect, run:

```shell
make clean && make run
```