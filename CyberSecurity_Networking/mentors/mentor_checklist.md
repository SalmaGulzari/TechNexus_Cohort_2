# TechNexus Cohort 2 — Mentor Checklist (CyberSecurity & Networking)

This checklist ensures consistency in reviewing student submissions and managing workshops effectively.

## Workshop Setup

For each workshop, create this structure inside the track:

```text
CyberSecurity_Networking/<Workshop-Name>/
├── tasks/
├── submissions/
└── resources/
```

Example: `CyberSecurity_Networking/Example-Workshop/`

## Task Management

- Create a `Day-<day_number>-task.md` file in `<Workshop-Name>/tasks/`.
- Clearly define the objectives, requirements, and success criteria for the task.
- Include links to relevant resources or documentation.
- Place supporting materials (datasets, slides, starter code) in `<Workshop-Name>/resources/`.
- Push the task to the repository as early as possible.

## Prepare the Submission Folder

- Navigate to `<Workshop-Name>/submissions/`.
- If a task is assigned for a specific day, **manually create the corresponding day subfolder** `Day-<day_number>/`.
- Example: `CyberSecurity_Networking/Example-Workshop/submissions/Day-1/`

## Reviewing Submissions

- Check the **Pull Requests (PRs)** tab for new student submissions.
- Ensure students follow the correct directory structure:
  `<Workshop-Name>/submissions/Day-<n>/<Student_Name>/`
- Review the code quality, completeness, and adherence to task requirements.
- Provide constructive feedback via PR comments.
- Approve and merge PRs if the submission meets expectations.
- If changes are needed, request modifications and guide the student.

## Mentorship & Support

- Encourage students to ask questions and clarify any doubts.
- Regularly engage with students on Discord.
- Provide additional explanations or hints where necessary.
- Share best practices and useful resources.
