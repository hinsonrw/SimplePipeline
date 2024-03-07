#!/bin/bash

# Define the S3 bucket and key
bucket_name="nasanex"
s3_key="NEX-DCP30/nex-dcp30-s3-files.json"

# Retrieve the output directory from the environment variable
output_dir="$OUTPUT_FOLDER"
if [ -z "$output_dir" ]; then
    echo "Error: OUTPUT_FOLDER environment variable is not set."
    exit 1
fi

# Ensure that the output directory exists
mkdir -p "$output_dir"

# Define the output file path
output_file="$output_dir/sample_data.txt"

echo "Downloading file from S3"
echo "output_file: $output_file"

aws s3api get-object --bucket "$bucket_name" --key "$s3_key" "$output_file" --no-sign-request
