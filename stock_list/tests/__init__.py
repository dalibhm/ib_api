import os
import sys

container_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
))
sys.path.insert(0, container_folder)