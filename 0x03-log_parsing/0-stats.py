#!/usr/bin/python3
"""log parsing"""
import sys

file_size = 0
l_200 = 0
l_301 = 0
l_400 = 0
l_401 = 0
l_403 = 0
l_404 = 0
l_405 = 0
l_500 = 0

for i, line in enumerate(sys.stdin, 1):
    log_parts = line.split()

    if len(log_parts) != 9:
        continue
    try:
        status_c = int(log_parts[7])
        file_size += int(line.split()[8])
    except ValueError:
        continue

    if status_c == 200:
        l_200 += 1
    if status_c == 301:
        l_301 += 1
    if status_c == 400:
        l_400 += 1
    if status_c == 401:
        l_401 += 1
    if status_c == 403:
        l_403 += 1
    if status_c == 404:
        l_404 += 1
    if status_c == 405:
        l_405 += 1
    if status_c == 500:
        l_500 += 1

    if i % 10 == 0:
        print(f"File size: {file_size}")
        if l_200:
            print(f"200: {l_200}")
        if l_301:
            print(f"301: {l_301}")
        if l_400:
            print(f"400: {l_400}")
        if l_401:
            print(f"401: {l_401}")
        if l_403:
            print(f"403: {l_403}")
        if l_404:
            print(f"404: {l_404}")
        if l_405:
            print(f"405: {l_405}")
        if l_500:
            print(f"500: {l_500}")

print(f"File size: {file_size}")
if l_200:
    print(f"200: {l_200}")
if l_301:
    print(f"301: {l_301}")
if l_400:
    print(f"400: {l_400}")
if l_401:
    print(f"401: {l_401}")
if l_403:
    print(f"403: {l_403}")
if l_404:
    print(f"404: {l_404}")
if l_405:
    print(f"405: {l_405}")
if l_500:
    print(f"500: {l_500}")
