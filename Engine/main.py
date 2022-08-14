import os
import argparse

from api.app import create_app

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-disk", action="store_true",
                        help="USe this flag to use the disk based provider",
                        required=False)
    
    args = parser.parse_args()

    # FLASK_ENV->  expected as one of the keys in env_config (ex: "development")
    app = create_app(os.getenv("FLASK_ENV"))

    # bind on '0.0.0.0' so as to expose the service on the network and 8080 is one of the open ports

    app.run(debug=True, host='localhost', port=5010)

if __name__ == '__main__':
    _main()

