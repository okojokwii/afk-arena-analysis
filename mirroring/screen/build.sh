#!/bin/sh
cd "$(dirname "$0")" && swiftc -O main.swift -o afk-screen
