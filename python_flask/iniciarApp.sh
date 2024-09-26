#!/bin/bash

# Ativar o ambiente virtual
source ~/Aws_pipeline/my_env/bin/activate

# Iniciar o Gunicorn
exec gunicorn --workers 3 --bind unix:/home/ubuntu/Aws_pipeline/app.sock app:app