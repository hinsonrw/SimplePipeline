import os
import sys
import importlib.util
import subprocess
import logging
from datetime import datetime

class PipelineRunner:
    def __init__(self, pipeline_module):
        self.pipeline_module = pipeline_module
        self.log_file = None
        self.project_folder = None

    def create_folders(self):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        project_folder = f"InstanceData/{timestamp}"
        os.makedirs(project_folder, exist_ok=True)

        input_folders = getattr(self.pipeline_module, 'INPUT_FOLDERS', [])
        output_folders = getattr(self.pipeline_module, 'OUTPUT_FOLDERS', [])

        for folder in input_folders + output_folders:
            folder_path = os.path.join(project_folder, folder)
            os.makedirs(folder_path, exist_ok=True)

        self.log_file = os.path.join(project_folder, 'pipeline.log')
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

        return project_folder

    def run_pipeline(self):
        self.project_folder = self.create_folders()

        for stage in self.pipeline_module.PIPELINE:
            script_path = os.path.join(os.path.dirname(__file__), 'StageScripts', stage['script'])
            if not os.path.exists(script_path):
                MissingScriptError = f"Script file '{stage['script']}' not found. Exiting pipeline due to missing script."
                logging.error(MissingScriptError)
                print(MissingScriptError)
                sys.exit(1)
            self.run_stage(stage)

    def run_stage(self, stage):
        script_type = stage['type']
        input_paths = ' '.join([os.path.join(self.project_folder, path) for path in stage['input_paths']])
        output_folder = os.path.join(self.project_folder, stage['output_folder'])
        script_path = os.path.join(os.getcwd(), 'StageScripts', stage['script'])

        logging.info(f"Running stage: {stage['script']}")

        env = os.environ.copy()
        env['INPUT_PATHS'] = input_paths
        env['OUTPUT_FOLDER'] = output_folder  # Corrected here

        try:
            if script_type == 'python':
                subprocess.run(['python3', script_path, *stage.get('args', [])], env=env, check=True)
            elif script_type == 'shell':
                subprocess.run(['bash', script_path], env=env, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Stage '{stage['script']}' failed with exit code {e.returncode}.")
            logging.error("Exiting pipeline due to stage failure.")
            sys.exit(1)

if __name__ == "__main__":
    
    ## Update the pipeline_module_path to the path of the pipeline module. 
    ## Currently we're running the example

    pipeline_module_path = os.path.join(os.path.dirname(__file__), 'Pipelines', 'example')

    spec = importlib.util.spec_from_file_location("example", f"{pipeline_module_path}.py")
    pipeline_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pipeline_module)
    
    # Instantiate ExamplePipeline class
    example_pipeline = pipeline_module.ExamplePipeline()
    
    runner = PipelineRunner(example_pipeline)  # Pass the instantiated object
    runner.run_pipeline()
