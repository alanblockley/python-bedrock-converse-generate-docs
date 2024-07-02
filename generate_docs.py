import os
import sys
import json
import boto3
from botocore.config import Config

region_config = Config(
    region_name="ap-southeast-2"
)

bedrock_runtime = boto3.client("bedrock-runtime", config=region_config)
model_id = "anthropic.claude-3-haiku-20240307-v1:0"
temp = 0.5
top_k = 200

def init(output_dir):
    # Output the current meta data including boto3 version, aws account id and region.
    print(boto3.client('sts').get_caller_identity().get('Account'))
    print(boto3.client('sts').meta.region_name)
    print(boto3.__version__)

    # if docs/ directory does not exist, create it.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def extract_substring(text, trigger_str, end_str):
    last_trigger_index = text.rfind(trigger_str)
    if last_trigger_index == -1:
        return ""
    next_end_index = text.find(end_str, last_trigger_index)
    if next_end_index == -1:
        return ""
    substring = text[last_trigger_index + len(trigger_str):next_end_index]
    return substring

def ingest(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_output(markup_output, output_file):
    with open(output_file, 'w') as f:
        f.write(markup_output)
        f.close()

def main(source_file, output):

    source = ingest(source_file)
    system_prompt = [
        {
            "text" : """
You are a technical writer tasked with documenting the provided source code. Your goal is to create documentation that is easily understood by individuals of varying technical expertise and business backgrounds. The documentation should be written in plain English, with source references included where applicable.

Requirements:

The documentation must have a title and a subtitle.
Use code formatting where relevant.
Format the documentation in markup language suitable for a .md (Markdown) file.

Output your thought process within <scratchpad> XML tags. Output your final documentation within <markup> XML tags.
    """
        }
    ]

    message = {
        "role" : "user",
        "content" : [
            {
                "text" : source
            }
        ]
    }

    messages = [message]
    inference_config = {"temperature": temp}
    additional_model_fields = {"top_k": top_k}

    response = bedrock_runtime.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompt,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    output = response['output']['message']['content'][0]['text']
    markup_output = extract_substring(output, "<markup>","</markup>")

    # Output markup_output into a file
    function_name = os.path.basename(source_file).split('.')[0]
    output_file = os.path.join(output_dir, f"{function_name}.md")

    write_output(markup_output, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_docs.py <source_file> <output_dir>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    output_dir = sys.argv[2]   
    
    init(output_dir)
    main(source_file, output_dir)