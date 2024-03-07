class ExamplePipeline:
    INPUT_FOLDERS = ['s3inputs']
    OUTPUT_FOLDERS = ['process1Output']

    PIPELINE = [
        {
            "type": "shell",
            "input_paths": ["s3://mybucket/input_data.txt"], #this variable is not used, it is just here for example purposes
            "output_folder": "s3inputs",
            "script": "example_pull_from_s3.sh",
            "args": [] # eg ["--param1", "value1", "--param2", "value2"] 
        },
        {
            "type": "python",
            "input_paths": ["s3inputs/sample_data.txt"],
            "output_folder": "process1_Output",
            "script": "example_process_data.py",
            "args": []
        },
        {
            "type": "shell",
            "input_paths": ["process1_Output/"],
            "output_folder": "s3://mybucket/output_data.txt",
            "script": "example_push_to_s3.sh",
            "args": []

        }
    ]
