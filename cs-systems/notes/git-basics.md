# Git Basics

## Overview
Git is a version control system used to track changes in code and files over time. It helps developers save progress, compare versions, and collaborate without constantly creating duplicate files.

---

## Version Control
Version control is the system of recording changes to files so older versions can still be viewed or restored later.

Why it matters:
- keeps a history of changes
- makes collaboration easier
- helps recover from mistakes
- lets multiple people work on the same project

Git is one of the most common version control systems.

---

## Repository
A **repository** (or **repo**) is the folder that Git tracks.

A repo contains:
- your project files
- hidden Git data
- the full history of commits

A repository can exist:
- locally on your computer
- remotely on GitHub

---

## Repository Structure
A Git repository usually includes:
- the working directory
- the staging area
- the commit history

### Working Directory
This is where you actively edit files.

### Staging Area
This is where you prepare changes before committing them.

### Commit History
This is the timeline of saved snapshots of the project.

A common workflow is:
- edit files
- save files
- add changes
- commit changes
- push changes

---

## Common Git Terms

| Term | Meaning |
|------|---------|
| `clone` | copy a remote repo to your local machine |
| `add` | move changes into the staging area |
| `commit` | save a snapshot of changes locally |
| `push` | send local commits to GitHub |
| `pull` | bring remote changes into your local repo |
| `fetch` | check for remote changes without merging them |

---

## Local vs Remote Repository
A **local repository** is on your own computer.

A **remote repository** is stored online, such as on GitHub.

This allows you to:
- work on multiple devices
- share code with others
- back up your progress in the cloud

---

## Pulling Changes from the Cloud
When changes are made to the remote repository, your local repository can become outdated.

To update your local copy, you use **pull**.

### What pull does
A pull updates your local repository with changes from the remote repository.

This helps:
- keep your code current
- sync changes across devices
- avoid working from an outdated version

### Basic idea
Pull = fetch + merge

That means Git:
- checks for new remote changes
- brings them down to your machine
- tries to merge them into your local repo

---

## Why Pulling Matters
Pulling is important when:
- you edited files on another machine
- a teammate pushed changes
- you changed something directly on GitHub

Without pulling first, your local repo may not match the remote repo.

---

## Merge Conflicts
A merge conflict happens when Git cannot automatically decide how to combine two changes.

This usually happens when:
- two people edit the same part of a file
- local and remote commits are based on the same earlier version
- the changes do not match cleanly

---

## What a Merge Conflict Means
A merge conflict does **not** mean Git lost your work.

It means Git found conflicting changes and needs a human to choose what the final version should be.

Git pauses the merge so the user can:
- review both changes
- choose one change
- combine them manually
- complete the merge

---

## Resolving a Merge Conflict
A basic merge conflict workflow is:
- pull or merge changes
- Git reports a conflict
- open the file with the conflict
- decide which version to keep
- save the corrected file
- commit the merge result
- push the resolved version

After that, the project returns to one main history stream.

---

## Why Merge Conflicts Happen
Merge conflicts are common when:
- people do not pull before starting work
- multiple users edit the same lines
- local and cloud histories diverge

Good habits that reduce conflicts:
- pull before starting work
- commit often
- communicate with teammates
- keep changes small and organized

---

## Basic Workflow Example
A common Git workflow looks like this:
1. Edit a file
2. Save the file
3. Add the change
4. Commit the change
5. Push to GitHub

When receiving updates:
1. Fetch or pull from origin
2. Review incoming changes
3. Continue working with the updated repository

---

## Key Takeaways
- Git is a version control system
- A repository stores your project and its history
- Git tracks changes through working directory, staging area, and commits
- Pulling updates your local repo with remote changes
- Merge conflicts happen when Git cannot combine changes automatically
- Good Git habits help keep projects organized and safe
