# Day 1 Assignment: Fundamentals of Git and GitHub

## Objective

By the end of this assignment, you will practice using fundamental Git commands to create a repository, track changes, manage files, work with branches, handle merge conflicts, and push your progress to GitHub. 

Instead of contributing to a shared repository, you will build and manage **your own personal public GitHub repository** and submit its link for grading.

---

## Deadline

### The Deadline for this Assessment is 31st July, 2026 at 11AM Malysia Time. 

This is the submission form:  [https://forms.gle/zjcouGafkcZGYFPJ7](https://forms.gle/zjcouGafkcZGYFPJ7) 

---

## 🚨 Critical Requirement: Public Repository Visibility

Before you begin, ensure your repository is set to **Public**. If your repository is set to **Private**, instructors and mentors will **not** be able to view or grade your submission.

---

## Expected Final Repository Structure

By the end of this assignment, your personal repository root directory should look like this:

```text
technexus-git-fundamentals/
├── README.md
├── up_to_date
├── .gitignore
├── task1.png
├── task2.png
├── task3.png
├── task4.png
├── task5.png
├── task6.png
├── task7.png
├── task8.png
├── bash/
│   ├── technexus
│   ├── school
│   └── 98
└── c/
    └── c_is_fun.c
```

*(Note: The `js/` folder should be deleted during Task 4).*

---

## Screenshot Proof Rules

For every task below, save a screenshot showing proof that you completed the step. Upload each screenshot file into the root of your local repository, commit it, and push it to GitHub alongside your code.

- **Naming rule:** `task<number>.<extension>` (e.g., `task1.png`, `task2.jpg`, `task3.png`).
- **Accepted formats:** `.png`, `.jpg`, or `.jpeg`.
- **Quality:** Ensure terminal text and GitHub UI elements are clearly visible.

---

## Task Instructions

### Task 1: Create Your Public Repository & Initial Setup

1. Log into your account at [GitHub](https://github.com).
2. Click the `**+`** icon in the top right corner and select **New repository**.
3. Fill in the following details:
  - **Repository name:** `technexus-git-fundamentals`
  - **Description:** `TechNexus Cohort 2 - Day 1 Git & GitHub Fundamentals`
  - **Visibility:** Select **PUBLIC** 🌐 *(Do NOT select Private)*
  - **Initialize repository:** Check the box that says **Add a README file**.
4. Click **Create repository**.
5. Copy your repository HTTPS URL (e.g., `https://github.com/<YOUR_USERNAME>/technexus-git-fundamentals.git`).
6. Open your terminal on your computer and clone your new repository:

```bash
git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/technexus-git-fundamentals.git
cd technexus-git-fundamentals
```

1. Configure your Git developer identity (if not already done globally):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your_email@example.com"
```

1. Update `README.md` locally:

```bash
echo 'My first readme' > README.md
```

1. Stage, commit, and push your changes:

```bash
git add README.md
git commit -m "feat: initial commit with readme"
git push origin main
```

**📸 Screenshot proof — Save as `task1.png`**  
Capture your repository homepage on GitHub showing `README.md` rendered on the screen with the text `My first readme`. Place `task1.png` in your local project root folder.

---

### Task 2: Update Your README with Your Full Name

1. Open `README.md` on your computer using a text editor or terminal.
2. Replace its entire content with your **Full Name**.
3. Verify the changes in terminal:

```bash
cat README.md
```

1. Stage, commit, and push:

```bash
git add README.md
git commit -m "docs: update README with full name"
git push origin main
```

**📸 Screenshot proof — Save as `task2.png`**  
Capture `README.md` open on GitHub showing your **Full Name** as the file content and your commit message in history. Place `task2.png` in your local project root folder.

---

### Task 3: Build the Project Directory Structure

Inside the root of your `technexus-git-fundamentals` repository:

1. Create three directories: `bash`, `c`, and `js`.
2. Create these files:
  - `c/c_is_fun.c`
  - `js/main.js`
  - `js/index.js`
3. Create `bash/technexus` with the following content:
  ```bash
   #!/bin/bash
   echo "TechNexus"
  ```
4. Create `bash/school` with the following content:
  ```bash
   #!/bin/bash
   echo "Albukhary International University"
  ```
5. Stage everything, commit, and push to GitHub:

```bash
git add .
git commit -m "Starting to code today, so cool"
git push origin main
```

**📸 Screenshot proof — Save as `task3.png`**  
Capture your repository file tree on GitHub showing the `bash/`, `c/`, and `js/` folders with all files created inside them. Place `task3.png` in your local project root folder.

---

### Task 4: Practice Branching & Isolated Edits

Follow these exact terminal steps to create a branch, make modifications, and perform a separate fix on `main`:

1. Create and switch to a new branch named `update_script`:

```bash
git checkout -b update_script
```

1. Perform the following edits on the `update_script` branch:
  - Create an empty file named `bash/98`.
  - In `bash/technexus`, change `echo "TechNexus"` to `echo "TechNexus School"`.
  - In `bash/school`, change `echo "Albukhary International University"` to `echo "The school is open!"`.
2. Commit and push the branch to GitHub:

```bash
git add .
git commit -m "My personal work"
git push origin update_script
```

1. Switch back to your `main` branch to apply an urgent hotfix:

```bash
git checkout main
```

1. Perform the following edits on `main`:
  - In `bash/technexus`, change `echo "TechNexus"` to `echo "TechNexus Cohort is so cool!"`.
  - Delete the `js` folder and its contents:
    ```bash
    rm -rf js
    ```
2. Commit and push the hotfix on `main`:

```bash
git add .
git commit -m "Hot fix"
git push origin main
```

**📸 Screenshot proof — Save as `task4.png`**  
Capture the branch dropdown menu on GitHub showing both `main` and `update_script` branches listed. Switch to `update_script` on GitHub and verify `bash/98` is visible. Place `task4.png` in your local project root folder.

---

### Task 5: Sync Changes from GitHub (Remote Pull)

1. Open your repository on the **GitHub website** in your browser.
2. Click on `README.md` and click the **pencil icon (Edit)** in the top right.
3. Add a line at the bottom of the file (e.g., `Edited directly on GitHub web`).
4. Click **Commit changes...** at the top right of the web editor.
5. Return to your terminal on your computer and pull the remote changes down to your machine:

```bash
git pull origin main
```

1. Create a file named `up_to_date` in the root of your local repository.
2. Inside `up_to_date`, write the exact terminal command you used to pull changes (`git pull origin main`).
3. Commit and push:

```bash
git add .
git commit -m "How to be up to date in git"
git push origin main
```

**📸 Screenshot proof — Save as `task5.png`**  
Capture your terminal window showing the successful output of running `git pull origin main`. Place `task5.png` in your local project root folder.

---

### Task 6: Resolve Your First Merge Conflict

Now you will merge your `update_script` feature branch into `main`. Because both branches modified `bash/technexus`, Git will flag a merge conflict.

1. Ensure you are on the `main` branch:

```bash
git checkout main
```

1. Trigger the merge:

```bash
git merge update_script
```

*(Git will output `CONFLICT (content): Merge conflict in bash/technexus`)*

1. Open `bash/technexus` in your code editor. You will see conflict markers like this:

```bash
<<<<<<< HEAD
echo "TechNexus Cohort is so cool!"
=======
echo "TechNexus School"
>>>>>>> update_script
```

1. Resolve the conflict by keeping the incoming version from `update_script` (`echo "TechNexus School"`). Delete all `<<<<<<<`, `=======`, and `>>>>>>>` markers.
2. Save the file.
3. Complete the merge commit and push:

```bash
git add bash/technexus
git commit -m "fix: resolve merge conflict between main and update_script"
git push origin main
```

**📸 Screenshot proof — Save as `task6.png`**  
Capture your terminal showing either the conflict warning message or the final successful merge commit output after running `git push`. Place `task6.png` in your local project root folder.

---

### Task 7: Configure File Exclusion with `.gitignore`

1. Create a file named `.gitignore` in the root of your repository:

```bash
echo "*~" > .gitignore
```

1. Stage, commit, and push `.gitignore`:

```bash
git add .gitignore
git commit -m "style: add gitignore for emacs backup files"
git push origin main
```

**📸 Screenshot proof — Save as `task7.png`**  
Capture `.gitignore` open on GitHub showing the `*~` rule. Place `task7.png` in your local project root folder.

---

### Task 8: Final Verification & Repository Submission

1. Ensure all task screenshots (`task1.png` through `task8.png`) are staged, committed, and pushed to your remote repository on GitHub:

```bash
git add task*.png task*.jpg task*.jpeg
git commit -m "docs: upload all task screenshot proofs"
git push origin main
```

1. Verify your repository visibility:
  - Open an **Incognito / Private browser window**.
  - Paste your GitHub repository link: `https://github.com/<YOUR_USERNAME>/technexus-git-fundamentals`
  - If the page loads without asking you to log in, your repository is **Public** and ready for grading.

**📸 Screenshot proof — Save as `task8.png`**  
Capture your GitHub repository home page in your browser showing all project files and all `task1.png` through `task8.png` screenshot files listed in the root directory.

1. **Final Submission Step:** Submit the direct web URL of your public GitHub repository (`https://github.com/<YOUR_USERNAME>/technexus-git-fundamentals`) on this  submission form:  [https://forms.gle/zjcouGafkcZGYFPJ7](https://forms.gle/zjcouGafkcZGYFPJ7)

---

## Submission Checklist

Before submitting your link, confirm the following:

- Repository visibility is set to **Public**.
- `README.md` contains your full name.
- The `js/` directory was deleted as part of the hotfix.
- `up_to_date` contains the `git pull origin main` command.
- `.gitignore` contains the rule `*~`.
- Screenshots `task1.png` through `task8.png` are visible in the repository root on GitHub.
- Your repository link has been pasted into the official assignment submission form.

---

## Resources

- [GitHub Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)
- [Git Handbook (GitHub Guides)](https://guides.github.com/introduction/git-handbook/)
- [Git Branching – Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [Ignoring Files Documentation](https://git-scm.com/docs/gitignore)

