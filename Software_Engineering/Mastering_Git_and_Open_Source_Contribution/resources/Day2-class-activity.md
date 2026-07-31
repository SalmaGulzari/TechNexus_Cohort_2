# Day 2 Live Class Activity: My First Open Source Contribution

## Objective

Today, you will take the work you completed for your **Day 1 Assignment** inside your personal repository (`technexus-git-fundamentals`) and submit it to the central **TechNexus Organization Repository** via a Pull Request.

You do **not** need to re-write any code! You will practice the full open-source contribution workflow (Forking, Branching, Directory Setup, Committing, Pushing, and opening a PR) using your existing Day 1 files.

---

## Workspace Directory Requirement

Your files MUST be placed in this exact directory path inside the central repository:

```text
Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/
```

### Folder Name Example:
If your name is **Bilal Oyeleke Soliu**, your folder path must be:
`Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/Bilal_Oyeleke_Soliu/`

---

## Step-by-Step Instructions

### Step 1: Fork the Central Organization Repository

1. Open your browser and navigate to the official TechNexus repository:  
   👉 [https://github.com/TechNexusClub/TechNexus_Cohort_2](https://github.com/TechNexusClub/TechNexus_Cohort_2)
2. In the top right corner of the page, click the **Fork** button.
3. Select your personal account as the destination and click **Create fork**.

---

### Step 2: Clone Your Fork to Your Local Machine

1. Open your terminal on your computer.
2. Clone your newly created fork (replace `<YOUR_USERNAME>` with your actual GitHub username):

```bash
git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/TechNexus_Cohort_2.git
cd TechNexus_Cohort_2
```

3. Verify that your Git developer identity is set:

```bash
git config user.name "Your Full Name"
git config user.email "your_email@example.com"
```

---

### Step 3: Create a Dedicated Feature Branch

In open-source software development, you never submit Pull Requests directly from your `main` branch. Always create a feature branch first.

Create and switch to a new branch named `feat/add-day1-open-source-contribution`:

```bash
git checkout -b feat/add-day1-open-source-contribution
```

---

### Step 4: Create Your Submission Folder

Inside your terminal, create your personalized submission directory under `submissions/Day-1/` using your full name (`<Your_First_Middle_Last>`):

```bash
mkdir -p Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>
```

---

### Step 5: Copy Your Day 1 Files Into Your Submission Folder

Now, copy all files from your Day 1 personal repository (`technexus-git-fundamentals`) into your newly created submission folder.

#### Option A: Using Command Line (Linux/macOS/Git Bash)
Assuming your `technexus-git-fundamentals` folder is located in the same parent directory as `TechNexus_Cohort_2`:

```bash
cp -r ../technexus-git-fundamentals/* Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/
cp -r ../technexus-git-fundamentals/.gitignore Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/
```

#### Option B: Using File Explorer / Finder
1. Open your computer's File Explorer or Finder.
2. Copy all contents inside `technexus-git-fundamentals` (including `README.md`, `up_to_date`, `.gitignore`, screenshot images, `bash/`, and `c/`).
3. Paste them directly into:  
   `TechNexus_Cohort_2/Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/`

---

### Step 6: Verify Your Folder Structure

Verify that your student submission directory contains all expected files:

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

---

### Step 7: Stage, Commit, and Push Your Branch

1. Stage all added files:

```bash
git add .
```

2. Verify that only files inside your personalized folder are staged:

```bash
git status
```

3. Commit your work with the required message:

```bash
git commit -m "feat: add day 1 add as the first open source contribution"
```

4. Push your branch to your personal fork on GitHub:

```bash
git push -u origin feat/add-day1-open-source-contribution
```

---

### Step 8: Open Your First Open Source Pull Request (PR)

1. Open your web browser and go to the central repository:  
   👉 [https://github.com/TechNexusClub/TechNexus_Cohort_2](https://github.com/TechNexusClub/TechNexus_Cohort_2)
2. You will see a banner at the top saying **"Compare & pull request"**. Click it.  
   *(If you don't see the banner, go to the **Pull requests** tab and click **New pull request**)*.
3. Verify the target branches:
   - **base repository:** `TechNexusClub/TechNexus_Cohort_2`  ➡️  **base:** `main`
   - **head repository:** `<YOUR_USERNAME>/TechNexus_Cohort_2`  ➡️  **compare:** `feat/add-day1-open-source-contribution`
4. Set the **PR Title** to:
   ```text
   feat: add day 1 add as the first open source contribution for <Your_First_Middle_Last>
   ```
5. In the description box, write a brief sentence confirming that your Day 1 task files are complete inside your student folder.
6. Click **Create Pull Request**.

---

## Verification Checklist

Before celebrating, double-check these items on your open Pull Request:

- [ ] Your PR is directed to `TechNexusClub/TechNexus_Cohort_2` on branch `main`.
- [ ] Your files are inside `Software_Engineering/Mastering_Git_and_Open_Source_Contribution/submissions/Day-1/<Your_First_Middle_Last>/`.
- [ ] You did not delete or edit any files outside of your personal folder.
- [ ] All 8 task screenshots and project files are visible under the **Files changed** tab.

**Congratulations! You have successfully executed a real open-source contribution workflow!** 