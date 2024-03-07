#!/bin/bash

# Get input and output folder paths from environment variables
INPUT_PATHS="$INPUT_PATHS"
OUTPUT_FOLDER="$OUTPUT_FOLDER"

# Ensure input paths and output folder are provided
if [ -z "$INPUT_PATHS" ] || [ -z "$OUTPUT_FOLDER" ]; then
    echo "Error: INPUT_PATHS or OUTPUT_FOLDER is not set."
    exit 1
fi


# Extract the bucket name from the output folder path
bucket_name=$(echo "$OUTPUT_FOLDER" | cut -d'/' -f1)

# Sync the input folder to the S3 bucket
aws s3 sync "$INPUT_PATHS" "s3://$bucket_name/"