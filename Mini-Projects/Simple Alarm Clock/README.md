# Simple Alarm Clock

A basic Python alarm clock that waits until the user-set time matches the current system time.

## Project Overview
This project uses Python's `time` module to compare the current time with a user-provided alarm time in `HH:MM` format.

## Files
- `SetAlarm.py` - main alarm clock logic

## How to Run
```bash
python SetAlarm.py
```

## How It Works
1. Enter an alarm time in `HH:MM` format.
2. The program keeps checking the current time.
3. When the time matches, it prints `Wake Up! Alarm Time!` and stops.

## Example
```text
Set alarm time (HH:MM): 08:30
Alarm is running...
Wake Up! Alarm Time!
```

## Requirements
- Python 3
