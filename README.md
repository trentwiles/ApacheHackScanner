# Apache Hack Scanner

Scan your logs for Wordpress/CMS/Router hack attempts.


### How to use

Install everything with pip:

```
python3 -m pip install apachelogs
```

Run the script with your server software as an argument (Default Apache2 and Nginx logs are supported). Examples:

Apache2:

```
python3 main.py apache2
```

Nginx:

```
python3 main.py nginx
```
