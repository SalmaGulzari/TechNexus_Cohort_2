# TechNexus Cohort 2 — Contribution Guide

Welcome to **TechNexus Cohort 2**! This repository is used for publishing workshop tasks, submitting student assessments, and reviewing progress across all training tracks.

Follow this guide so submissions land in the correct folders and can be reviewed smoothly.

---

## Repository Structure

```text
TechNexus_Cohort_2/
├── AI_ML/
├── Blockchain_Engineering/
├── CyberSecurity_Networking/
└── Software_Engineering/
```

Every track uses the same layout. Mentors stay at the track level. Each workshop gets its own folder with `tasks`, `submissions`, and `resources`:

```text
<Track>/
├── mentors/                      # Mentor guidelines and checklists
└── <Workshop-Name>/              # e.g. Example-Workshop
    ├── tasks/                    # Task briefs for this workshop
    ├── submissions/              # Student assessment submissions
    └── resources/                # Extra materials for this workshop
```

### Example layout (per track)

```text
<Track>/
├── mentors/
│   └── mentor_checklist.md
└── Example-Workshop/
    ├── tasks/
    │   └── Day-1-task.md
    ├── submissions/
    │   └── Day-1/
    │       └── <Student_Name>/
    │           ├── <write-up>.md
    │           └── <code files>
    └── resources/
```

### Example student submissions

| Track | Example student folder |
|-------|------------------------|
| Software Engineering | `Software_Engineering/Example-Workshop/submissions/Day-1/Bilal_Oyeleke_Soliu/` |
| Blockchain Engineering | `Blockchain_Engineering/Example-Workshop/submissions/Day-1/Bonson_Adem_Alo/` |
| AI / ML | `AI_ML/Example-Workshop/submissions/Day-1/Khin_Pwint_Yati_Maung/` |
| CyberSecurity & Networking | `CyberSecurity_Networking/Example-Workshop/submissions/Day-1/Karim_Ismail_Abdellah_Mohammed/` |

### Naming conventions

| Item | Pattern | Example |
|------|---------|---------|
| Workshop folder | `<Workshop-Name>` | `Example-Workshop` |
| Task file | `<Workshop-Name>/tasks/Day-<n>-task.md` | `Example-Workshop/tasks/Day-1-task.md` |
| Submission day folder | `<Workshop-Name>/submissions/Day-<n>/` | `Example-Workshop/submissions/Day-1/` |
| Resources folder | `<Workshop-Name>/resources/` | `Example-Workshop/resources/` |
| Student folder | `<First_Middle_Last>` (use underscores) | `Bilal_Oyeleke_Soliu` |

---

## For Students: Submitting Your Tasks

### 1. Fork the Repository

Create a personal copy of this repository on your GitHub account.

