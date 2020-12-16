#!/bin/bash

function diary() {
    cd
    cd Desktop/PythonApps/auto_diary/
    python3 diary.py
    cd
    cd Desktop/Diary/
    vi `ls -tr | tail -1`
    
}


