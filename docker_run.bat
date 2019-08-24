docker run ^
--rm -it ^
-p 5000:5000 ^
-p 5001:5001 ^
-v %cd%:/app ^
paradoxlabs/knot ^
/bin/bash -c "nohup jupyter lab --ip=0.0.0.0 --port=5001 --no-browser --allow-root > /app/logs/jupyter.log 2>&1"
