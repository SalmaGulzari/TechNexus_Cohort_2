# Source Code Management

## What is Source Code Management?

Source Code Management (SCM) is a system that helps me keep track of changes made to my code over time. Instead of creating multiple copies of a project, SCM records every change, making it easy to go back to previous versions whenever needed.

One of its biggest advantages is collaboration. Multiple developers can work on the same project at the same time without constantly overwriting each other's work.

### Common Terms

Before working with any SCM tool, these are some important terms I should know:

- **Repository (Repo):** The main folder that contains my entire project and its version history.
- **Branch:** A separate copy of the project where I can work on a new feature or fix a bug without affecting the main code.
- **Main Branch:** The primary version of the project. In Git, this is usually called `main`.
- **Commit:** A snapshot of the changes I've made. Every commit should include a short and meaningful message describing what changed.
- **Commit History:** A timeline of all commits made to the project. This makes it easy to understand what changed and who made the changes.
- **Merge:** The process of combining changes from one branch into another.
- **Merge Conflict:** A situation where Git cannot automatically combine changes because multiple people modified the same part of a file. These conflicts must be resolved manually.

---

# Source Code Management Systems

Over the years, different source code management systems have been developed. Some are now outdated, while others are still widely used.

## SourceSafe

SourceSafe was Microsoft's early version control system.

It allowed only one developer to edit a file at a time by using a **check-out/check-in** process. While this prevented conflicts, it wasn't practical for larger teams where multiple developers needed to work simultaneously.

Today, SourceSafe is obsolete.

---

## CVS (Concurrent Versions System)

CVS was one of the earliest open-source version control systems.

Unlike SourceSafe, multiple developers could modify the same files simultaneously. However, CVS had very limited merge capabilities, so developers frequently had to resolve conflicts manually.

Although it played an important role historically, CVS is rarely used today.

---

## SVN (Subversion)

SVN was created to improve upon CVS.

It introduced proper branching and better merging capabilities. However, branches were created by copying the entire project, making them relatively expensive compared to modern systems.

SVN is still used in some organizations, especially those maintaining older enterprise applications.

---

## Git

Git is currently the most popular source code management system.

Unlike older systems, Git stores changes efficiently without copying the whole project whenever a branch is created. This makes branching and merging much faster.

Some of the reasons I prefer Git include:

- Fast branching and merging
- Better conflict resolution
- Ability to work offline
- Distributed version control
- Excellent collaboration support

Because branches are lightweight, it's considered good practice to create a new branch for every feature or bug fix instead of working directly on the `main` branch.

---

## Mercurial

Mercurial is another distributed version control system.

Its overall concepts are very similar to Git, although the command syntax is different. While Git dominates the software industry today, Mercurial is still used in some projects.

---

# Understanding Git

Git is designed as a distributed version control system.

This means I can continue committing changes even without an internet connection because commits are stored locally on my computer.

When I'm ready to share my work with others, I simply push my commits to a remote repository.

---

## Local Repository vs Remote Repository

A Git project usually has two versions:

- **Local Repository:** The copy stored on my computer.
- **Remote Repository:** The copy hosted online, usually on platforms like GitHub.

I work locally first, then synchronize my work with the remote repository.

---

## Push and Pull

Two Git commands I use frequently are:

### Push

Uploads my local commits to the remote repository.

```bash
git push origin main
```

### Pull

Downloads the latest changes from the remote repository and merges them into my local branch.

```bash
git pull origin main
```

Pulling regularly helps me avoid unnecessary merge conflicts.

---

## The Staging Area

Git doesn't automatically include every modified file in a commit.

Instead, it uses a **staging area** (also called the **index**) where I choose exactly which files should be included in my next commit.

For example:

```bash
git add file1 file2
```

or to stage everything:

```bash
git add .
```

---

# Basic Git Workflow

A typical Git workflow looks like this:

### Clone an existing repository

```bash
git clone <repository-url>
```

### Stage changes

```bash
git add .
```

### Commit changes

```bash
git commit -m "Describe what changed"
```

### Push changes

```bash
git push origin main
```

---

# Working with Branches

Instead of working directly on the main branch, I usually create a separate branch for each feature.

### Create a branch

```bash
git branch my_feature
```

or

```bash
git checkout -b my_feature
```

The second command creates the branch and switches to it immediately.

---

### Switch branches

```bash
git checkout my_feature
```

---

### Push the branch

```bash
git push origin my_feature
```

---

### Keep the branch updated

```bash
git pull origin my_feature
```

---

### Merge back into the main branch

```bash
git checkout main
git merge my_feature
```

Once the feature is complete, I merge it back into the main branch.

---

# Creating a Git Repository

If I already have a project that isn't using Git, I can initialize it with:

```bash
git init
```

Then I connect it to a remote repository:

```bash
git remote add origin <repository-url>
```

---

# Checking Repository Status

To see which files have been modified or staged, I use:

```bash
git status
```

This command helps me understand the current state of my repository before committing.

---

# Git vs GitHub

Although people often use the names interchangeably, Git and GitHub are different.

## Git

Git is the version control software installed on my computer. It manages my project's history and tracks changes.

## GitHub

GitHub is an online platform that hosts Git repositories.

Besides storing code, GitHub also provides features like:

- Repository hosting
- Code reviews
- Team collaboration
- Issue tracking
- Pull Requests
- CI/CD integration

---

# Forks

A **Fork** creates my own copy of someone else's repository on GitHub.

This allows me to experiment, make improvements, or contribute to open-source projects without affecting the original repository.

---

# Pull Requests

After making changes to a branch or fork, I can open a **Pull Request (PR)**.

A pull request asks the project maintainers to review my changes before merging them into the main project.

This review process helps maintain code quality and encourages collaboration.

---

# Other Git Hosting Platforms

Although GitHub is the most popular platform, there are several alternatives, including:

- GitLab
- Bitbucket

Each platform provides Git hosting with collaboration features, though GitHub remains the industry standard for open-source development.

---

# Helpful Resources

If I want to improve my Git skills, these are excellent resources:

- Git Official Book: https://git-scm.com/book
- GitHub Documentation: https://docs.github.com/en/get-started
- Learn Git Branching: https://learngitbranching.js.org/
- Git From the Inside Out: https://codewords.recurse.com/issues/two/git-from-the-inside-out
- Semantic Versioning: https://semver.org/

---

# Summary

Git has become the industry-standard version control system because it makes tracking changes, collaborating with other developers, and managing project history much easier.

By understanding repositories, branches, commits, merges, push, pull, and pull requests, I can confidently manage software projects and contribute to team-based or open-source development.