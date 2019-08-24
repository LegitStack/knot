docker run \
--rm -it \
-p 5000:5000 \
-p 5001:5001 \
-v $(pwd):/app \
paradoxlabs/knot \
nohup jupyter lab --ip=0.0.0.0 --port=5001 --no-browser --allow-root > /dev/null 2>&1
