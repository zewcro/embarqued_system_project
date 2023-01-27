import subprocess


def main(): 
    def start_server(): 
        try:
            print("== Starting web-server ==")
            subprocess.call(["python", "server.py"])
        except NameError:
            print("process requested not found")
        except:
            print("error while starting the server")
    
    start_server()


main()