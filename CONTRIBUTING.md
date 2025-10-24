## Contributing

Thank you for considering contributions to this project. The guidance below is intended to keep the contribution process simple and efficient.

1. Reporting issues

- Open an issue describing the bug or enhancement. Include steps to reproduce, expected behavior, and any relevant logs or small data samples.

2. Pull requests

- Fork the repository and create a topic branch for your change.
- Keep changes focused and document the intent in the PR description.
- If the change affects behavior or model outputs, include before/after notes and any relevant metrics.

NOTE: Code style and tests

- Follow existing project conventions. Keep code readable and well-commented.
- Add tests where applicable (unit or integration). If no test framework exists, include a small script or instructions to reproduce the change locally.

Working locally

1. Create and activate a virtual environment (optional but recommended):

   python -m venv .venv
   # Windows PowerShell
   .\.venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

3. Run the application or training scripts to validate changes. See `app.py` and the `training/` folder.

License

- By contributing, you agree that your contributions will be licensed under the project's MIT License.

Contact

If you need additional guidance before opening an issue or PR, add a comment to an existing issue or open a new one to start the discussion.
