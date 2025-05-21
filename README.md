# remoter

MRE for remote execution of workflows.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/valerius21/remoter.git
   cd remoter
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run with a custom config file:

```bash
python -m app.main --config path/to/your_config.yml
```

If you omit --config, it defaults to config.yml in the project root.

## Configuration

The configuration file is a YAML file specifying remotes and workflows. See `config.example.yml` for a template:

```yaml
remotes:
  - host: 127.0.0.1
    user: youruser
    password: ${YOUR_PASSWORD_ENV_VAR}

workflows:
  - name: echo
    steps:
      - name: echo test
        command: |
          echo "test"
```

You can use environment variables in the config by referencing them as `${VARNAME}`. Set them in your shell or in a `.env` file.

## Example Workflow

Suppose you want to run a workflow that creates and reads a file on a remote host:

```yaml
workflows:
  - name: read file
    steps:
      - name: read file
        command: |
          export FILE_NAME="test-$(date +%Y-%m-%d-%H-%M-%S).txt"
          echo "test" > /tmp/$FILE_NAME
          cat /tmp/$FILE_NAME
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Structure

```
remoter/
    app/
        __init__.py
        lib.py
        main.py
    tests/
        __init__.py
        test_lib.py
        test_main.py
    requirements.txt
    README.md
    CITATION.cff
    config.example.yaml
```

- `app/`: Main application code
- `tests/`: Unit tests
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation 
- `config.example.yaml`: Example configuration file

## Citation

If you use this software, please cite it as below.

```bibtex
@software{remoter,
  author       = {Valerius Mattfeld},
  title        = {remoter},
  version      = {0.1.0},
  date         = {2025-05-21},
  url          = {https://github.com/valerius21/remoter},
  note         = {If you use this software, please cite it as below.},
  orcid        = {https://orcid.org/0000-0003-0263-0332}
}
```
