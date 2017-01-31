# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "5r(hfb22vj)ss&+6+)gox^@2mi%%k6hek8l2wupe567^*_-x2a"
NEVERCACHE_KEY = ")1a&*1=lca_&e=(w5ww5d@)!&#j5r5qs#0h334)dr^ic3f$$w%"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # "NAME": "opsclickwebsite",
        # Not used with sqlite3.
        "USER": "opsclickwebuser",
        # Not used with sqlite3.
        "PASSWORD": "opsclickwebsite_ABCD",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "opsclickwebsite.cgaj5yboqlza.us-east-1.rds.amazonaws.com",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    }
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }
