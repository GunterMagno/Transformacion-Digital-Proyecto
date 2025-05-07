# 🚀 Task Prioritization Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Task Prioritization Manager** is a desktop application that helps you manage tasks efficiently. The software automatically calculates task priority based on **deadline** and **importance**, allowing you to focus on what's most urgent and important.

---

## 💡 Motivation
**"I constantly struggled with task overload - forgetting deadlines, misjudging priorities, and feeling overwhelmed. This tool is my solution to:**  
✅ Stop guessing what to do first  
✅ Never miss important deadlines again  
✅ Feel in control of my daily tasks  

"It's the organizer I wish I had when everything felt urgent but I didn't know where to start."

## 🌟 Key Features

- ✅ **Automatic prioritization**: Calculates task priority based on deadline and importance
- ✅ **Intuitive graphical interface**: Uses `Tkinter` for a simple, user-friendly experience
- ✅ **SQLite database**: Persistent task storage
- ✅ **Advanced functionality**:
  - Add, edit, and delete tasks
  - Mark tasks as completed
  - View pending and completed tasks in separate tables
  - Delete completed tasks individually or clear the entire list

---

## 🛠️ How It Works

### 1️⃣ **Data Input**
The user enters the following data for each task:
- **Name**: Task name
- **Description**: Additional details about the task
- **Deadline**: Due date in `YYYY-MM-DD` format
- **Importance**: Importance level (1-10 scale)

### 2️⃣ **Priority Calculation**
Each task's priority is automatically calculated using:
`priority = importance × 10 - days_remaining`

Where:
- **Importance**: Task importance level (1-10)
- **Days remaining**: Difference between current date and deadline

**Example**:
- For a task with importance `8` and `5` days remaining:  
  `priority = 8 × 10 - 5 = 75`

### 3️⃣ **Database Storage**
Tasks are stored in an SQLite database (`tasks.db`) with this structure:

| Column       | Type     | Description                              |
|--------------|----------|------------------------------------------|
| `id`         | INTEGER  | Unique task identifier                   |
| `name`       | TEXT     | Task name                                |
| `description`| TEXT     | Task description                         |
| `deadline`   | TEXT     | Due date (`YYYY-MM-DD`)                  |
| `importance` | INTEGER  | Importance level (1-10)                  |
| `priority`   | INTEGER  | Automatically calculated priority        |
| `completed`  | INTEGER  | Task status (0: pending, 1: completed)  |

### 4️⃣ **Graphical Interface**
The GUI is divided into two main sections:
- **Pending Tasks**: Shows tasks ordered by priority (highest first)
- **Completed Tasks**: Displays tasks marked as completed

---

## 📥 Installation

### 1️⃣ **Requirements**
- Python 3.x
- `tkinter` library (included with Python)
- `sqlite3` library (included with Python)

### 2️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/Transformacion-Digital-Proyecto.git
cd task-manager
```

### 3️⃣ Run the Program
```
python task_organizer.py
```

## 📝 Example for Adding a high-priority task:
Name: "Finish Project Report"

Description: "Quarterly financial analysis"

Deadline: "2024-07-15"  # 10 days from today

Importance: 9

``` bash
System calculates: priority = (9×10) - 10 = 80
```
