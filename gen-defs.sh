#!/usr/bin/env bash
cd `dirname "$0"`

protoc --python_out=python/ data.proto

# after installing protoc-gen-go from
# http://code.google.com/p/goprotobuf/
protoc --go_out=go/test data.proto

