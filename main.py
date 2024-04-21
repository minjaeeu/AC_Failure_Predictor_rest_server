from configurations.server_config import host, port
import subprocess

# invoking uvicorn to run our server app at server_config.host and server_config.port
command = f"uvicorn server:app --host {host} --port {port} --reload"

# initiating process
process = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)

# capturing process error
error = process.communicate()

# print errors if any
if error:
    print("Error:", error.decode("utf-8"))
