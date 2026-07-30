# Day 1: Fundamentals of Git and Open Source Contribution

## Objective

By the end of this session, you should be able to use Git and GitHub confidently enough to contribute to a shared project. You will fork this repository, work inside your own submission folder, practice commits and branches, handle a merge conflict, and finish by opening a Pull Request — the same habit open-source contributors use every day.

## Background

Git helps you track changes. GitHub helps teams share those changes. In TechNexus Cohort 2, we do not practice in a throwaway repo. You will learn by contributing to **this** organization repository, inside a folder that belongs to you. That is intentional: open-source contribution is not just knowing commands — it is knowing where your work belongs, how to keep it clean, and how to submit it for review.

## Where You Will Work

Everything you create today goes here:

```text
Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/
```

Example:

```text
Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/Bilal_Oyeleke_Soliu/
```

That folder is your workspace root. Build every file and directory inside it.

Please do not touch another student’s folder, and do not edit anything under `tasks/`.

## Screenshot Proof

For every task below, save a screenshot as proof that you completed it. Upload each screenshot into your student folder, commit it, and push it with the rest of your work.

**Naming rule:** use `task<number>.<extension>` — for example `task1.png`, `task2.jpg`, `task3.png`.

Accepted formats: `.png`, `.jpg`, or `.jpeg`.

Make sure your screenshot clearly shows what is being checked. Blurry or cropped screenshots may be sent back for resubmission.

---

## Task Instructions

### 1. Get Ready on GitHub

