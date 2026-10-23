
from pathlib import Path
from datetime import datetime


# Create workspace folder automatically
WORKSPACE = Path("workspace")
WORKSPACE.mkdir(exist_ok=True)


def generate_output(task):
    """Generate the initial output based on the user's task."""

    task_lower = task.lower().strip()

    # Python study plan
    if "study plan" in task_lower and "python" in task_lower:
        return "Study Python for 3 hours every day."

    # Leave letter or leave request
    if any(word in task_lower for word in [
        "leave letter",
        "leave email",
        "leave request"
    ]):
        return (
            "Subject: Leave Request\n\n"
            "Dear Sir/Madam,\n\n"
            "I am writing to request leave due to personal reasons. "
            "Kindly grant me leave for the required period.\n\n"
            "Thank you for your understanding.\n\n"
            "Yours sincerely,\n"
            "[Your Name]"
        )

    # Generic task
    return (
        f"Task: {task}\n\n"
        "1. Define the goal clearly.\n"
        "2. Break the goal into smaller steps.\n"
        "3. Complete the steps in order.\n"
        "4. Review the result and make improvements."
    )


def improve_output(task, output, feedback):
    """Improve the output using predefined feedback rules."""

    feedback_lower = feedback.lower().strip()
    task_lower = task.lower().strip()

    # Study plan: one hour per day for a beginner
    if (
        "python" in task_lower
        and "study plan" in task_lower
        and any(phrase in feedback_lower for phrase in [
            "1 hour",
            "one hour",
            "60 minutes",
            "60 mins"
        ])
    ):
        return (
            "Beginner-Friendly Python Study Plan\n\n"
            "Study Python for 1 hour daily:\n"
            "1. 20 minutes - Learn Python concepts.\n"
            "2. 30 minutes - Practise coding.\n"
            "3. 10 minutes - Revise what you learned."
        )

    # Professional or formal email
    if (
        "professional email" in feedback_lower
        or "formal email" in feedback_lower
    ):
        return (
            "Subject: Leave Request\n\n"
            "Dear Sir/Madam,\n\n"
            "I am writing to formally request leave due to personal "
            "reasons. I kindly request you to approve my leave "
            "for the required period.\n\n"
            "Thank you for your time and consideration.\n\n"
            "Yours sincerely,\n"
            "[Your Name]"
        )

    # Make the output shorter
    if any(word in feedback_lower for word in [
        "shorter",
        "brief",
        "concise"
    ]):
        lines = output.splitlines()
        return "\n".join(lines[:6])

    # Simplify the language
    if any(word in feedback_lower for word in [
        "simple english",
        "easy english",
        "simplify",
        "beginner-friendly"
    ]):
        return (
            "Simple Version\n\n"
            + output
            + "\n\nTip: Learn one concept at a time and practise daily."
        )

    # Add more details
    if any(word in feedback_lower for word in [
        "more detail",
        "detailed",
        "explain more"
    ]):
        return (
            output
            + "\n\nAdditional Details:\n"
            "Include examples, practise regularly, and review your progress."
        )

    # Add an example
    if "example" in feedback_lower:
        return (
            output
            + "\n\nExample:\n"
            "Practise a small program related to the topic every day."
        )

    # Default: preserve the original output and record feedback
    return (
        output
        + "\n\nFeedback received: "
        + feedback
        + "\nNote: This demo supports predefined feedback rules only."
    )


def save_output(output):
    """Save the approved output in a text file."""

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = WORKSPACE / f"final_output_{timestamp}.txt"

    file_path.write_text(output + "\n", encoding="utf-8")

    return file_path


def main():
    print("=" * 55)
    print("       FEEDBACK-IN-THE-LOOP AGENT")
    print("=" * 55)
    print("This agent improves drafts using human feedback.")
    print("Type 'exit' at any time to stop.\n")

    task = input("Enter your task: ").strip()

    if not task:
        print("Please enter a valid task.")
        return

    if task.lower() == "exit":
        print("Agent stopped.")
        return

    # Step 1: Generate the initial output
    output = generate_output(task)
    revision = 0

    # Step 2: Ask for human feedback and approval
    while True:
        print("\n" + "-" * 55)
        print(f"CURRENT OUTPUT (Revision {revision})")
        print("-" * 55)
        print(output)

        answer = input(
            "\nAre you satisfied with this output? (yes/no): "
        ).strip().lower()

        if answer == "exit":
            print("Agent stopped without saving.")
            return

        # Step 3: Save only after human approval
        if answer in ["yes", "y"]:
            file_path = save_output(output)

            print("\nHuman approval received!")
            print("Final output saved successfully.")
            print(f"File location: {file_path.resolve()}")
            break

        # Step 4: Collect feedback and improve
        elif answer in ["no", "n"]:
            feedback = input(
                "What would you like to improve? "
            ).strip()

            if feedback.lower() == "exit":
                print("Agent stopped without saving.")
                return

            if not feedback:
                print("Please enter your feedback.")
                continue

            output = improve_output(task, output, feedback)
            revision += 1

            print(f"\nFeedback applied. Revision number: {revision}")

        else:
            print("Please enter 'yes', 'no', or 'exit'.")


if __name__ == "__main__":
    main()
