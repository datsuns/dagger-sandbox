#!/usr/bin/bash

cd $1
wget -nc --no-check-certificate https://github.com/VOICEVOX/voicevox_core/raw/refs/heads/main/model/sample.vvm/decode.onnx
wget -nc --no-check-certificate https://github.com/VOICEVOX/voicevox_core/raw/refs/heads/main/model/sample.vvm/vocoder.onnx