If you do not have a GitHub account yet, create one here: [https://github.com](https://github.com)

Next, create a Personal Access Token so you can authenticate when you push code:

- Guide: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Treat the token like a password. Never commit it.

When you are done, your token screen should look similar to this:

Personal Access Token example

Now fork the TechNexus Cohort 2 repository:

1. Open [https://github.com/TechNexusClub/TechNexus_Cohort_2](https://github.com/TechNexusClub/TechNexus_Cohort_2)
2. Click **Fork**

Fork the repository

Clone your fork:

```bash
git clone https://github.com/<YOUR_USERNAME>/TechNexus_Cohort_2.git
cd TechNexus_Cohort_2
```

Or with a token:

```bash
git clone https://<YOUR_PERSONAL_TOKEN>@github.com/<YOUR_USERNAME>/TechNexus_Cohort_2.git
cd TechNexus_Cohort_2
```

Tell Git who you are:

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Create your submission folder and move into it:

```bash
mkdir -p Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>
cd Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>
```

Create your first `README.md`:

```bash
echo 'My first readme' > README.md
cat README.md
```

Then commit and push:

```bash
git add .
git commit -m "My first commit"
git push origin main
```

You are ready when your fork shows `README.md` in your Day-1 folder with the text `My first readme`.

**Screenshot proof — save as `task1.png`**

Capture your **fork on GitHub** showing:

- your student folder path under `submissions/Day-1/`
- `README.md` visible inside that folder
- the file content `My first readme` when opened (or the commit `My first commit` in the history)

This proves your fork, clone, first commit, and push all worked.

---

### 2. Own Your Submission Folder

Open the `README.md` inside your student folder and replace the content with your **full name**.

Commit and push again.

Your folder should now look like this:

```text
<Your_First_Middle_Last>/
└── README.md
```
Then when you run the command "cat README.md". You should see you full name. See example below:
```
cat README.md
Bilal Oyeleke Soliu
```

**Screenshot proof — save as `task2.png`**

Capture `**README.md` open on GitHub** in your student folder, showing your **full name** as the file content. The commit message should also be visible if possible.

This proves you edited, committed, and pushed an update to your own folder.

---

### 3. Start Building Inside Your Folder

Right now your folder is almost empty. Let’s give it a simple project shape.

Still inside:

```text
.../submissions/Day-1/<Your_First_Middle_Last>/
```

1. Create these directories: `bash`, `c`, `js`
2. Create these empty files:
  - `c/c_is_fun.c`
  - `js/main.js`
  - `js/index.js`
3. Create `bash/technexus` with exactly:
  ```bash
   #!/bin/bash
   echo "TechNexus"
  ```
4. Create `bash/school` with exactly:
  ```bash
   #!/bin/bash
   echo "Albukhary International University"
  ```
5. Stage everything, commit with the message `Starting to code today, so cool`, and push to your fork.

You should now have:

- `bash/technexus`
- `bash/school`
- `c/c_is_fun.c`
- `js/main.js`
- `js/index.js`

**Screenshot proof — save as `task3.png`**

Capture your **student folder on GitHub** showing the full file tree: `bash/`, `c/`, and `js/` directories with all required files inside. The commit `Starting to code today, so cool` should be visible in the commit history if possible.

This proves you created the project structure and pushed it successfully.

---

### 4. Learn to Work on a Branch

In open source, you rarely edit `main` directly while experimenting. A branch gives you a safe copy of the project so you can try ideas without breaking the shared line of work.

Branches are useful when you want to:

- build a feature without disturbing stable code
- collaborate without stepping on each other
- keep review clean and intentional

Create a branch called `update_script`. On that branch, inside your student folder:

1. Create an empty file named `bash/98`
2. In `bash/technexus`, change `echo "TechNexus"` to `echo "TechNexus School"`
3. In `bash/school`, change `echo "Albukhary International University"` to `echo "The school is open!"`
4. Commit with the message `My personal work`
5. Push the branch to your fork

Create and push a branch

If you can see another branch on your github like the above image apart from the main branch, and you really pushed there. You've did a great job, Your feature work is isolated.

Now imagine a mentor asks for an urgent fix on `main`:

1. Switch back to `main`
2. In `bash/technexus`, change `echo "TechNexus"` to `echo "TechNexus Cohort is so cool!"`
3. Delete the `js` directory
4. Commit with the message `Hot fix` and push

After this section, you should understand why `update_script` and `main` can tell different stories about the same files.

**Screenshot proof — save as `task4.png`**

Capture the **branch dropdown on GitHub** (or the Branches page on your fork) showing both `main` and `update_script`. Switch to `update_script` and make sure `bash/98` is visible in the file tree.

This proves you created a feature branch, pushed it, and applied separate changes on `main`.

---

### 5. Stay in Sync with GitHub

Contributors do not work alone. Someone else — or even you, from the browser — may change the remote before you do.

For this part only, edit `README.md` in your student folder from the **GitHub website** on your fork’s `main` branch. This is the only time today you should commit from the GitHub UI.

Edit a file on GitHub

Then return to your terminal and:

1. Bring the remote `main` changes into your local copy
2. Create a file named `up_to_date` in your student folder
3. Write the exact git command you used into that file
4. Commit with the message `How to be up to date in git` and push

You should end with an updated `README.md` and a new `up_to_date` file.

**Screenshot proof — save as `task5.png`**

Capture your **terminal** showing the git command you used to pull/fetch remote changes (for example `git pull origin main`) with a successful output. If possible, also show `up_to_date` visible in your student folder on GitHub.

This proves you synced local work with remote changes and recorded the command you used.

---

### 6. Resolve Your First Merge Conflict

Sooner or later, two branches will touch the same lines. That is normal. What matters is how you resolve it.

Merge `update_script` into `main`:

```bash
git checkout main
git merge update_script
```

Expect something like this:

```text
CONFLICT (content): Merge conflict in bash/technexus
```

Merge conflict example

Resolve it by keeping the version from `update_script`, finish the merge, and push.

When you are done, `main` should include:

- the work from `update_script` (`bash/98` and the two updated scripts), and
- the earlier `main` changes (including the deleted `js` folder),

with no conflict markers left behind.

**Screenshot proof — save as `task6.png`**

Capture your **terminal** showing either:

- the merge conflict message (`CONFLICT (content): Merge conflict in bash/technexus`), or
- the successful merge commit after you resolved it and ran `git push`

If you took both, combine them into one screenshot or use the resolved state as your final proof.

This proves you encountered and handled a real merge conflict.

---

### 7. Protect the Repository with `.gitignore`

Not every file belongs in Git. Backup files, secrets, and local editor junk should stay on your machine.

Create a `.gitignore` at the root of your student folder and add a rule that ignores files ending with `~` (common Emacs backup files).

Commit and push it.

**Screenshot proof — save as `task7.png`**

Capture `**.gitignore` open on GitHub** in your student folder, showing the rule that ignores `~` files (for example `*~`).

This proves you added ignore rules and pushed them with your submission.

---

### 8. Submit Your Work with a Pull Request

This is the open-source finish line for today.

When your folder is complete on your fork:

1. Open [https://github.com/TechNexusClub/TechNexus_Cohort_2](https://github.com/TechNexusClub/TechNexus_Cohort_2)
2. Go to **Pull requests** → **New pull request**
3. Compare across forks if needed
4. Set:
  - **base:** `TechNexusClub/TechNexus_Cohort_2` → `main`
  - **compare:** your fork → the branch with your finished work (usually `main`)
5. Title it clearly, for example:
  ```text
   Add Day-1 Git fundamentals submission for <Your_First_Middle_Last>
  ```
6. In the description, briefly say what you practiced.
7. Open the PR and wait for review.

Open a pull request

**Screenshot proof — save as `task8.png`**

Capture your **opened Pull Request page** showing:

- the PR title
- base repository `TechNexusClub/TechNexus_Cohort_2`
- your fork as the compare branch
- the list of files changed in your student folder

This proves you completed the open-source contribution flow end to end.

> After you take `task8.png`, add it to your student folder, commit, and push so the screenshot is included in the PR (or in a quick follow-up commit on the same PR branch).

---

## Expected Final Folder Structure

```text
Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/
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

Remember: `js/` should no longer be there after the hot fix.

Your screenshot filenames may use `.jpg` or `.jpeg` instead of `.png`, as long as they follow the `task1`, `task2`, … naming pattern.

---

## Deadline

Submit your Pull Request by **[DAY / TIME]**.

## Resources

- [Github Cheetsheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Git Handbook (GitHub)](https://guides.github.com/introduction/git-handbook/)
- [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Git Branching – Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
- [gitignore documentation](https://git-scm.com/docs/gitignore)
- Workshop Resources and Demo Images: `Software_Engineering/Mastering_Git_and_Open_Source_Contribution/resources/`

---

Take your time, read each step carefully, and ask questions when something is unclear. See you in the PR reviews.