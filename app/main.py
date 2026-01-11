# for local launching, not needed in docker

# import sys
# from pathlib import Path

# if __name__ == "__main__":
#     sys.path.insert(0, str(Path(__file__).parent.parent))

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
