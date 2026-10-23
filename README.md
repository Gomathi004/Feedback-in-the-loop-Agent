# Feedback-in-the-Loop Agent

## About the Project

The Feedback-in-the-Loop Agent is a simple Python command-line project that demonstrates how user feedback can be used to revise an initial output.

The program creates a draft based on a task, shows it to the user, and asks for feedback. It then applies predefined Python rules to revise the output. When the user is satisfied, the final result can be saved as a text file.

This learning demo does not use an AI model or API.

## Features

- Accepts a task from the user.
- Generates a draft using predefined templates.
- Collects feedback from the user.
- Revises the draft using simple keyword-based rules.
- Repeats the review process until the user is satisfied.
- Saves the final output as a text file.
- Does not overwrite an existing output file.

## Technologies Used

- Python
- Python Standard Library
- Command-line interface

## How It Works

1. Enter a task.
2. Review the initial output.
3. Enter `no` if you want to improve it.
4. Describe your feedback.
5. Review the revised output.
6. Enter `yes` when satisfied.
7. Save the final output in the `workspace` folder.

## Project Structure

```text
feedback-in-the-loop-agent/
├── main.py
├── README.md
├── .gitignore
└── workspace/
    └── .gitkeep
```

## How to Run

Install Python 3.10 or later, open a terminal in the project folder, and run:

```bash
python main.py
```

No extra packages, API key, database, or web interface are required.

## Example Feedback

Task: `Create a study plan`

Feedback: `Make it beginner-friendly and fit one hour`

The program applies supported keyword-based rules and displays a revised draft.

## Limitations

This project uses predefined templates and keyword-based rules. It does not understand arbitrary feedback like a real AI model. Its purpose is to demonstrate the feedback-and-revision workflow.

## Future Improvements

- Add more task templates.
- Improve feedback handling.
- Compare initial and revised versions.
- Integrate an AI model in a future version.

## Author

Gomathi V

GitHub: https://github.com/Gomathi004
