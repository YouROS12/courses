# Getting Started with Python Course

Welcome! This guide will help you set up your learning environment and start your Python programming journey.

## Table of Contents

- [Choose Your Learning Method](#choose-your-learning-method)
- [Method 1: Google Colab (Recommended for Beginners)](#method-1-google-colab-recommended-for-beginners)
- [Method 2: Local Installation](#method-2-local-installation)
- [Method 3: Other Cloud Platforms](#method-3-other-cloud-platforms)
- [Verify Your Setup](#verify-your-setup)
- [Course Navigation](#course-navigation)
- [Getting Help](#getting-help)

## Choose Your Learning Method

There are three ways to take this course:

| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| **Google Colab** | Beginners, quick start | No installation, works anywhere, free | Requires internet, sessions timeout |
| **Local Installation** | Offline work, customization | Full control, works offline, faster | Requires setup, uses disk space |
| **Other Platforms** | Specific preferences | Various options | Setup varies by platform |

## Method 1: Google Colab (Recommended for Beginners)

**No installation required! Start coding in 2 minutes.**

### Step 1: Get a Google Account

If you don't have one, create a free Google account at [google.com](https://accounts.google.com/signup)

### Step 2: Open Any Practice Notebook

1. Navigate to any chapter folder (e.g., `chapter_01_introduction/`)
2. Click on the `practice.ipynb` file
3. Click the **"Open in Colab"** badge at the top of the notebook
4. The notebook opens in Google Colab - ready to use!

### Step 3: Start Coding

- **Run a cell**: Click the play button (▶) or press `Shift + Enter`
- **Add a cell**: Hover between cells and click `+ Code`
- **Save your work**: File → Save a copy in Drive

### Google Colab Tips

- Your work is automatically saved to Google Drive
- Sessions disconnect after 90 minutes of inactivity (just reconnect)
- All course exercises work perfectly in Colab
- You can download notebooks: File → Download → .ipynb

### Quick Colab Tutorial

```python
# Type this in a cell and press Shift+Enter
print("Hello, Python!")

# You should see the output below the cell
```

**That's it! You're ready to start Chapter 1.**

---

## Method 2: Local Installation

**For offline work and full customization.**

### Prerequisites

- A computer with Windows, macOS, or Linux
- At least 1 GB of free disk space
- Administrator/sudo access for installation

### Step 1: Install Python

#### Windows

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```

#### macOS

**Option A: Official Installer**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. Verify:
   ```bash
   python3 --version
   ```

**Option B: Using Homebrew** (if installed)
```bash
brew install python
python3 --version
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

### Step 2: Install Jupyter Notebook

Open your terminal/command prompt and run:

```bash
# Install Jupyter
pip install jupyter notebook

# Or if using Python 3 explicitly
pip3 install jupyter notebook
```

### Step 3: Download Course Materials

**Option A: Download ZIP** (No Git required)
1. Click the "Code" button on the repository page
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location
4. Open terminal and navigate to the folder:
   ```bash
   cd path/to/python_course
   ```

**Option B: Clone with Git**
```bash
git clone <repository-url>
cd python_course
```

### Step 4: Install Course Dependencies

```bash
# Navigate to the course directory
cd python_course

# Install required packages
pip install -r requirements.txt

# Or with Python 3 explicitly
pip3 install -r requirements.txt
```

### Step 5: Launch Jupyter Notebook

```bash
# Start Jupyter from the course directory
jupyter notebook
```

A browser window will open showing the course files. Click any `.ipynb` file to open it!

### Local Installation Tips

- **Close Jupyter**: Press `Ctrl+C` in the terminal twice
- **Restart Jupyter**: Run `jupyter notebook` again
- **Update packages**: Run `pip install --upgrade jupyter notebook`
- **Check installed packages**: Run `pip list`

---

## Method 3: Other Cloud Platforms

### Jupyter Notebook Online Platforms

All course materials work on these platforms:

#### JupyterLab (MyBinder)
- Visit [mybinder.org](https://mybinder.org/)
- Paste the repository URL
- Click "Launch"
- Free, no account required

#### Kaggle Notebooks
- Create free account at [kaggle.com](https://www.kaggle.com/)
- Upload notebooks
- Similar to Google Colab

#### VS Code with Jupyter Extension
- Install [VS Code](https://code.visualstudio.com/)
- Install Python extension
- Install Jupyter extension
- Open `.ipynb` files directly

---

## Verify Your Setup

### Test Your Environment

Run this code in a new notebook cell:

```python
# Test 1: Basic Python
print("✓ Python is working!")

# Test 2: Import required libraries
import json
import csv
print("✓ Standard libraries loaded!")

# Test 3: Check Python version
import sys
print(f"✓ Python version: {sys.version}")

# Test 4: Simple calculation
result = 2 + 2
assert result == 4
print("✓ Math works!")

print("\n🎉 Your setup is ready! Start with Chapter 1.")
```

If you see all checkmarks, you're ready to go!

### Troubleshooting Setup Issues

**Problem**: `jupyter: command not found`
- **Solution**: Run `pip install --user jupyter` or check PATH settings

**Problem**: `ModuleNotFoundError` when running notebooks
- **Solution**: Install missing package: `pip install <package-name>`

**Problem**: Jupyter opens but notebooks won't run
- **Solution**: Ensure Python kernel is selected (Kernel → Change kernel → Python 3)

**Problem**: Google Colab won't open notebooks
- **Solution**: Allow pop-ups for colab.google.com in your browser

See [FAQ.md](FAQ.md) for more troubleshooting help.

---

## Course Navigation

### Presentations First, Then Practice

For each chapter:

1. **📊 Start with the presentation** (`presentation.html`)
   - Open in any web browser
   - Read through all slides
   - Take notes on key concepts

2. **💻 Then open the practice notebook** (`practice.ipynb`)
   - Work through exercises one by one
   - Experiment with the code
   - Complete all practice problems

3. **✅ Take the quiz** after every 2 chapters
   - Test your understanding
   - Review incorrect answers
   - Revisit concepts as needed

### Recommended Study Order

```
Chapter 1 → Chapter 2 → Quiz 1
Chapter 3 → Chapter 4 → Quiz 2
Chapter 5 → Chapter 6 → Quiz 3
Chapter 7 → Practice → Quiz 4
Chapter 8 → Chapter 9 → Quiz 5
Chapter 10 → Quiz 5 → Quiz 6
Capstone Project
```

### How to Use Practice Notebooks

Each practice notebook contains:

- **📖 Concept Review**: Brief explanation of key ideas
- **💡 Examples**: Demonstrated code with explanations
- **✏️ Practice Problems**: Exercises for you to complete
- **🎯 Challenges**: Optional harder problems

**Tips for Practice**:
- Type every example yourself (don't copy-paste)
- Run each cell to see the output
- Modify examples to experiment
- Complete all exercises before moving on

---

## Learning Tips

### Effective Learning Strategies

1. **Code Every Day**: 30 minutes daily beats 5 hours once a week
2. **Type, Don't Copy**: Muscle memory helps learning
3. **Experiment Freely**: Change code to see what happens
4. **Embrace Errors**: Mistakes are learning opportunities
5. **Take Breaks**: Step away when frustrated
6. **Review Regularly**: Revisit earlier chapters

### Note-Taking Suggestions

Create a **learning journal** to track:
- Concepts you understand well
- Topics that need more practice
- Interesting code snippets
- Questions to research later
- Project ideas

Use the [Progress Tracker](PROGRESS_TRACKER.md) to stay organized!

### Time Management

**Suggested Time per Chapter**:
- Presentation: 30-45 minutes
- Practice exercises: 60-90 minutes
- Experimentation: 30 minutes
- Quiz: 30 minutes

**Total course time**: 25-35 hours

---

## Getting Help

### When You're Stuck

1. **Read error messages carefully** - they often explain the problem
2. **Check the [FAQ](FAQ.md)** - common issues are covered
3. **Review the chapter presentation** - refresh your understanding
4. **Experiment with smaller examples** - isolate the problem
5. **Take a break and return later** - fresh perspective helps

### Online Resources

- **Python Documentation**: [docs.python.org](https://docs.python.org/3/)
- **Stack Overflow**: Search for specific error messages
- **Python Tutor**: [pythontutor.com](http://pythontutor.com/) - visualize code execution
- **Real Python**: [realpython.com](https://realpython.com/) - tutorials and guides

### Course Resources

- **[FAQ.md](FAQ.md)**: Common questions and troubleshooting
- **[Quick Reference Sheets](cheat_sheets/)**: One-page summaries
- **[Instructor Guide](INSTRUCTOR_GUIDE.md)**: Additional explanations and answer keys

---

## Ready to Start?

### Your First Steps

1. ✅ Choose your learning method (Colab or Local)
2. ✅ Set up your environment
3. ✅ Run the verification test
4. ✅ Open [Chapter 1: Introduction to Python](chapter_01_introduction/)
5. ✅ Read the presentation
6. ✅ Open `practice.ipynb`
7. ✅ Run your first Python code!

### Set Your Goals

Before starting, decide:
- How much time can you dedicate per week?
- What do you want to build with Python?
- When do you want to finish the course?

Write these down and refer to them for motivation!

---

**🎉 You're all set! Open Chapter 1 and start your Python journey!**

**Questions?** Check the [FAQ](FAQ.md) or [Troubleshooting Guide](FAQ.md#troubleshooting).

**Track your progress**: Use the [Progress Tracker](PROGRESS_TRACKER.md).

---

*Happy Learning! 🐍*
