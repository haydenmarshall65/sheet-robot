#!/bin/bash

if [ -d "venv/" ]; then
    source venv/bin/activate
else
    source .venv/bin/activate
fi