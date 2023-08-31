# gunicorn_config.py

workers = 2      # Number of worker processes
bind = "0.0.0.0:80"  # Binding address and port
# timeout = 1       # Maximum request/response timeout