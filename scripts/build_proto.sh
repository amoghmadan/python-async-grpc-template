#!/bin/bash

set -e

# Absolute or relative path to your proto files (inside your package)
PROTO_DIR="proto/app"
GENERATION_DIR="gen/app/python"
mkdir -p "$GENERATION_DIR"

echo "📦 Generating Python gRPC files from .proto files in $PROTO_DIR..."

# Compile all .proto files in the directory
for proto_file in "$PROTO_DIR"/*.proto; do
    echo "🔄 Compiling $proto_file..."
    python -m grpc_tools.protoc \
        -I"$PROTO_DIR" \
        --python_out="$GENERATION_DIR" \
        --grpc_python_out="$GENERATION_DIR" \
        "$proto_file"
done
