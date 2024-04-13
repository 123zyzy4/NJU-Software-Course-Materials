import os
import pandas as pd

import subprocess

import os
import subprocess

def process_c_files(directory,output_path):
    
    report_counter = 1

    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".c"):
                file_path = os.path.join(subdir, file)

                with open(file_path, 'r', encoding='utf-8') as source_file:
                    content = source_file.read()
                    tmp_file_path = os.path.join("E:/workspace/SoftwareSecHomework/Experiment1/tmp",str(report_counter)+".c")
                    with open(tmp_file_path, 'w', encoding='utf-8') as tmp_file:
                        tmp_file.write(content)

                output_file = os.path.join(output_path,str(report_counter)+".csv")
                flawfinder_command = f"flawfinder --csv > {output_file} {tmp_file_path}"
                subprocess.run(flawfinder_command, shell=True)
                report_counter += 1

   


def delete_files(output_path):
    for file in os.listdir(output_path):
            if file.endswith(".csv"):
                file_path = os.path.join(output_path, file)
                with open(file_path, 'r') as report:
                    report_content = report.read()
                    if "E:/workspace/SoftwareSecHomework/Experiment1/tmp" not in report_content:
                        report.close()
                        os.remove(file_path)



target_directory = "E:/workspace/SoftwareSecHomework/vlc-master"
output_path = "E:/workspace/SoftwareSecHomework/Experiment1/output"

process_c_files(target_directory, output_path)
delete_files(output_path)


