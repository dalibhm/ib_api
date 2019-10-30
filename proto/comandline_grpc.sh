# install grpc tools
python -m pip install --upgrade pip
python -m pip install grpcio
# if there is a  problem on mac:
# python -m pip install grpcio --ignore-installed

python -m pip install grpcio-tools

# compile proro file
python -m grpc_tools.protoc -I=./proto --python_out=./proto --grpc_python_out=./proto listing.proto
