import os
import sys
import time
import requests


def detect_server(ports: list, max_seconds: int = 60):
    port = ports[0]
    seconds = 0
    sleep = 1
    success = False
    print(f'searching for jupyter lab at http://localhost:{port}...')
    while seconds < max_seconds:
        try:
            resp = requests.get(f'http://localhost:{port}')
            if resp.status_code == 200:
                os.system(f'start http://localhost:{port}')
                success = True
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(sleep)
        seconds += sleep
    if not success:
        print('Error! Unable to detect jupyter lab container.')
        print(f'Please open http://localhost:{port} manually.')
        time.sleep(30)

    for port in ports[1:]:
        seconds = 0
        sleep = 1
        success = False
        print(f'searching for project server at http://localhost:{port}...')
        while seconds < max_seconds:
            try:
                resp = requests.get(f'http://localhost:{port}')
                if resp.status_code == 200:
                    os.system(f'start http://localhost:{port}')
                    success = True
                    break
            except requests.exceptions.ConnectionError:
                pass
            time.sleep(sleep)
            seconds += sleep
        if not success:
            print('Error! Unable to detect project server.')
            print(f'Please open http://localhost:{port} manually.')
            time.sleep(30)
