#!/usr/bin/env bash

echo "Who are you?"
read name
printf "hello, %s\n" "$name"

echo "what are you doing" "$name" "?\n"
read action 
printf "so you are ${action}ing now\n"
