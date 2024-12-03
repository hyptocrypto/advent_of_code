#!/bin/bash

# Directory containing the day files
directory="days"

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "Directory '$directory' does not exist. Creating it now."
  mkdir "$directory"
fi

# Find the highest day number
highest_day=$(ls "$directory" | grep -Eo 'day[0-9]+' | grep -Eo '[0-9]+' | sort -n | tail -n 1)

# Set the next day number
if [ -z "$highest_day" ]; then
  next_day=1
else
  next_day=$((highest_day + 1))
fi

# Create the new day file
new_file="$directory/day${next_day}.py"
if [ -e "$new_file" ]; then
  echo "File '$new_file' already exists!"
else
  touch "$new_file"
  echo "# Day ${next_day}" > "$new_file"
  echo "File '$new_file' has been created."
fi

