"""Root-level entrypoint for the Local Security Lab.

Allows running `python app.py` or `py app.py` directly from the project root.
"""

import os
import sys

# Ensure lab directory is on sys.path
LAB_DIR = os.path.join(os.path.dirname(__file__), "lab")
if LAB_DIR not in sys.path:
    sys.path.insert(0, LAB_DIR)

from app import HOST, PORT, LabHandler, ThreadedLabServer

if __name__ == "__main__":
    print(f"Local-only lab running at http://{HOST}:{PORT}/ (Ctrl+C to stop)", flush=True)
    server = ThreadedLabServer((HOST, PORT), LabHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nLab server stopped.")
    finally:
        server.server_close()
