# install grpc tools
venv/bin/python -m pip install --upgrade pip
venv/bin/python -m pip install grpcio
# if there is a  problem on mac:
# python -m pip install grpcio --ignore-installed

venv/bin/python -m pip install grpcio-tools

# compile proro file
venv/bin/python -m grpc_tools.protoc -I=./proto --python_out=./proto --grpc_python_out=./proto contracts.proto
