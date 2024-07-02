
# Source Code Documentation Generator

## Overview

This Python script generates documentation for a given source code file using the Anthropic Bedrock Runtime API. The generated documentation is formatted in Markdown and stored in the specified output directory.

### Requirements

- The documentation must have a title and a subtitle.
- Code formatting should be used where relevant.
- The documentation should be formatted in Markup language suitable for a .md (Markdown) file.

### Usage

To use the script, run the following command:

```
python generate_docs.py <source_file> <output_dir>
```

Replace `<source_file>` with the path to the source code file you want to document, and `<output_dir>` with the directory where you want the generated documentation to be stored.

### How it Works

The script uses the following key components:

1. **Boto3**: The AWS SDK for Python, used to interact with the Bedrock Runtime API.
2. **Bedrock Runtime API**: The Anthropic API used to generate the documentation.
3. **Markdown Formatting**: The generated documentation is formatted in Markdown, a lightweight markup language.

The script performs the following steps:

1. Imports the necessary modules and sets up the Bedrock Runtime API client.
2. Defines the Anthropic model ID and parameters (temperature, top_k) to be used for the documentation generation.
3. Implements several helper functions:
   - `init(output_dir)`: Checks if the output directory exists, and creates it if it doesn't.
   - `extract_substring(text, trigger_str, end_str)`: Extracts a substring from the given text, based on the provided trigger and end strings.
   - `ingest(filename)`: Reads the contents of the specified file.
   - `write_output(markup_output, output_file)`: Writes the generated documentation to the specified output file.
4. Implements the `main(source_file, output)` function, which:
   - Reads the contents of the source file.
   - Constructs the system prompt and message for the Bedrock Runtime API.
   - Calls the Bedrock Runtime API to generate the documentation.
   - Extracts the generated markup from the API response.
   - Writes the markup to the specified output file.
5. Implements the entry point of the script, which:
   - Checks if the correct number of command-line arguments are provided.
   - Calls the `init()` and `main()` functions with the provided source file and output directory.

The generated documentation will be in Markdown format and will be stored in the specified output directory.
