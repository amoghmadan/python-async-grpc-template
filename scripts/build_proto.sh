#!/bin/bash

PROTO_PATH="proto"
GENERATION_PATH="src"

echo "🔄 Compiling 'proto/app/**/*.proto' to '$GENERATION_PATH'..."

python -m grpc_tools.protoc \
  -I"$PROTO_PATH" \
  --python_out="$GENERATION_PATH" \
  --grpc_python_out="$GENERATION_PATH" \
  proto/app/**/*.proto

echo "✅ Done! Generated stubs in '$GENERATION_PATH'"

echo "🔄 Adding __init__.py files to subpackages..."

OUT_DIR="src/app/protobuf"

# Add __init__.py to every folder in OUT_DIR
find $OUT_DIR -type d | while read -r dir; do
  init_file="$dir/__init__.py"
  if [ ! -f "$init_file" ]; then
    echo "# Auto-generated to make this a Python package" > "$init_file"
    echo "Created $init_file"
  fi
done

echo "✅ Done!"
