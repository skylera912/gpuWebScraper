@echo off
:START
python scraper.py
TIMEOUT 10
GOTO START