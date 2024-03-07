SimplePipeline
Simple tool for data pipelining.

Overview
SimplePipeline is a lightweight tool designed to facilitate data pipelining by chaining together simple scripts and passing inputs from one script to the outputs of another. It's particularly useful for processing data in sequential stages where each stage depends on the output of the previous one.

Usage
Define Your Pipeline: Define your data processing pipeline by creating a Python script that specifies the sequence of stages, input paths, and output paths. Each stage can be a Python or shell script.


# Define your pipeline
```
PIPELINE = [
    {
        'script': 'stage1.py',
        'type': 'python',
        'input_paths': ['input_data.txt'],
        'output_folder': 'stage1_output'
    },
    {
        'script': 'stage2.sh',
        'type': 'shell',
        'input_paths': ['stage1_output'],
        'output_folder': 'stage2_output'
    },
    # Add more stages as needed
]
```
Run the Pipeline: Run the pipeline using the provided pipeliner.py script. This script reads the pipeline definition, executes each stage sequentially, and passes the necessary input and output paths to each stage.


python3 pipeliner.py
View Results: After running the pipeline, you can find the results in the specified output folders.

Example
Here's a simple example demonstrating how to use SimplePipeline:

Create a pipeline definition file (example.py):


from SimplePipeline import Pipeline
```
class ExamplePipeline(Pipeline):
    PIPELINE = [
        {
            'script': 'stage1.py',
            'type': 'python',
            'input_paths': ['input_data.txt'],
            'output_folder': 'stage1_output'
        },
        {
            'script': 'stage2.sh',
            'type': 'shell',
            'input_paths': ['stage1_output'],
            'output_folder': 'stage2_output'
        },
        # Add more stages as needed
    ]
```
Create individual stage scripts (stage1.py, stage2.sh, etc.) to perform specific data processing tasks.

Run the pipeline:

python3 pipeliner.py
View the results in the specified output folders.

Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for details.