- Visit: [https://github.com/TechNexusClub/TechNexus_Cohort_2](https://github.com/TechNexusClub/TechNexus_Cohort_2)
- Click **Fork** at the top right of the page.

### 2. Clone Your Fork

```bash
git clone https://github.com/<your_username>/TechNexus_Cohort_2.git
cd TechNexus_Cohort_2
```

### 3. Sync Your Fork Regularly

Keep your fork up to date with the main repository:

```bash
git remote add upstream https://github.com/TechNexusClub/TechNexus_Cohort_2.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 4. Read the Task Brief

Open the task for your track, workshop, and day:

```text
Software_Engineering/Example-Workshop/tasks/Day-1-task.md
Blockchain_Engineering/Example-Workshop/tasks/Day-1-task.md
AI_ML/Example-Workshop/tasks/Day-1-task.md
CyberSecurity_Networking/Example-Workshop/tasks/Day-1-task.md
```

Supporting materials (if any) live in that workshop’s `resources/` folder. Complete everything the task asks for before submitting.

### 5. Navigate to the Correct Submission Folder

Submissions are organized by **track → workshop → submissions → day**:

```bash
cd <Track>/<Workshop-Name>/submissions/Day-<day_number>
```

Examples:

```bash
cd Software_Engineering/Example-Workshop/submissions/Day-1
cd Blockchain_Engineering/Example-Workshop/submissions/Day-1
cd AI_ML/Example-Workshop/submissions/Day-1
cd CyberSecurity_Networking/Example-Workshop/submissions/Day-1
```

### 6. Create Your Personal Folder

Create a folder using your registered name with underscores:

```bash
mkdir <First_Middle_Last>
```

Example:

```bash
mkdir Bilal_Oyeleke_Soliu
```

Your full submission path should look like:

```text
Software_Engineering/Example-Workshop/submissions/Day-1/Bilal_Oyeleke_Soliu/
```

### 7. Add Your Task Files

Place all files for that day’s assessment inside your personal folder. Keep them organized and clearly named (write-ups, code, tests, diagrams, etc.).

Example:

```text
Bilal_Oyeleke_Soliu/
├── unit-test.md
├── average.py
└── test_average.py
```

### 8. Commit and Push Your Changes

```bash
git add .
git commit -m "Add Example-Workshop Day-1 submission for Bilal_Oyeleke_Soliu"
git push origin main
```

Use a clear commit message that includes the workshop, day, and your name.

### 9. Create a Pull Request

1. Open the original repository: [https://github.com/TechNexusClub/TechNexus_Cohort_2](https://github.com/TechNexusClub/TechNexus_Cohort_2)
2. Go to the **Pull requests** tab → **New pull request**
3. Choose **compare across forks** if needed
4. Set your fork/branch as the source and `main` on `TechNexusClub/TechNexus_Cohort_2` as the base
5. Use a descriptive title and briefly explain what you submitted

Example PR title:

```text
Add Example-Workshop Day-1 submission for Bilal_Oyeleke_Soliu
```

### 10. Wait for Review

Mentors may leave comments or request changes. Update your files, push again to the same branch, and the PR will update automatically.

---

## Additional Notes for Students

- Submit only inside **your own** student folder. Do not edit other students’ submissions.
- Do not modify files under `tasks/` or `resources/` unless a mentor asks you to.
- Make sure your work is complete and readable before opening a PR.
- Sync with `upstream` often so your PR stays easy to merge.
- If you get stuck, ask your facilitator or mentor for help.

---

## For Mentors: Managing Tasks

See also the mentor checklist in your track, e.g. [`Software_Engineering/mentors/mentor_checklist.md`](Software_Engineering/mentors/mentor_checklist.md).

### 1. Creating a Workshop Folder

For each new workshop, create this structure inside your track:

```text
<Track>/<Workshop-Name>/
├── tasks/
├── submissions/
└── resources/
```

Example:

```bash
mkdir -p Software_Engineering/Workshop-1/{tasks,submissions,resources}
```

### 2. Adding a Task

1. Add a markdown file named `Day-<day_number>-task.md` inside `<Workshop-Name>/tasks/`.
2. Include clear objectives, instructions, deadline, and links.
3. Place any supporting files (datasets, slides, starter code) in `<Workshop-Name>/resources/`.
4. Commit and push.

Example:

```bash
git add Software_Engineering/Example-Workshop/tasks/Day-1-task.md
git commit -m "Add Software Engineering Example-Workshop Day-1 task"
git push origin main
```

### 3. Preparing the Submission Folder

Before students submit, create the matching day folder:

```text
<Track>/<Workshop-Name>/submissions/Day-<day_number>/
```

Example:

```text
Software_Engineering/Example-Workshop/submissions/Day-1/
```

Students will then create their personal folders inside that day folder:

```text
Software_Engineering/Example-Workshop/submissions/Day-1/<Student_Name>/
```

### 4. Reviewing Student Submissions

1. Open the **Pull requests** tab on GitHub.
2. Confirm the path matches: `<Track>/<Workshop-Name>/submissions/Day-<n>/<Student_Name>/`
3. Review completeness, correctness, and clarity against the task brief.
4. Leave constructive comments if changes are needed.
5. Approve and merge when the submission meets expectations.

---

Thank you for contributing to TechNexus Cohort 2. Happy building!
